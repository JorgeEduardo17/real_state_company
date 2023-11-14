from pydantic import BaseModel
from typing import Optional
from datetime import date


class PropertyTraceCreate(BaseModel):
    date_sale: date
    name: str
    value: float
    tax: float
    id_property: str


class PropertyTraceInDB(PropertyTraceCreate):
    id: str
