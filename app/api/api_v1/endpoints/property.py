import os
from shutil import copyfileobj
from uuid import uuid4
from typing import Any
from pymongo import MongoClient

from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Body
from app.schemas import PropertyCreate, PropertyUpdate, PropertyInDB, PropertyImageInDB, PropertyImageCreate
from app.api.api_v1.deps import get_db
from app.repositories.property import PropertyRepository
from app.repositories.property_image import PropertyImageRepository

router = APIRouter()

IMAGES_DIRECTORY = "app/images/"  # Ruta en el contenedor

# Dependencia para obtener la instancia de la base de datos
def get_property_repository(db: MongoClient = Depends(get_db)) -> PropertyRepository:
    return PropertyRepository(db)


def get_property_image_repository(db: MongoClient = Depends(get_db)) -> PropertyImageRepository:
    return PropertyImageRepository(db)


@router.post("/create-property/", response_model=PropertyInDB)
def create_property_building(
        *,
        property_repo: PropertyRepository = Depends(get_property_repository),
        property_in: PropertyCreate,
) -> Any:
    """
    Create new property building.
    """
    property = property_repo.create(property_in)
    return property


@router.put("/change-price/{property_id}", response_model=PropertyInDB)
def change_price(
        *,
        property_repo: PropertyRepository = Depends(get_property_repository),
        property_id: str,
        price_in: float,
) -> Any:
    """
    Update the price of a property.
    """
    # Obtener la propiedad existente
    property = property_repo.get(property_id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    # Crear el esquema de actualización con el nuevo precio
    property_in = PropertyUpdate(price=price_in)
    property = property_repo.update(property_id, property_in)
    return property


@router.post("/properties/{property_id}/upload-image/", response_model=PropertyImageInDB)
def upload_image_to_property(
    property_id: str,
    image: UploadFile = File(...),
    property_repo: PropertyRepository = Depends(get_property_repository),
    property_image_repo: PropertyImageRepository = Depends(get_property_image_repository),
) -> Any:
    """
    Add an image to a property.
    """
    property = property_repo.get(property_id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    # Generar un nombre de archivo único para evitar conflictos y sobrescrituras
    file_name = f"{uuid4()}-{image.filename.replace(' ', '_')}"
    file_path = os.path.join(IMAGES_DIRECTORY, file_name)  # Asegúrate de que este directorio esté presente y sea accesible

    # Guardar la imagen en el sistema de archivos
    with open(file_path, "wb") as buffer:
        copyfileobj(image.file, buffer)

    img = property_image_repo.add_property_image(property_id, file_path, True)
    return img

