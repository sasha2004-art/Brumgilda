from __future__ import annotations

from typing import Protocol
from uuid import UUID

from src.domain.directions.entities import Direction


class IDirectionRepository(Protocol):
    async def list_roots(self) -> list[Direction]: ...

    async def list_children(self, parent_id: UUID) -> list[Direction]: ...

    async def get_by_id(self, direction_id: UUID) -> Direction | None: ...
