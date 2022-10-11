from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class GoogleNewsModel(Base):
    id = Column(
        String(32), primary_key=True, nullable=False
    )
    published = Column(DateTime, nullable=False)
    title = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    topic = Column(Text, nullable=True)
    url = Column(Text, nullable=True)
    source = Column(Text, nullable=True)
    keyword = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=current_timestamp())
