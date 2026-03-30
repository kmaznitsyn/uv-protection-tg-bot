TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        "welcome": (
            "👋 Welcome to the UV Protection Bot!\n\n"
            "I check the daily UV index for your location and remind you "
            "when to apply sunscreen.\n\n"
            "Please share your location:"
        ),
        "share_location_btn": "📍 Share my location",
        "location_saved": (
            "✅ Location saved!\n\n"
            "You'll receive a daily UV protection reminder at *10:00*.\n\n"
            "Use the buttons below to check UV, change notification time, or switch language."
        ),
        "location_updated": "📍 Location updated: *{location}*",
        "location_change_prompt": (
            "📍 Send your location with the button below, type a city name (e.g. *Berlin*), "
            "or enter coordinates (e.g. *48.1351, 11.5820*):"
        ),
        "location_not_found": "❌ Location not found. Please try a different city name or check the coordinates.",
        "fetching": "⏳ Fetching UV data…",
        "no_location": "Please share your location first with /start.",
        "error": "❌ Error fetching UV data. Please try again later.",
        "time_set": "✅ Notification time set to *{hour:02d}:00*.",
        "time_usage": "Usage: `/settime HH` (e.g. `/settime 09` for 9:00)",
        "settime_prompt": "🕐 Choose your daily notification time:",
        "lang_set": "✅ Language set to English.",
        "lang_usage": (
            "Usage: `/language CODE`\n"
            "Available: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Choose your language:",
        "lang_detected": "🌍 Language auto-detected: *English*. Use the button below to change.",
        "uv_clear_header": "☁️ *UV Protection Today*",
        "uv_clear_body": "The UV index is low for the next 3 hours (< 3).\nNo sunscreen needed right now. Enjoy your day! 😊",
        "uv_day_header": "☀️ *UV Protection Today*",
        "uv_day_needed": "🧴 Sunscreen is recommended today!",
        "uv_day_clear_body": "The UV index is low all day (< 3).\nNo sunscreen needed today. Enjoy your day! 😊",
        "uv_header": "☀️ *UV Forecast — Next 3 Hours*",
        "uv_apply": "UV protection status:\n",
        "uv_hour_line": "  {hour:02d}:00 — UV Index {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Peak: {hour:02d}:00 (UV Index {uv:.1f})",
        "uv_tips": (
            "\n💡 *Tips:*\n"
            "• Reapply every 2 hours\n"
            "• Reapply after sweating or swimming\n"
            "• Use SPF 30 or higher"
        ),
        "uv_level_moderate": "🟢 Moderate",
        "uv_level_high": "🟡 High",
        "uv_level_very_high": "🟠 Very High",
        "uv_level_extreme": "🔴 Extreme",
        "btn_uv": "☀️ UV Index",
        "btn_settime": "🕐 Notification time",
        "btn_language": "🌍 Language",
        "btn_location": "📍 Change location",
    },
    "de": {
        "welcome": (
            "👋 Willkommen beim UV-Schutz-Bot!\n\n"
            "Ich prüfe täglich den UV-Index für deinen Standort und erinnere dich, "
            "wann du UV-Schutz-Creme auftragen solltest.\n\n"
            "Bitte teile deinen Standort:"
        ),
        "share_location_btn": "📍 Meinen Standort teilen",
        "location_saved": (
            "✅ Standort gespeichert!\n\n"
            "Du erhältst täglich um *10:00 Uhr* eine UV-Schutz-Erinnerung.\n\n"
            "Nutze die Buttons unten, um den UV-Index abzurufen, die Uhrzeit zu ändern oder die Sprache zu wechseln."
        ),
        "location_updated": "📍 Standort aktualisiert: *{location}*",
        "location_change_prompt": (
            "📍 Sende deinen Standort über den Button, gib einen Stadtnamen ein (z.B. *Berlin*) "
            "oder gib Koordinaten ein (z.B. *48.1351, 11.5820*):"
        ),
        "location_not_found": "❌ Ort nicht gefunden. Bitte versuche einen anderen Stadtnamen oder überprüfe die Koordinaten.",
        "fetching": "⏳ Rufe UV-Daten ab…",
        "no_location": "Bitte teile zuerst deinen Standort mit /start.",
        "error": "❌ Fehler beim Abrufen der UV-Daten. Bitte später erneut versuchen.",
        "time_set": "✅ Benachrichtigungszeit auf *{hour:02d}:00 Uhr* gesetzt.",
        "time_usage": "Verwendung: `/settime HH` (z.B. `/settime 09` für 9:00 Uhr)",
        "settime_prompt": "🕐 Wähle deine tägliche Benachrichtigungszeit:",
        "lang_set": "✅ Sprache auf Deutsch gesetzt.",
        "lang_usage": (
            "Verwendung: `/language CODE`\n"
            "Verfügbar: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Wähle deine Sprache:",
        "lang_detected": "🌍 Sprache automatisch erkannt: *Deutsch*. Ändern mit dem Button unten.",
        "uv_clear_header": "☁️ *UV-Schutz heute*",
        "uv_clear_body": "Der UV-Index ist in den nächsten 3 Stunden niedrig (< 3).\nJetzt keine UV-Schutz-Creme notwendig. Genießen Sie Ihren Tag! 😊",
        "uv_day_header": "☀️ *UV-Schutz heute*",
        "uv_day_needed": "🧴 Heute Sonnenschutz-Creme empfohlen!",
        "uv_day_clear_body": "Der UV-Index ist heute den ganzen Tag niedrig (< 3).\nKeine UV-Schutz-Creme notwendig. Genießen Sie Ihren Tag! 😊",
        "uv_header": "☀️ *UV-Prognose — Nächste 3 Stunden*",
        "uv_apply": "UV-Schutz-Status:\n",
        "uv_hour_line": "  {hour:02d}:00 Uhr — UV-Index {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Spitzenwert: {hour:02d}:00 Uhr (UV-Index {uv:.1f})",
        "uv_tips": (
            "\n💡 *Tipps:*\n"
            "• Creme alle 2 Stunden erneut auftragen\n"
            "• Nach dem Schwitzen oder Schwimmen neu eincremen\n"
            "• Lichtschutzfaktor (LSF) 30 oder höher verwenden"
        ),
        "uv_level_moderate": "🟢 Mäßig",
        "uv_level_high": "🟡 Hoch",
        "uv_level_very_high": "🟠 Sehr hoch",
        "uv_level_extreme": "🔴 Extrem",
        "btn_uv": "☀️ UV-Index",
        "btn_settime": "🕐 Benachrichtigungszeit",
        "btn_language": "🌍 Sprache",
        "btn_location": "📍 Standort ändern",
    },
    "uk": {
        "welcome": (
            "👋 Ласкаво просимо до UV-захист бота!\n\n"
            "Я щодня перевіряю UV-індекс для вашого місця та нагадую, "
            "коли потрібно наносити сонцезахисний крем.\n\n"
            "Будь ласка, поділіться місцезнаходженням:"
        ),
        "share_location_btn": "📍 Поділитися місцезнаходженням",
        "location_saved": (
            "✅ Місцезнаходження збережено!\n\n"
            "Ви отримуватимете щоденне нагадування о *10:00*.\n\n"
            "Використовуйте кнопки нижче для перевірки UV, зміни часу або мови."
        ),
        "location_updated": "📍 Місцезнаходження оновлено: *{location}*",
        "location_change_prompt": (
            "📍 Надішліть місцезнаходження кнопкою, введіть назву міста (наприклад *Київ*) "
            "або координати (наприклад *50.4501, 30.5234*):"
        ),
        "location_not_found": "❌ Місце не знайдено. Спробуйте іншу назву міста або перевірте координати.",
        "fetching": "⏳ Отримання UV-даних…",
        "no_location": "Будь ласка, спочатку поділіться місцезнаходженням через /start.",
        "error": "❌ Помилка отримання UV-даних. Спробуйте пізніше.",
        "time_set": "✅ Час сповіщень встановлено на *{hour:02d}:00*.",
        "time_usage": "Використання: `/settime HH` (наприклад `/settime 09` для 9:00)",
        "settime_prompt": "🕐 Оберіть час щоденного сповіщення:",
        "lang_set": "✅ Мову змінено на українську.",
        "lang_usage": (
            "Використання: `/language CODE`\n"
            "Доступні: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Оберіть мову:",
        "lang_detected": "🌍 Мова визначена автоматично: *Українська*. Змінити кнопкою нижче.",
        "uv_clear_header": "☁️ *UV-захист сьогодні*",
        "uv_clear_body": "UV-індекс у найближчі 3 години низький (< 3).\nЗараз сонцезахисний крем не потрібен. Гарного дня! 😊",
        "uv_day_header": "☀️ *UV-захист сьогодні*",
        "uv_day_needed": "🧴 Сьогодні рекомендується сонцезахисний крем!",
        "uv_day_clear_body": "UV-індекс сьогодні весь день низький (< 3).\nСонцезахисний крем не потрібен. Гарного дня! 😊",
        "uv_header": "☀️ *UV-прогноз — Наступні 3 години*",
        "uv_apply": "UV-статус захисту:\n",
        "uv_hour_line": "  {hour:02d}:00 — UV-індекс {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Пік: {hour:02d}:00 (UV-індекс {uv:.1f})",
        "uv_tips": (
            "\n💡 *Поради:*\n"
            "• Повторно наносити кожні 2 години\n"
            "• Наносити повторно після потовиділення або плавання\n"
            "• Використовувати SPF 30 або вище"
        ),
        "uv_level_moderate": "🟢 Помірний",
        "uv_level_high": "🟡 Високий",
        "uv_level_very_high": "🟠 Дуже високий",
        "uv_level_extreme": "🔴 Екстремальний",
        "btn_uv": "☀️ UV-індекс",
        "btn_settime": "🕐 Час сповіщень",
        "btn_language": "🌍 Мова",
        "btn_location": "📍 Змінити місце",
    },
    "fr": {
        "welcome": (
            "👋 Bienvenue sur le Bot Protection UV!\n\n"
            "Je vérifie l'indice UV quotidien pour votre position et vous rappelle "
            "quand appliquer de la crème solaire.\n\n"
            "Veuillez partager votre position:"
        ),
        "share_location_btn": "📍 Partager ma position",
        "location_saved": (
            "✅ Position enregistrée!\n\n"
            "Vous recevrez un rappel quotidien à *10:00*.\n\n"
            "Utilisez les boutons ci-dessous pour vérifier l'UV, changer l'heure ou la langue."
        ),
        "location_updated": "📍 Position mise à jour: *{location}*",
        "location_change_prompt": (
            "📍 Envoyez votre position via le bouton, tapez un nom de ville (ex. *Paris*) "
            "ou des coordonnées (ex. *48.8566, 2.3522*):"
        ),
        "location_not_found": "❌ Lieu introuvable. Essayez un autre nom de ville ou vérifiez les coordonnées.",
        "fetching": "⏳ Récupération des données UV…",
        "no_location": "Veuillez d'abord partager votre position avec /start.",
        "error": "❌ Erreur lors de la récupération des données UV. Réessayez plus tard.",
        "time_set": "✅ Heure de notification réglée à *{hour:02d}:00*.",
        "time_usage": "Utilisation: `/settime HH` (ex. `/settime 09` pour 9h00)",
        "settime_prompt": "🕐 Choisissez l'heure de notification quotidienne:",
        "lang_set": "✅ Langue définie sur Français.",
        "lang_usage": (
            "Utilisation: `/language CODE`\n"
            "Disponibles: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Choisissez votre langue:",
        "lang_detected": "🌍 Langue détectée automatiquement: *Français*. Changer avec le bouton ci-dessous.",
        "uv_clear_header": "☁️ *Protection UV aujourd'hui*",
        "uv_clear_body": "L'indice UV est faible pour les 3 prochaines heures (< 3).\nAucune crème solaire nécessaire pour l'instant. Bonne journée! 😊",
        "uv_day_header": "☀️ *Protection UV aujourd'hui*",
        "uv_day_needed": "🧴 Crème solaire recommandée aujourd'hui!",
        "uv_day_clear_body": "L'indice UV est faible toute la journée (< 3).\nAucune crème solaire nécessaire aujourd'hui. Bonne journée! 😊",
        "uv_header": "☀️ *Prévisions UV — 3 prochaines heures*",
        "uv_apply": "Statut de protection UV:\n",
        "uv_hour_line": "  {hour:02d}h00 — Indice UV {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Pic: {hour:02d}h00 (Indice UV {uv:.1f})",
        "uv_tips": (
            "\n💡 *Conseils:*\n"
            "• Réappliquer toutes les 2 heures\n"
            "• Réappliquer après transpiration ou baignade\n"
            "• Utiliser un SPF 30 ou plus"
        ),
        "uv_level_moderate": "🟢 Modéré",
        "uv_level_high": "🟡 Élevé",
        "uv_level_very_high": "🟠 Très élevé",
        "uv_level_extreme": "🔴 Extrême",
        "btn_uv": "☀️ Indice UV",
        "btn_settime": "🕐 Heure de notification",
        "btn_language": "🌍 Langue",
        "btn_location": "📍 Changer position",
    },
    "es": {
        "welcome": (
            "👋 ¡Bienvenido al Bot de Protección UV!\n\n"
            "Verifico el índice UV diario para tu ubicación y te recuerdo "
            "cuándo aplicar protector solar.\n\n"
            "Por favor, comparte tu ubicación:"
        ),
        "share_location_btn": "📍 Compartir mi ubicación",
        "location_saved": (
            "✅ ¡Ubicación guardada!\n\n"
            "Recibirás un recordatorio diario a las *10:00*.\n\n"
            "Usa los botones de abajo para consultar el UV, cambiar la hora o el idioma."
        ),
        "location_updated": "📍 Ubicación actualizada: *{location}*",
        "location_change_prompt": (
            "📍 Envía tu ubicación con el botón, escribe un nombre de ciudad (ej. *Madrid*) "
            "o introduce coordenadas (ej. *40.4168, -3.7038*):"
        ),
        "location_not_found": "❌ Ubicación no encontrada. Prueba otro nombre de ciudad o comprueba las coordenadas.",
        "fetching": "⏳ Obteniendo datos UV…",
        "no_location": "Por favor, comparte tu ubicación primero con /start.",
        "error": "❌ Error al obtener datos UV. Por favor, inténtalo más tarde.",
        "time_set": "✅ Hora de notificación establecida a las *{hour:02d}:00*.",
        "time_usage": "Uso: `/settime HH` (ej. `/settime 09` para las 9:00)",
        "settime_prompt": "🕐 Elige tu hora de notificación diaria:",
        "lang_set": "✅ Idioma establecido en Español.",
        "lang_usage": (
            "Uso: `/language CODE`\n"
            "Disponibles: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Elige tu idioma:",
        "lang_detected": "🌍 Idioma detectado automáticamente: *Español*. Cambiar con el botón de abajo.",
        "uv_clear_header": "☁️ *Protección UV hoy*",
        "uv_clear_body": "El índice UV es bajo en las próximas 3 horas (< 3).\n¡No se necesita protector solar ahora. Disfruta el día! 😊",
        "uv_day_header": "☀️ *Protección UV hoy*",
        "uv_day_needed": "🧴 ¡Protector solar recomendado hoy!",
        "uv_day_clear_body": "El índice UV es bajo todo el día (< 3).\n¡No se necesita protector solar hoy. Disfruta el día! 😊",
        "uv_header": "☀️ *Previsión UV — Próximas 3 horas*",
        "uv_apply": "Estado de protección UV:\n",
        "uv_hour_line": "  {hour:02d}:00 — Índice UV {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Pico: {hour:02d}:00 (Índice UV {uv:.1f})",
        "uv_tips": (
            "\n💡 *Consejos:*\n"
            "• Reaplicar cada 2 horas\n"
            "• Reaplicar después de sudar o nadar\n"
            "• Usar FPS 30 o superior"
        ),
        "uv_level_moderate": "🟢 Moderado",
        "uv_level_high": "🟡 Alto",
        "uv_level_very_high": "🟠 Muy alto",
        "uv_level_extreme": "🔴 Extremo",
        "btn_uv": "☀️ Índice UV",
        "btn_settime": "🕐 Hora de notificación",
        "btn_language": "🌍 Idioma",
        "btn_location": "📍 Cambiar ubicación",
    },
    "pl": {
        "welcome": (
            "👋 Witaj w Bocie Ochrony UV!\n\n"
            "Codziennie sprawdzam indeks UV dla Twojej lokalizacji i przypominam, "
            "kiedy należy nałożyć krem z filtrem.\n\n"
            "Proszę udostępnij swoją lokalizację:"
        ),
        "share_location_btn": "📍 Udostępnij moją lokalizację",
        "location_saved": (
            "✅ Lokalizacja zapisana!\n\n"
            "Będziesz otrzymywać codzienne przypomnienie o *10:00*.\n\n"
            "Użyj przycisków poniżej, aby sprawdzić UV, zmienić godzinę lub język."
        ),
        "location_updated": "📍 Lokalizacja zaktualizowana: *{location}*",
        "location_change_prompt": (
            "📍 Wyślij lokalizację przyciskiem, wpisz nazwę miasta (np. *Warszawa*) "
            "lub podaj współrzędne (np. *52.2297, 21.0122*):"
        ),
        "location_not_found": "❌ Nie znaleziono miejsca. Spróbuj innej nazwy miasta lub sprawdź współrzędne.",
        "fetching": "⏳ Pobieranie danych UV…",
        "no_location": "Proszę najpierw udostępnij swoją lokalizację przez /start.",
        "error": "❌ Błąd pobierania danych UV. Spróbuj ponownie później.",
        "time_set": "✅ Godzina powiadomień ustawiona na *{hour:02d}:00*.",
        "time_usage": "Użycie: `/settime HH` (np. `/settime 09` dla 9:00)",
        "settime_prompt": "🕐 Wybierz godzinę codziennego powiadomienia:",
        "lang_set": "✅ Język ustawiony na Polski.",
        "lang_usage": (
            "Użycie: `/language CODE`\n"
            "Dostępne: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Wybierz swój język:",
        "lang_detected": "🌍 Język wykryty automatycznie: *Polski*. Zmień przyciskiem poniżej.",
        "uv_clear_header": "☁️ *Ochrona UV dzisiaj*",
        "uv_clear_body": "Indeks UV przez następne 3 godziny jest niski (< 3).\nKrem z filtrem nie jest teraz potrzebny. Miłego dnia! 😊",
        "uv_day_header": "☀️ *Ochrona UV dzisiaj*",
        "uv_day_needed": "🧴 Dzisiaj zalecany krem z filtrem!",
        "uv_day_clear_body": "Indeks UV jest dziś przez cały dzień niski (< 3).\nKrem z filtrem nie jest dzisiaj potrzebny. Miłego dnia! 😊",
        "uv_header": "☀️ *Prognoza UV — Następne 3 godziny*",
        "uv_apply": "Status ochrony UV:\n",
        "uv_hour_line": "  {hour:02d}:00 — Indeks UV {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Szczyt: {hour:02d}:00 (Indeks UV {uv:.1f})",
        "uv_tips": (
            "\n💡 *Wskazówki:*\n"
            "• Nakładać ponownie co 2 godziny\n"
            "• Nakładać ponownie po poceniu się lub pływaniu\n"
            "• Używać SPF 30 lub wyższego"
        ),
        "uv_level_moderate": "🟢 Umiarkowany",
        "uv_level_high": "🟡 Wysoki",
        "uv_level_very_high": "🟠 Bardzo wysoki",
        "uv_level_extreme": "🔴 Ekstremalny",
        "btn_uv": "☀️ Indeks UV",
        "btn_settime": "🕐 Godzina powiadomień",
        "btn_language": "🌍 Język",
        "btn_location": "📍 Zmień lokalizację",
    },
    "it": {
        "welcome": (
            "👋 Benvenuto al Bot Protezione UV!\n\n"
            "Controllo ogni giorno l'indice UV per la tua posizione e ti ricordo "
            "quando applicare la crema solare.\n\n"
            "Condividi la tua posizione:"
        ),
        "share_location_btn": "📍 Condividi la mia posizione",
        "location_saved": (
            "✅ Posizione salvata!\n\n"
            "Riceverai un promemoria quotidiano alle *10:00*.\n\n"
            "Usa i pulsanti qui sotto per controllare l'UV, cambiare l'orario o la lingua."
        ),
        "location_updated": "📍 Posizione aggiornata: *{location}*",
        "location_change_prompt": (
            "📍 Invia la tua posizione con il pulsante, digita un nome di città (es. *Roma*) "
            "o inserisci le coordinate (es. *41.9028, 12.4964*):"
        ),
        "location_not_found": "❌ Luogo non trovato. Prova un altro nome di città o verifica le coordinate.",
        "fetching": "⏳ Recupero dati UV…",
        "no_location": "Per favore condividi prima la tua posizione con /start.",
        "error": "❌ Errore nel recupero dei dati UV. Riprova più tardi.",
        "time_set": "✅ Orario notifica impostato alle *{hour:02d}:00*.",
        "time_usage": "Uso: `/settime HH` (es. `/settime 09` per le 9:00)",
        "settime_prompt": "🕐 Scegli l'orario di notifica giornaliero:",
        "lang_set": "✅ Lingua impostata su Italiano.",
        "lang_usage": (
            "Uso: `/language CODE`\n"
            "Disponibili: `en` 🇬🇧  `de` 🇩🇪  `uk` 🇺🇦  `fr` 🇫🇷  `es` 🇪🇸  `pl` 🇵🇱  `it` 🇮🇹"
        ),
        "language_prompt": "🌍 Scegli la tua lingua:",
        "lang_detected": "🌍 Lingua rilevata automaticamente: *Italiano*. Cambia con il pulsante qui sotto.",
        "uv_clear_header": "☁️ *Protezione UV oggi*",
        "uv_clear_body": "L'indice UV è basso per le prossime 3 ore (< 3).\nNessuna crema solare necessaria al momento. Buona giornata! 😊",
        "uv_day_header": "☀️ *Protezione UV oggi*",
        "uv_day_needed": "🧴 Crema solare consigliata oggi!",
        "uv_day_clear_body": "L'indice UV è basso tutto il giorno (< 3).\nNessuna crema solare necessaria oggi. Buona giornata! 😊",
        "uv_header": "☀️ *Previsione UV — Prossime 3 ore*",
        "uv_apply": "Stato protezione UV:\n",
        "uv_hour_line": "  {hour:02d}:00 — Indice UV {uv:.1f} ({level})",
        "uv_peak": "\n🕐 Picco: {hour:02d}:00 (Indice UV {uv:.1f})",
        "uv_tips": (
            "\n💡 *Consigli:*\n"
            "• Riapplicare ogni 2 ore\n"
            "• Riapplicare dopo aver sudato o nuotato\n"
            "• Usare SPF 30 o superiore"
        ),
        "uv_level_moderate": "🟢 Moderato",
        "uv_level_high": "🟡 Alto",
        "uv_level_very_high": "🟠 Molto alto",
        "uv_level_extreme": "🔴 Estremo",
        "btn_uv": "☀️ Indice UV",
        "btn_settime": "🕐 Orario notifica",
        "btn_language": "🌍 Lingua",
        "btn_location": "📍 Cambia posizione",
    },
}
