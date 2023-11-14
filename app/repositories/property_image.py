from pymongo import MongoClient
from app.models.property_image import PropertyImage
from app.schemas.property_image import PropertyImageCreate, PropertyImageInDB
from app.models.py_object_id import PyObjectId


class PropertyImageRepository:
    def __init__(self, client: MongoClient):
        self.collection = client.realStateCompany.Property_images

    def add_property_image(self, property_id: str, image_path: str, enable: bool) -> PropertyImageInDB:

        property_image_data = {
            "id_property": PyObjectId(property_id),
            "file": image_path,
            "enable": enable
        }
        result = self.collection.insert_one(property_image_data)
        property_image_data['_id'] = PyObjectId(result.inserted_id)
        return PropertyImageInDB(**property_image_data)

