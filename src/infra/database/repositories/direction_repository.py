from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.directions.entities import Direction
from src.infra.database.models import DirectionModel


class SqlAlchemyDirectionRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_roots(self) -> list[Direction]:
        result = await self._session.execute(
            select(DirectionModel)
            .where(DirectionModel.parent_id.is_(None))
            .order_by(DirectionModel.sort_order)
        )
        return [_direction_to_entity(r) for r in result.scalars()]

    async def list_children(self, parent_id: UUID) -> list[Direction]:
        result = await self._session.execute(
            select(DirectionModel)
            .where(DirectionModel.parent_id == parent_id)
            .order_by(DirectionModel.sort_order)
        )
        return [_direction_to_entity(r) for r in result.scalars()]

    async def get_by_id(self, direction_id: UUID) -> Direction | None:
        row = await self._session.get(DirectionModel, direction_id)
        if row is None:
            return None
        return _direction_to_entity(row)


def _direction_to_entity(row: DirectionModel) -> Direction:
    return Direction(
        id=row.id,
        parent_id=row.parent_id,
        name=row.name,
        sort_order=row.sort_order,
        is_other=row.is_other,
    )
