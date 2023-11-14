import os
from uuid import uuid4

from app.core.config import settings
from app.repositories.property import PropertyRepository
from app.core.validation import validate_image_upload
from app.repositories.property_image import PropertyImageRepository
from app.schemas import PropertyCreate, PropertyUpdate, PropertyInDB, PropertyImageInDB
from app.utils.file_utils import save_image


class PropertyService:
    """
    Service to manage operations related to real estate properties.

    This service facilitates the creation, update and management of images associated with real estate properties.
    It uses repositories to interact with the database and validation and usability methods to ensure data integrity and proper file management.
    data integrity and proper file management.

    Attributes:
    property_repo (PropertyRepository): repository for property related operations.
    property_image_repo (PropertyImageRepository): Repository for operations related to property images.

    Methods:
    create_property(property_data: PropertyCreate) -> PropertyInDB:
        Creates a new real estate property based on the provided data.

    update_property_price(property_id: str, new_price: float) -> PropertyInDB:
        Updates the price of an existing property.

    upload_image_to_property(property_id: str, image_file) -> PropertyImageInDB:
        Uploads and associates an image to an existing property.

    get_property_or_404(property_id: str) -> PropertyInDB:
        Gets a property by its ID or throws an exception if it is not found.
    """
    def __init__(self, property_repo: PropertyRepository, property_image_repo: PropertyImageRepository):
        self.property_repo = property_repo
        self.property_image_repo = property_image_repo

    def create_property(self, property_data: PropertyCreate) -> PropertyInDB:
        return self.property_repo.create(property_data)

    def update_property_price(self, property_id: str, new_price: float) -> PropertyInDB:
        # Validations
        property_in_db = self.get_property_or_404(property_id)
        property_data = PropertyUpdate(price=new_price)
        return self.property_repo.update(property_id, property_data)

    def upload_image_to_property(self, property_id: str, image_file) -> PropertyImageInDB:
        # Validations
        validate_image_upload(image_file)
        property_in_db = self.get_property_or_404(property_id)
        # Generate a unique file name to avoid conflicts and overwrites
        file_name = f"{uuid4()}-{image_file.filename.replace(' ', '_')}"
        file_path = os.path.join(settings.IMAGES_DIRECTORY, file_name)

        save_image(image_file, file_path)

        return self.property_image_repo.add_property_image(property_id, file_path, True)

    def get_property_or_404(self, property_id: str) -> PropertyInDB:
        property_in_db = self.property_repo.get(property_id)
        if not property_in_db:
            # Manejar la excepción como prefieras
            raise ValueError("Property not found")
        return property_in_db