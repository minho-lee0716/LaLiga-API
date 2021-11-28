from typing import List, Optional

from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    back_number: Optional[int] = None


class PlayerCreate(PlayerBase):
    club_id: Optional[int] = None


class Player(PlayerCreate):
    id: int

    class Config:
        orm_mode = True


class ClubBase(BaseModel):
    name: str


class ClubCreate(ClubBase):
    pass


class Club(ClubBase):
    id: int
    players: List[Player] = []

    class Config:
        orm_mode = True
