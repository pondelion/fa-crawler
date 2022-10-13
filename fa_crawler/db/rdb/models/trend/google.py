from sqlalchemy import BigInteger, Column, DateTime, Text
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class GoogleTrendModel(Base):  # type: ignore
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    datetime = Column(DateTime, nullable=False)
    keyword = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=current_timestamp())
