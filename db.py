import os
import logging
from typing import Any

import asyncpg

logger = logging.getLogger(__name__)

_pool: asyncpg.Pool | None = None


async def get_pool() -> asyncpg.Pool:
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(os.environ["DATABASE_URL"], min_size=1, max_size=5)
        await _init_schema(_pool)
    return _pool


async def _init_schema(pool: asyncpg.Pool) -> None:
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id  BIGINT PRIMARY KEY,
                name     TEXT,
                lat      DOUBLE PRECISION,
                lon      DOUBLE PRECISION,
                notify_hour INTEGER NOT NULL DEFAULT 10,
                lang     TEXT NOT NULL DEFAULT 'en'
            )
        """)
    logger.info("DB schema ready.")


# ── CRUD ──────────────────────────────────────────────────────────────────────

async def get_user(user_id: int) -> dict[str, Any] | None:
    pool = await get_pool()
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT * FROM users WHERE user_id = $1", user_id)
    return dict(row) if row else None


async def upsert_user(
    user_id: int,
    name: str,
    lat: float,
    lon: float,
    notify_hour: int,
    lang: str,
) -> None:
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO users (user_id, name, lat, lon, notify_hour, lang)
            VALUES ($1, $2, $3, $4, $5, $6)
            ON CONFLICT (user_id) DO UPDATE SET
                name        = EXCLUDED.name,
                lat         = EXCLUDED.lat,
                lon         = EXCLUDED.lon,
                notify_hour = EXCLUDED.notify_hour,
                lang        = EXCLUDED.lang
        """, user_id, name, lat, lon, notify_hour, lang)


async def update_notify_hour(user_id: int, hour: int) -> None:
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "UPDATE users SET notify_hour = $1 WHERE user_id = $2", hour, user_id
        )


async def update_lang(user_id: int, lang: str) -> None:
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            "UPDATE users SET lang = $1 WHERE user_id = $2", lang, user_id
        )


async def get_all_users() -> list[dict[str, Any]]:
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM users")
    return [dict(r) for r in rows]
