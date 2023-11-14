import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()  # Carga las variables de entorno desde un archivo .env


class Settings(BaseModel):
    """
        Configurations for the Real_State_Company_API application.

        This class uses Pydantic to define and validate the configurations required for the application.
        The configurations are loaded primarily from environment variables, with default values
        provided for some parameters.

        Attributes:
            ENVIRONMENT (str): Environment in which the application runs (e.g., 'development', 'production').
            PROJECT_NAME (str): Project or application name.
            DATABASE_URL (str): Connection URL to the main MongoDB database.
            DATABASE_TEST_URL (str): Connection URL to the MongoDB test database.
            DATABASE_PORT (int): Port for the database connection.
            LOG_LEVEL (str): Log level for the application log output.
            IMAGES_DIRECTORY (str): Directory for storing loaded images.
            MAX_FILE_SIZE_MG (int): Maximum file size allowed for uploads.
            EXTENTIONS_FILE_LIST (list): List of file extensions allowed for uploads.
    """

    # Project
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PROJECT_NAME: str = os.getenv("APP_NAME", "Real_State_Company_API")

    # DataBase
    DATABASE_URL: str = os.getenv("MONGODB_URI", "mongodb://db:27017/realStateCompany")
    DATABASE_TEST_URL: str = os.getenv("MONGODB_TEST_URI") if os.getenv("ENVIRONMENT") == "test" else os.getenv("MONGODB_URI")
    DATABASE_PORT = int(os.getenv("DATABASE_PORT", 27017))

    # General
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    IMAGES_DIRECTORY: str = os.getenv("IMAGES_DIRECTORY", "app/images/")
    MAX_FILE_SIZE_MG: int = 5
    EXTENTIONS_FILE_LIST: list = ["jpg", "jpeg", "png", "gif"]


# Instancia de la configuración
settings = Settings()

