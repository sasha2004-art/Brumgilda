from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Config:
    db_uri: str
    telegram_bot_token: str

    @classmethod
    def get_config(cls) -> Config:
        try:
            return cls(
                db_uri=os.environ["DB_URI"],
                telegram_bot_token=os.environ["TELEGRAM_BOT_TOKEN"],
            )
        except KeyError as e:
            raise ValueError(f"Missing environment variable: {e.args[0]}") from e
