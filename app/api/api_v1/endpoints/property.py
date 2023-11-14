import logging
from typing import Any

from fastapi import APIRouter, Depends, UploadFile, File
from pymongo import MongoClient

from app.api.api_v1.deps import get_db
from app.core.exceptions import handle_db_error
from app.repositories.property import PropertyRepository
from app.repositories.property_image import PropertyImageRepository
from app.schemas import PropertyCreate, PropertyInDB, PropertyImageInDB
from app.services.property_service import PropertyService

router = APIRouter()

logger = logging.getLogger(__name__)


# Dependencia para obtener la instancia de la base de datos
def get_property_repository(db: MongoClient = Depends(get_db)) -> PropertyRepository:
    return PropertyRepository(db)


def get_property_image_repository(db: MongoClient = Depends(get_db)) -> PropertyImageRepository:
    return PropertyImageRepository(db)


def get_property_service(
    property_repo: PropertyRepository = Depends(get_property_repository),
    property_image_repo: PropertyImageRepository = Depends(get_property_image_repository)
) -> PropertyService:
    return PropertyService(property_repo, property_image_repo)


@router.post("/create-property/", response_model=PropertyInDB)
async def create_property_building(
        *,
        property_data: PropertyCreate,
        property_service: PropertyService = Depends(get_property_service)
) -> Any:
    """
    Creates a new real estate property.

    Uses the information provided in `property_data` to create a new property record in the database. Returns the
    details of the created property.

    Args:
        property_service (PropertyService): servicio for property logic.
        property_data (PropertyCreate): Input data for property creation.

    Returns:
        PropertyInDB: An object representing the created property.

    Example:
        POST /create-property/
            {
              "name": "property_name_1",
              "address": "carrera 1",
              "price": 1000,
              "code_internal": "001",
              "year": 1,
              "id_owner": "JOED1"
            }

    """
    logger.info(f"Creating a new property with data {property_data}")
    try:
        property_created = property_service.create_property(property_data)
        logger.info(f"Property created successfully with id {str(property_created['id'])}")
        return property_created
    except Exception as e:
        logger.error(f"Error creating property: {e}")
        handle_db_error(e)


@router.put("/change-price/{property_id}", response_model=PropertyInDB)
async def change_price(
        *,
        property_id: str,
        price_in: float,
        property_service: PropertyService = Depends(get_property_service)
) -> Any:
    """
    Update the price of an existing property.

    This endpoint allows you to change the price of a specific property, identified by its ID.
    by its ID. If the property is not found, it returns a 404 error.

    Args:
        property_id (str): The ID of the property to update.
        price_in (float): The new price of the property.
        property_service (PropertyService): property service for interaction with the database.


    Returns:
        PropertyInDB: Object representing the property with the updated price.

    Example:
        PUT /change-price/12345
        body: {
            "price": 35000
        }

    """
    logger.info(f"Updating price for property {property_id}")
    try:
        property_updated = property_service.update_property_price(property_id, price_in)
        logger.info(f"Price updated successfully for property {property_id}")
        return property_updated
    except Exception as e:
        logger.error(f"Error updating property price: {e}")
        handle_db_error(e)


@router.post("/properties/{property_id}/upload-image/", response_model=PropertyImageInDB)
async def upload_image_to_property(
        property_id: str,
        image: UploadFile = File(...),
        property_service: PropertyService = Depends(get_property_service)
) -> Any:
    """
    Adds an image to an existing property.

    This endpoint allows to upload and associate an image to a specific property. The image is
    saved in the file system and its path is registered in the database. If the
    property does not exist, it returns a 404 error.

    Args:
        property_id (str): The ID of the property to which the image will be added.
        image (UploadFile): The image to upload.
        property_service (PropertyService): Property service for the interaction with the database.

    Returns:
        PropertyImageInDB: Object representing the image associated to the property.

    Example:
        POST /properties/12345/upload-image/
        body: (multipart/form-data with the image file)

    """
    logger.info(f"Uploading image to property {property_id}")
    try:
        property_img = property_service.upload_image_to_property(property_id, image)
        logger.info(f"Image uploaded successfully for property {property_id}")
        return property_img
    except Exception as e:
        logger.error(f"Error uploading image to property {property_id}: {e}")
        handle_db_error(e)
