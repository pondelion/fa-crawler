from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from ...settings import settings
from .db import init_rdb

engine = create_engine(
    settings.DEFAULT_RDB_URI,
    convert_unicode=True,
    pool_pre_ping=True
)

Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
# Base.query = Session.query_property()

session = Session()
init_rdb(engine=engine)
print(engine.table_names())
