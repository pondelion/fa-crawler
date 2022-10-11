from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Text
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class CompanyAnnouncementModel(Base):
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    company_code = Column(BigInteger, ForeignKey("company.code"), nullable=False)
    pubdate = Column(DateTime, nullable=False)
    title = Column(Text, nullable=False)
    markets_string = Column(Text, nullable=False)
    document_url = Column(Text, nullable=False)
    url_xbrl = Column(Text, nullable=True)
    url_report_type_summary = Column(Text, nullable=True)
    update_history = Column(Text, nullable=True)
    url_report_type_earnings_forecast = Column(Text, nullable=True)
    created_at = Column(
        DateTime,
        server_default=current_timestamp()
    )
    # updated_at = Column(
    #     DateTime,
    #     server_default=current_timestamp(),
    #     onupdate=current_timestamp()
    # )
    # company = relationship("CompanyModel", back_populates="companyannouncement")
