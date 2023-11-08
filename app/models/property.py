from pydantic import BaseModel, Field
from bson import ObjectId
from app.models.py_object_id import PyObjectId


class Property(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    address: str
    price: float
    code_internal: str
    year: int
    id_owner: PyObjectId

    class Config:
        allow_population_by_field_name = True
        json_encoders = {PyObjectId: str}
