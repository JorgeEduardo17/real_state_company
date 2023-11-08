from pydantic import BaseModel, Field
from bson import ObjectId
from app.models.py_object_id import PyObjectId


class PropertyImage(BaseModel):
    id: PyObjectId = Field(alias="_id")
    id_property: PyObjectId
    file: str
    enable: bool

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
