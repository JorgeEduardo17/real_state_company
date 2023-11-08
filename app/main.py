from fastapi import FastAPI
from app.api.api_v1.endpoints import property
from app.core import config
from app.db.mongodb import close_mongo_connection, connect_to_mongo

app = FastAPI(title=config.PROJECT_NAME)

app.include_router(property.router, prefix="/api/v1/property", tags=["property"])


@app.on_event("startup")
def startup_db_client():
     connect_to_mongo()

@app.on_event("shutdown")
def shutdown_db_client():
    close_mongo_connection()