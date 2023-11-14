from pymongo import MongoClient
from app.models.property_trace import PropertyTrace
from app.schemas.property_trace import PropertyTraceCreate


class PropertyTraceRepository:
    def __init__(self, client: MongoClient):
        self.collection = client.realStateCompany.Property_traces

    def create(self, property_trace: PropertyTraceCreate) -> PropertyTrace:
        property_trace_id = self.collection.insert_one(property_trace.dict()).inserted_id
        property_trace_db = self.collection.find_one({"_id": property_trace_id})
        return PropertyTrace(**property_trace_db)
