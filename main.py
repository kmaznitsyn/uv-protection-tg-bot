import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path

import httpx
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

from constants import UV_VERY_HIGH, UV_HIGH, UV_EXTREME, UV_MODERATE, AVAILABLE_LANGUAGES, DEFAULT_NOTIFY_HOUR
from translations import TRANSLATIONS

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

USERS_FILE = "users.json"
BOT_TOKEN = os.environ["BOT_TOKEN"]

_uv_cache: dict[tuple[float, float], tuple[datetime, list[dict]]] = {}
CACHE_TTL_SECONDS = 7200  # 2 hours


# ISO 3166-1 alpha-2 country code → language
COUNTRY_TO_LANG: dict[str, str] = {
    # German
    "de": "de", "at": "de", "ch": "de", "li": "de",
    # Ukrainian
    "ua": "uk",
    # French
    "fr": "fr", "mc": "fr", "lu": "fr", "be": "fr",
    # Spanish
    "es": "es", "mx": "es", "ar": "es", "co": "es", "pe": "es",
    "ve": "es", "cl": "es", "ec": "es", "bo": "es", "py": "es",
    "uy": "es", "cr": "es", "pa": "es", "hn": "es", "sv": "es",
    "gt": "es", "ni": "es", "do": "es", "cu": "es",
    # Polish
    "pl": "pl",
    # Italian
    "it": "it", "sm": "it", "va": "it",
}


def t(lang: str, key: str, **kwargs) -> str:
    """Return a translated string, falling back to English."""
    text = TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key) or TRANSLATIONS["en"][key]
    return text.format(**kwargs) if kwargs else text


def load_users() -> dict:
    if Path(USERS_FILE).exists():
        with open(USERS_FILE) as f:
            return json.load(f)
    return {}


def save_users(users: dict):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


async def get_country_code(lat: float, lon: float) -> str | None:
    """Reverse-geocode coordinates to ISO country code via Nominatim."""
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            resp = await client.get(
                "https://nominatim.openstreetmap.org/reverse",
                params={"lat": lat, "lon": lon, "format": "json"},
                headers={"User-Agent": "uv-protection-tg-bot/1.0"},
            )
            resp.raise_for_status()
            return resp.json().get("address", {}).get("country_code")  # lowercase ISO
    except Exception as e:
        logger.warning("Reverse geocoding failed: %s", e)
        return None


def parse_coordinates(text: str) -> tuple[float, float] | None:
    """Parse 'lat, lon' from free text, e.g. '48.1351, 11.5820'."""
    m = re.match(r"^\s*(-?\d+\.?\d*)\s*[,\s]\s*(-?\d+\.?\d*)\s*$", text.strip())
    if m:
        lat, lon = float(m.group(1)), float(m.group(2))
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return lat, lon
    return None


async def geocode_city(query: str) -> tuple[float, float, str] | None:
    """Forward-geocode a city name via Nominatim. Returns (lat, lon, display_name)."""
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            resp = await client.get(
                "https://nominatim.openstreetmap.org/search",
                params={"q": query, "format": "json", "limit": 1},
                headers={"User-Agent": "uv-protection-tg-bot/1.0"},
            )
            resp.raise_for_status()
            results = resp.json()
        if not results:
            return None
        r = results[0]
        return float(r["lat"]), float(r["lon"]), r.get("display_name", query)
    except Exception as e:
        logger.warning("Forward geocoding failed for %r: %s", query, e)
        return None


async def get_uv_forecast(lat: float, lon: float) -> list[dict]:
    """Fetch today's hourly UV index from Open-Meteo, cached for 2 hours."""
    key = (round(lat, 2), round(lon, 2))
    cache_entry = _uv_cache.get(key)
    if cache_entry and (datetime.now() - cache_entry[0]).total_seconds() < CACHE_TTL_SECONDS:
        logger.debug("UV cache hit for %s", key)
        return cache_entry[1]

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "hourly": "uv_index",
                "forecast_days": 1,
                "timezone": "auto",
            },
        )
        resp.raise_for_status()
        data = resp.json()

    result = [
        {"time": ts, "uv": uv}
        for ts, uv in zip(data["hourly"]["time"], data["hourly"]["uv_index"])
    ]
    _uv_cache[key] = (datetime.now(), result)
    logger.debug("UV cache stored for %s", key)
    return result


def uv_level_label(uv: float, lang: str) -> str:
    if uv >= UV_EXTREME:
        return t(lang, "uv_level_extreme")
    if uv >= UV_VERY_HIGH:
        return t(lang, "uv_level_very_high")
    if uv >= UV_HIGH:
        return t(lang, "uv_level_high")
    return t(lang, "uv_level_moderate")


def _uv_by_hour(hourly_uv: list[dict]) -> dict[int, float]:
    today = datetime.now().date().isoformat()
    return {
        int(e["time"][11:13]): e["uv"]
        for e in hourly_uv
        if e["time"].startswith(today)
    }


def _uv_lines_and_peak(
    forecast: list[tuple[int, float]], lang: str, mark_protection: bool = False
) -> list[str]:
    lines = []
    for hour, uv in forecast:
        line = t(lang, "uv_hour_line", hour=hour, uv=uv, level=uv_level_label(uv, lang))
        if mark_protection and uv >= UV_MODERATE:
            line += " ⚠️"
        lines.append(line)
    peak_hour, peak_uv = max(forecast, key=lambda x: x[1])
    lines.append(t(lang, "uv_peak", hour=peak_hour, uv=peak_uv))
    lines.append(t(lang, "uv_tips"))
    return lines


def build_uv_message(hourly_uv: list[dict], lang: str) -> str:
    """Next 3 hours — used by the ☀️ UV button."""
    current_hour = datetime.now().hour
    uv_map = _uv_by_hour(hourly_uv)

    forecast = [
        (h, uv_map[h])
        for h in range(current_hour, min(current_hour + 3, 24))
        if h in uv_map
    ]

    if not forecast or max(uv for _, uv in forecast) < UV_MODERATE:
        return t(lang, "uv_clear_header") + "\n\n" + t(lang, "uv_clear_body")

    lines = [t(lang, "uv_header") + "\n", t(lang, "uv_apply")]
    lines += _uv_lines_and_peak(forecast, lang, mark_protection=True)
    return "\n".join(lines)


def build_uv_day_message(hourly_uv: list[dict], lang: str) -> str:
    """Daily scheduled notification — yes/no sunscreen needed today + peak time."""
    uv_map = _uv_by_hour(hourly_uv)
    all_hours = [(h, uv_map[h]) for h in sorted(uv_map)]

    if not all_hours or max(uv for _, uv in all_hours) < UV_MODERATE:
        return t(lang, "uv_clear_header") + "\n\n" + t(lang, "uv_day_clear_body")

    peak_hour, peak_uv = max(all_hours, key=lambda x: x[1])
    return "\n".join([
        t(lang, "uv_day_header") + "\n",
        t(lang, "uv_day_needed"),
        t(lang, "uv_peak", hour=peak_hour, uv=peak_uv),
        t(lang, "uv_tips"),
    ])


def user_lang(users: dict, user_id: str) -> str:
    return users.get(user_id, {}).get("lang", "en")


def build_main_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [t(lang, "btn_uv"), t(lang, "btn_settime")],
            [t(lang, "btn_location"), t(lang, "btn_language")],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


def build_location_request_keyboard(lang: str) -> ReplyKeyboardMarkup:
    """One-time keyboard shown while awaiting a location update."""
    return ReplyKeyboardMarkup(
        [[KeyboardButton(t(lang, "share_location_btn"), request_location=True)]],
        one_time_keyboard=True,
        resize_keyboard=True,
    )


def detect_button_action(text: str) -> str | None:
    """Map any language's button label to its action name."""
    for lang_code in AVAILABLE_LANGUAGES:
        if text == t(lang_code, "btn_uv"):
            return "uv"
        if text == t(lang_code, "btn_settime"):
            return "settime"
        if text == t(lang_code, "btn_language"):
            return "language"
        if text == t(lang_code, "btn_location"):
            return "location"
    return None


def build_settime_keyboard() -> InlineKeyboardMarkup:
    hours = range(6, 22)
    rows = [
        [InlineKeyboardButton(f"{h:02d}:00", callback_data=f"settime:{h}") for h in list(hours)[i:i+4]]
        for i in range(0, 16, 4)
    ]
    return InlineKeyboardMarkup(rows)


def build_language_keyboard() -> InlineKeyboardMarkup:
    options = [
        ("🇬🇧 English", "en"), ("🇩🇪 Deutsch", "de"), ("🇺🇦 Українська", "uk"),
        ("🇫🇷 Français", "fr"), ("🇪🇸 Español", "es"), ("🇵🇱 Polski", "pl"), ("🇮🇹 Italiano", "it"),
    ]
    rows = [
        [InlineKeyboardButton(label, callback_data=f"lang:{code}") for label, code in options[i:i+3]]
        for i in range(0, len(options), 3)
    ]
    return InlineKeyboardMarkup(rows)


# ── Handlers ──────────────────────────────────────────────────────────────────

async def send_welcome_prompt(update: Update, lang: str) -> None:
    """Send the welcome message with location-share button."""
    assert update.message is not None
    keyboard = [[KeyboardButton(t(lang, "share_location_btn"), request_location=True)]]
    await update.message.reply_text(
        t(lang, "welcome"),
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True),
    )


async def ensure_location(update: Update, users: dict, user_id: str) -> bool:
    """Return True if user has a location. Otherwise send the welcome prompt and return False."""
    if users.get(user_id, {}).get("lat"):
        return True
    lang = user_lang(users, user_id)
    await send_welcome_prompt(update, lang)
    return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    users = load_users()
    assert update.effective_user is not None
    lang = user_lang(users, str(update.effective_user.id))
    await send_welcome_prompt(update, lang)


async def _save_location(
    user_id: str,
    first_name: str,
    lat: float,
    lon: float,
    context: ContextTypes.DEFAULT_TYPE,
) -> tuple[str, bool, str | None]:
    """Persist location, detect language. Returns (lang, is_new, country_code)."""
    assert context.user_data is not None
    context.user_data.pop("awaiting_location", None)

    country_code = await get_country_code(lat, lon)
    detected_lang = COUNTRY_TO_LANG.get(country_code or "", "en")

    users = load_users()
    existing = users.get(user_id, {})
    is_new = not existing.get("lat")
    lang = existing.get("lang") or detected_lang

    users[user_id] = {
        **existing,
        "name": first_name,
        "lat": lat,
        "lon": lon,
        "notify_hour": existing.get("notify_hour", DEFAULT_NOTIFY_HOUR),
        "lang": lang,
    }
    save_users(users)
    return lang, is_new, country_code


async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.effective_user is not None
    assert update.message is not None
    assert update.message.location is not None
    user = update.effective_user
    loc = update.message.location
    lang, is_new, country_code = await _save_location(
        str(user.id), user.first_name or "", loc.latitude, loc.longitude, context
    )
    key = "location_saved" if is_new else "location_updated"
    display = f"{loc.latitude:.4f}, {loc.longitude:.4f}"
    await update.message.reply_text(
        t(lang, key, location=display),
        parse_mode="Markdown",
        reply_markup=build_main_keyboard(lang),
    )
    if is_new and country_code:
        await update.message.reply_text(t(lang, "lang_detected"), parse_mode="Markdown")


async def cmd_uv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.effective_user is not None
    assert update.message is not None
    user_id = str(update.effective_user.id)
    users = load_users()
    lang = user_lang(users, user_id)

    if not await ensure_location(update, users, user_id):
        return

    await update.message.reply_text(t(lang, "fetching"))
    try:
        data = users[user_id]
        hourly = await get_uv_forecast(data["lat"], data["lon"])
        await update.message.reply_text(build_uv_message(hourly, lang), parse_mode="Markdown")
    except Exception as e:
        logger.error("UV fetch error: %s", e)
        await update.message.reply_text(t(lang, "error"))


async def cmd_settime(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.effective_user is not None
    assert update.message is not None
    user_id = str(update.effective_user.id)
    users = load_users()
    lang = user_lang(users, user_id)

    if not await ensure_location(update, users, user_id):
        return

    args = context.args
    if not args or not args[0].isdigit() or not (0 <= int(args[0]) <= 23):
        await update.message.reply_text(t(lang, "time_usage"), parse_mode="Markdown")
        return

    hour = int(args[0])
    users[user_id]["notify_hour"] = hour
    save_users(users)
    await update.message.reply_text(t(lang, "time_set", hour=hour), parse_mode="Markdown")


async def cmd_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.effective_user is not None
    assert update.message is not None
    user_id = str(update.effective_user.id)
    users = load_users()
    lang = user_lang(users, user_id)

    args = context.args
    if not args or args[0].lower() not in AVAILABLE_LANGUAGES:
        await update.message.reply_text(t(lang, "lang_usage"), parse_mode="Markdown")
        return

    new_lang = args[0].lower()
    if user_id in users:
        users[user_id]["lang"] = new_lang
    else:
        users[user_id] = {"lang": new_lang, "notify_hour": DEFAULT_NOTIFY_HOUR}
    save_users(users)
    await update.message.reply_text(t(new_lang, "lang_set"))


async def handle_manual_location(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    text: str,
    lang: str,
) -> None:
    """Handle free-text location input: coordinates or city name."""
    assert update.effective_user is not None
    assert update.message is not None
    coords = parse_coordinates(text)
    if coords:
        lat, lon = coords
        display = f"{lat:.4f}, {lon:.4f}"
    else:
        result = await geocode_city(text)
        if not result:
            await update.message.reply_text(t(lang, "location_not_found"))
            return
        lat, lon, display = result
        # Trim long Nominatim display names to first two parts
        display = ", ".join(display.split(", ")[:2])

    user = update.effective_user
    lang, _, _ = await _save_location(str(user.id), user.first_name or "", lat, lon, context)
    await update.message.reply_text(
        t(lang, "location_updated", location=display),
        parse_mode="Markdown",
        reply_markup=build_main_keyboard(lang),
    )


async def handle_menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message is not None
    assert update.message.text is not None
    assert update.effective_user is not None
    assert context.user_data is not None
    text = update.message.text
    user_id = str(update.effective_user.id)
    users = load_users()
    lang = user_lang(users, user_id)

    # If we're awaiting a manual location, handle text input unless a button was pressed
    if context.user_data.get("awaiting_location"):
        # Always allow input in this state regardless of whether location exists
        pass
    elif not users.get(user_id, {}).get("lat") and detect_button_action(text) != "location":
        # No location yet and not asking to change it — show welcome prompt
        await send_welcome_prompt(update, lang)
        return

    if context.user_data.get("awaiting_location"):
        if detect_button_action(text) is None:
            await handle_manual_location(update, context, text, lang)
            return
        # A different button was tapped — cancel the awaiting state and fall through
        context.user_data.pop("awaiting_location", None)

    action = detect_button_action(text)
    if action == "uv":
        await cmd_uv(update, context)
    elif action == "settime":
        await update.message.reply_text(t(lang, "settime_prompt"), reply_markup=build_settime_keyboard())
    elif action == "language":
        await update.message.reply_text(t(lang, "language_prompt"), reply_markup=build_language_keyboard())
    elif action == "location":
        context.user_data["awaiting_location"] = True
        await update.message.reply_text(
            t(lang, "location_change_prompt"),
            reply_markup=build_location_request_keyboard(lang),
        )


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.callback_query is not None
    assert update.effective_user is not None
    assert update.effective_chat is not None
    query = update.callback_query
    await query.answer()

    assert query.data is not None
    user_id = str(update.effective_user.id)
    users = load_users()
    lang = user_lang(users, user_id)
    data = query.data

    if data.startswith("settime:"):
        hour = int(data.split(":")[1])
        if user_id in users:
            users[user_id]["notify_hour"] = hour
            save_users(users)
        await query.edit_message_text(t(lang, "time_set", hour=hour), parse_mode="Markdown")

    elif data.startswith("lang:"):
        new_lang = data.split(":")[1]
        if user_id in users:
            users[user_id]["lang"] = new_lang
        else:
            users[user_id] = {"lang": new_lang, "notify_hour": DEFAULT_NOTIFY_HOUR}
        save_users(users)
        await query.edit_message_text(t(new_lang, "lang_set"))
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="✅",
            reply_markup=build_main_keyboard(new_lang),
        )


# ── Daily scheduler ───────────────────────────────────────────────────────────

async def send_daily_notifications(application: Application) -> None:
    current_hour = datetime.now().hour
    users = load_users()

    for user_id, data in users.items():
        if data.get("notify_hour", DEFAULT_NOTIFY_HOUR) != current_hour:
            continue
        lang = data.get("lang", "en")
        try:
            hourly = await get_uv_forecast(data["lat"], data["lon"])
            await application.bot.send_message(
                chat_id=int(user_id),
                text=build_uv_day_message(hourly, lang),
                parse_mode="Markdown",
            )
            logger.info("Sent UV notification to user %s (%s)", user_id, lang)
        except Exception as e:
            logger.error("Failed to notify user %s: %s", user_id, e)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("uv", cmd_uv))
    application.add_handler(CommandHandler("settime", cmd_settime))
    application.add_handler(CommandHandler("language", cmd_language))
    application.add_handler(MessageHandler(filters.LOCATION, handle_location))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_buttons))
    application.add_handler(CallbackQueryHandler(handle_callback))

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_daily_notifications,
        trigger="cron",
        minute=0,
        args=[application],
    )
    scheduler.start()

    logger.info("Bot started.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
