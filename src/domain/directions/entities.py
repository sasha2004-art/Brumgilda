from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Direction:
    id: UUID
    parent_id: UUID | None
    name: str
    sort_order: int
    is_other: bool
