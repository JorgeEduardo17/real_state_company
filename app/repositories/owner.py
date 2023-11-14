from pymongo import MongoClient
from app.models.owner import Owner
from app.schemas.owner import OwnerCreate


class OwnerRepository:
    def __init__(self, client: MongoClient):
        self.collection = client.realStateCompany.Owners

    def create(self, owner: OwnerCreate) -> Owner:
        owner_id = self.collection.insert_one(owner.dict()).inserted_id
        owner_db = self.collection.find_one({"_id": owner_id})
        return Owner(**owner_db)
