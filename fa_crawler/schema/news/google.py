from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class GoogleNewsSchema(BaseModel):
    id: str
    published: datetime
    title: str
    summary: str
    url: HttpUrl
    source: str
    topic: Optional[str] = None
    keyword: Optional[str] = None


class GoogleNewsInDBSchema(GoogleNewsSchema):
    created_at: datetime


class GoogleNewsCreateSchema(GoogleNewsSchema):
    pass
