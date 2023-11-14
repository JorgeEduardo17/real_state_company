from pydantic import BaseModel
from typing import Optional
from datetime import date


class OwnerCreate(BaseModel):
    name: str
    address: str
    photo: Optional[str]
    birthday: date


class OwnerInDB(BaseModel):
    id: str
    name: str
    address: str
    photo: Optional[str]
    birthday: date

    class Config:
        orm_mode = True