from typing import Optional

from bson.objectid import ObjectId as BsonObjectId
from pymongo import MongoClient
from pymongo.database import Database

from .settings import Settings


class DB:
    client = MongoClient(Settings.get()["uri"], fsync=True)

    @classmethod
    def get(
        cls, db_name: Optional[str] = None, suffix: Optional[str] = None
    ) -> Database:
        if db_name is None:
            db_name = Settings.get()["uri"]
        if suffix:
            db_name = f"{db_name}-{suffix}"
        return cls.client[db_name]

    @classmethod
    def get_client(cls, url: Optional[str] = None) -> MongoClient:
        if url:
            return MongoClient(url)
        return cls.client
