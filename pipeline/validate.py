from pydantic import BaseModel, ValidationError
from typing import Optional


class MatchMetadata(BaseModel):
    season: Optional[str]
    city: Optional[str]
    venue: Optional[str]
    dates: list
    teams: list


class MatchOutcome(BaseModel):
    winner: Optional[str]


class MatchInfo(BaseModel):
    match_type: str
    teams: list
    dates: list
    venue: Optional[str] = None
    city: Optional[str] = None
    season: Optional[str] = None
    outcome: Optional[dict] = None