from __future__ import annotations

from uuid import UUID

from src.domain.user.repositories import IUserRepository
from src.domain.user.user import User


class GetUser:
    def __init__(self, users: IUserRepository) -> None:
        self._users = users

    async def execute(self, user_id: UUID) -> User | None:
        return await self._users.get_by_id(user_id)
