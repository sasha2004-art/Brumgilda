from __future__ import annotations

from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.application.usecases.user.resolve_or_create_user_by_external_identity import (
    ResolveOrCreateUserByExternalIdentity,
)
from src.domain.user.enums import IdentityProvider
from src.infra.database.adapter import session_scope
from src.infra.di import build_container


class AppMiddleware(BaseMiddleware):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with session_scope(self._session_factory) as session:
            data["session"] = session
            container = build_container(session)
            data["container"] = container

            user_id = None
            if isinstance(event, Message) and event.from_user:
                uc = container.resolve(ResolveOrCreateUserByExternalIdentity)
                user_id = await uc.execute(
                    IdentityProvider.TELEGRAM, str(event.from_user.id)
                )
            elif isinstance(event, CallbackQuery) and event.from_user:
                uc = container.resolve(ResolveOrCreateUserByExternalIdentity)
                user_id = await uc.execute(
                    IdentityProvider.TELEGRAM, str(event.from_user.id)
                )
            data["user_id"] = user_id

            return await handler(event, data)
