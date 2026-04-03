from __future__ import annotations

from enum import StrEnum


class IdentityProvider(StrEnum):
    TELEGRAM = "telegram"
    EMAIL = "email"


class UserStatus(StrEnum):
    SCHOOL = "school"
    STUDENT = "student"
    MASTER = "master"
    NOT_STUDYING = "not_studying"


class TeamSeekingMode(StrEnum):
    LOOKING_FOR_TEAM = "looking_for_team"
    LOOKING_FOR_PEOPLE = "looking_for_people"
