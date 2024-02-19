from datetime import datetime, timezone

from pydantic import Field

from .core import BaseDocument


class Timestamping(BaseDocument):
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
