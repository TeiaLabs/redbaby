from typing import TypedDict


class MongoConnection(TypedDict):
    db_name: str
    uri: str


class Settings:
    connections: dict[str, MongoConnection] = {}

    @classmethod
    def setup(
        cls,
        db_name: str,
        uri: str = "mongodb://localhost:27017",
        alias: str = "default",
    ):
        cls.connections[alias] = MongoConnection(db_name=db_name, uri=uri)

    @classmethod
    def get(cls, alias: str = "default") -> MongoConnection:
        return cls.connections[alias]
