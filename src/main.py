from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.infra.config import Config
from src.infra.database.adapter import create_engine, create_session_factory
from src.presentation.bot import onboarding_handlers
from src.presentation.bot.middleware import AppMiddleware


async def _run() -> None:
    logging.basicConfig(level=logging.INFO)
    config = Config.get_config()
    engine = create_engine(config.db_uri)
    session_factory = create_session_factory(engine)
    try:
        bot = Bot(config.telegram_bot_token)
        dp = Dispatcher(storage=MemoryStorage())
        dp.update.middleware(AppMiddleware(session_factory))
        dp.include_router(onboarding_handlers.router)
        await dp.start_polling(bot)
    finally:
        await engine.dispose()


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
