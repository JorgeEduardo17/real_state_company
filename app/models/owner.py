from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from bson import ObjectId
from app.models.py_object_id import PyObjectId


class Owner(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    address: str
    photo: Optional[str]
    birthday: date

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
