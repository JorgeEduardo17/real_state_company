from pydantic import BaseModel, Field
from app.models.py_object_id import PyObjectId  # Importamos la clase PyObjectId


class PropertyImageCreate(BaseModel):
    id_property: PyObjectId
    file: str
    enable: bool


class PropertyImageInDB(PropertyImageCreate):
    id: PyObjectId = Field(alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            PyObjectId: str  # Asegura que los ObjectId se conviertan a cadena
        }
