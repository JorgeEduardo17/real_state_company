"""
This file is the main entry point for the FastAPI application.
It configures the application, including routes, startup and shutdown events, and logging settings.
"""
from fastapi import FastAPI

from app.api.api_v1.endpoints import property
from app.core.config import settings
from app.core.logger import setup_logging
from app.db.mongodb import close_mongo_connection, connect_to_mongo

app = FastAPI(title=settings.PROJECT_NAME)  # Create a FastAPI instance for the application.

app.include_router(property.router, prefix="/api/v1/property", tags=["property"])   # All routes related to 'property' will be available under the prefix '/api/v1/property'.

setup_logging()     # Setup of logging module


@app.on_event("startup")
def startup_db_client():
    """
    Startup event that is triggered when the FastAPI application starts.
    Establishes the connection to the MongoDB database.
    :return:
    """
    connect_to_mongo()


@app.on_event("shutdown")
def shutdown_db_client():
    """
    Shutdown event that is triggered when the FastAPI application is shutting down.
    Closes the connection to the MongoDB database.
    :return:
    """
    close_mongo_connection()
