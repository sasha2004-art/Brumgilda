from __future__ import annotations

from typing import Any
from uuid import UUID

from src.application.common.exceptions import UserNotFoundError
from src.domain.user.repositories import IUserRepository


class PatchOnboardingDraft:
    def __init__(self, users: IUserRepository) -> None:
        self._users = users

    async def execute(self, user_id: UUID, patch: dict[str, Any]) -> None:
        user = await self._users.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(str(user_id))
        user.merge_draft(patch)
        await self._users.save(user)
