from sqlalchemy import BigInteger, Column, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class SectorModel(Base):
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    created_at = Column(
        DateTime,
        server_default=current_timestamp()
    )
    updated_at = Column(
        DateTime,
        server_default=current_timestamp(),
        onupdate=current_timestamp()
    )
    company = relationship("CompanyModel", back_populates="sector")
