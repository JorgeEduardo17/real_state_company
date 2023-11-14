from pydantic import BaseModel, Field
from app.models.py_object_id import PyObjectId  # Importamos la clase PyObjectId


class PropertyCreate(BaseModel):
    """
    Schema for the creation of a real estate property.

    This Pydantic schema defines the fields required to create a new real estate property.
    It is used to validate and serialize the input data when creating a new property.

    Attributes:
        name (str): Name of the property.
        address (str): Property address.
        price (float): Property price.
        code_internal (str): Internal code assigned to the property.
        year (int): Year of construction of the property.
        id_owner (str): Identification of the owner of the property.
    """
    name: str
    address: str
    price: float
    code_internal: str
    year: int
    id_owner: str


class PropertyInDB(PropertyCreate):
    """
    Schema to represent a real estate property in the database.

    Extends the PropertyCreate schema by adding a unique identifier for the property.
    It uses the PyObjectId type for the ID, which is converted to string for correct serialization in formats such as JSON.
    serialization in formats such as JSON.

    Attributes:
        id (PyObjectId): unique identifier of the property in the database.
    """
    id: PyObjectId = Field(alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            PyObjectId: str  # Asegura que los ObjectId se conviertan a cadena
        }


class PropertyUpdate(BaseModel):
    """
    Schema to update the price of an existing real estate property.

    This schema defines a field to update the price of a property.
    The price must be a positive value.

    Attributes:
        price (float): New price of the property. Must be greater than 0.
    """
    price: float = Field(..., gt=0, description="El nuevo precio de la propiedad.")
