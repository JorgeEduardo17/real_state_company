from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import date
from app.models.py_object_id import PyObjectId


class PropertyTrace(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    date_sale: date
    name: str
    value: float
    tax: float
    id_property: PyObjectId

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

