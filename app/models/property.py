from pydantic import BaseModel, Field
from bson import ObjectId
from app.models.py_object_id import PyObjectId


class Property(BaseModel):
    """
    Pydantic model to represent a real estate property.

    This model defines the structure of the data for a real estate property, including
    identification, name, address, price, internal code, year of construction and owner identification.
    of the owner. It uses PyObjectId to handle MongoDB ObjectId's in a Pydantic-compliant way.

    Attributes:
        id (PyObjectId): unique identifier of the property (MongoDB ObjectId).
        name (str): Property name.
        address (str): Property address.
        price (float): Price of the property.
        code_internal (str): Internal code assigned to the property.
        year (int): Year of construction of the property.
        id_owner (PyObjectId): Property owner identifier.
    """
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
