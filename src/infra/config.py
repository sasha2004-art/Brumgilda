from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Config:
    db_uri: str

    @classmethod
    def get_config(cls) -> Config:
        try:
            return cls(db_uri=os.environ["DB_URI"])
        except KeyError:
            raise ValueError("DB_URI environment variable not set")
