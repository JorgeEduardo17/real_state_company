from pymongo import MongoClient
from ..core.config import DATABASE_URL, DATABASE_PORT

client = MongoClient(DATABASE_URL, DATABASE_PORT)
db = client.realStateCompany  # Cambia 'mydatabase' al nombre de tu base de datos


def connect_to_mongo():
    # Código para manejar la conexión inicial si es necesario
    pass


def close_mongo_connection():
    client.close()
