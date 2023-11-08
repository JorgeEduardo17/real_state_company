from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import ReturnDocument

from app.schemas.property import PropertyCreate, PropertyInDB
from app.models.py_object_id import PyObjectId


class PropertyRepository:
    def __init__(self, client: MongoClient):
        self.collection = client.realStateCompany.Properties

    def create(self, property: PropertyCreate) -> PropertyInDB:
        property_data = property.dict(by_alias=True)
        result = self.collection.insert_one(property_data)
        property_data['_id'] = PyObjectId(result.inserted_id)
        return PropertyInDB(**property_data)

    def get(self, property_id: str) -> PropertyInDB:
        property_db = self.collection.find_one({"_id": ObjectId(property_id)})
        if property_db:
            # Convertimos el _id de ObjectId a PyObjectId
            property_db["id"] = PyObjectId(property_db["_id"])
            del property_db["_id"]  # Eliminar _id ya que no se necesita más
            return PropertyInDB(**property_db)
        else:
            raise ValueError(f"No property found with ID: {property_id}")

    def update(self, property_id: str, property_update: PropertyCreate) -> PropertyInDB:
        update_data = property_update.dict(exclude_unset=True)
        result = self.collection.find_one_and_update(
            {"_id": ObjectId(property_id)},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        if result:
            result["id"] = PyObjectId(result["_id"])
            del result["_id"]  # Eliminar _id ya que no se necesita más
            return PropertyInDB(**result)
        else:
            raise ValueError(f"No property found with ID: {property_id}")




