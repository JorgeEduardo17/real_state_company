from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.DATABASE_URL, settings.DATABASE_PORT) # Establish the connection to the MongoDB server using configurations.
db = client.realStateCompany  # Cambia 'realStateCompany' al nombre de tu base de datos


def connect_to_mongo():
    """
    Establishes the connection to the MongoDB database.

    This method can be used to handle initial connection logic
    with MongoDB, such as setting up specific connection parameters or performing initial operations
    performing initial operations required right after the connection is established.

    Note: Currently, this method does not implement any specific logic.
    """
    pass


def close_mongo_connection():
    """
    Closes the connection to the MongoDB database.

    This method closes the connection to MongoDB. It is important to call this method
    to free resources when the application stops or no longer needs to maintain the connection to the database.
    the connection to the database.
    """
    client.close()
