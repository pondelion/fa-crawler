from sqlalchemy_utils import create_database, database_exists, drop_database

from ...settings import settings
from ...utils.logger import Logger
from .models.base import Base
from .models.company import CompanyModel, SectorModel
from .models.financial import YFFinancialModel
from .models.news import GoogleNewsModel
from .models.stock import StqDailyStockpriceModel, YFDailyStockpriceModel


def delete_database() -> None:
    if database_exists(settings.DEFAULT_RDB_URI):
        Logger.i('rdb', f'Deleting database : {settings.DEFAULT_RDB_URI}')
        drop_database(settings.DEFAULT_RDB_URI)


def create_databse() -> None:
    if not database_exists(settings.DEFAULT_RDB_URI):
        Logger.i('rdb', f'Database not found. Creating database : {settings.DEFAULT_RDB_URI}')
        create_database(settings.DEFAULT_RDB_URI)


def init_rdb(
    engine,
    recreate_database: bool = False,
    recreate_table: bool = False
) -> None:
    if recreate_database:
        delete_database()
    create_databse()
    if recreate_table:
        drop_all_tables(engine)
    Base.metadata.create_all(engine)


def show_tables(engine) -> None:
    print(engine.table_names())


def drop_all_tables(engine) -> None:
    try:
        StqDailyStockpriceModel.__table__.drop(engine)
    except Exception as e:
        print(e)
    try:
        YFDailyStockpriceModel.__table__.drop(engine)
    except Exception as e:
        print(e)
    try:
        CompanyModel.__table__.drop(engine)
    except Exception as e:
        print(e)
    try:
        SectorModel.__table__.drop(engine)
    except Exception as e:
        print(e)
    try:
        YFFinancialModel.__table__.drop(engine)
    except Exception as e:
        print(e)
    try:
        GoogleNewsModel.__table__.drop(engine)
    except Exception as e:
        print(e)
    try:
        Base.metadata.drop_all(engine)
    except Exception as e:
        print(e)
