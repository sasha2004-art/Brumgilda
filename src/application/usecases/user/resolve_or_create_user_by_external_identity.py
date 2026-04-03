from __future__ import annotations

from uuid import UUID

from src.domain.user.enums import IdentityProvider
from src.domain.user.repositories import IUserIdentityRepository, IUserRepository
from src.domain.user.user import User


class ResolveOrCreateUserByExternalIdentity:
    def __init__(
        self,
        users: IUserRepository,
        identities: IUserIdentityRepository,
    ) -> None:
        self._users = users
        self._identities = identities

    async def execute(self, provider: IdentityProvider, subject_id: str) -> UUID:
        existing = await self._identities.find_user_id_by_identity(provider, subject_id)
        if existing is not None:
            return existing
        user = User.create_new()
        await self._users.save(user)
        await self._identities.link_identity(user.id, provider, subject_id)
        return user.id
