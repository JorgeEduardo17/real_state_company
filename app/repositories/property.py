from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import ReturnDocument

from app.schemas.property import PropertyCreate, PropertyInDB
from app.models.py_object_id import PyObjectId


class PropertyRepository:
    """
    Repository to handle database operations for real estate properties.

    This class provides methods to create, get and update real estate properties in a MongoDB database.
    It uses the Pydantic schema for data validation and serialization, and handles the conversion of MongoDB ObjectId
    to PyObjectId for use in Pydantic.

    Attributes:
        Collection (MongoClient): MongoDB client for interacting with the database.

    Methods:
        create(property: PropertyCreate) -> PropertyInDB:
            Creates a new property in the database.

        get(property_id: str) -> PropertyInDB:
            Retrieves a property by its ID.

        update(property_id: str, property_update: PropertyCreate) -> PropertyInDB:
            Updates an existing property.
    """
    def __init__(self, client: MongoClient):
        self.collection = client.realStateCompany.Properties

    def create(self, property: PropertyCreate) -> PropertyInDB:
        """
        Creates a new property in the database.

        Args:
            property (PropertyCreate): Data of the property to create.

        Returns:
            PropertyInDB: The property created with its generated ID.
        """
        property_data = property.dict(by_alias=True)
        result = self.collection.insert_one(property_data)
        property_data['_id'] = PyObjectId(result.inserted_id)
        return PropertyInDB(**property_data)

    def get(self, property_id: str) -> PropertyInDB:
        """
        Retrieves a property by its ID.

        Args:
            property_id (str): ID of the property to retrieve.

        Returns:
            PropertyInDB: The retrieved property.

        Raises:
            ValueError: If no property with the provided ID is found.
        """
        property_db = self.collection.find_one({"_id": ObjectId(property_id)})
        if property_db:
            # Convertimos el _id de ObjectId a PyObjectId
            property_db["id"] = PyObjectId(property_db["_id"])
            del property_db["_id"]  # Eliminar _id ya que no se necesita más
            return PropertyInDB(**property_db)
        else:
            raise ValueError(f"No property found with ID: {property_id}")

    def update(self, property_id: str, property_update: PropertyCreate) -> PropertyInDB:
        """
        Updates an existing property.

        Args:
            property_id (str): ID of the property to update.
            property_update (PropertyCreate): Updated property data.

        Returns:
            PropertyInDB: The updated property.

        Raises:
            ValueError: If no property with the provided ID is found.
        """
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




