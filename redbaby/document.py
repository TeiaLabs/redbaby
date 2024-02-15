from datetime import datetime, timezone
from typing import Any, Optional

from bson import ObjectId
from pydantic import BaseModel, Field
from pymongo import IndexModel
from pymongo.collection import Collection

from .database import DB
from .utils import PyObjectId


class Document(BaseModel):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))

    def bson(self) -> dict[str, Any]:
        obj = self.model_dump(by_alias=True)
        if self.model_fields["_id"].default_factory is PyObjectId:
            obj["_id"] = ObjectId(obj["_id"])
        return obj

    @classmethod
    def collection_name(cls) -> str:
        raise NotImplementedError

    @classmethod
    def collection(
        cls, db_name: Optional[str] = None, suffix: Optional[str] = None
    ) -> Collection:
        return DB.get(db_name, suffix)[cls.collection_name()]

    @classmethod
    def indexes(cls) -> list[IndexModel]:
        return []
