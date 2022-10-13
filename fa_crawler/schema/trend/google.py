from datetime import datetime

from pydantic import BaseModel


class GoogleTrendSchema(BaseModel):
    datetime: datetime
    keyword: str


class GoogleTrendInDBSchema(GoogleTrendSchema):
    id: int
    created_at: datetime


class GoogleTrendCreateSchema(GoogleTrendSchema):
    pass
