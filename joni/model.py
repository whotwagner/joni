from typing import (
    List,
    Optional
)

from pydantic import BaseModel,Field

class Track(BaseModel):
    id: str
    description: Optional[str]
    volume: Optional[int]
    play: List[str]
    class Config:
        validate_all = True
        validate_assignment = True
        extra = 'forbid'

class ConfigModel(BaseModel):
    mpdport: Optional[int] = 6600
    mpdhost: Optional[str] = 'localhost'
    volume: Optional[int] = 60
    timeout: Optional[int] = 20
    tracks: List[Track]
    class Config:
        validate_all = True
        validate_assignment = True
        extra = 'forbid'
