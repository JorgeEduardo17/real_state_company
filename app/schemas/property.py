from pydantic import BaseModel, Field
from app.models.py_object_id import PyObjectId  # Importamos la clase PyObjectId


class PropertyCreate(BaseModel):
    name: str
    address: str
    price: float
    code_internal: str
    year: int
    id_owner: str


class PropertyInDB(PropertyCreate):
    id: PyObjectId = Field(alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            PyObjectId: str  # Asegura que los ObjectId se conviertan a cadena
        }


class PropertyUpdate(BaseModel):
    price: float = Field(..., gt=0, description="El nuevo precio de la propiedad.")
