import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde un archivo .env

PROJECT_NAME = "Real State Company API"
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", 27017))

