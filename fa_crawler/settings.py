import os
from enum import Enum
from typing import Optional

from pydantic import BaseSettings
from sqlalchemy.engine.url import URL


class RDBType(Enum):
    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'


class Settings(BaseSettings):

    DEFAULT_RDB_TYPE: RDBType = RDBType.MYSQL
    DEFAULT_RDB_HOST: Optional[str] = '127.0.0.1'
    DEFAULT_RDB_PORT: Optional[int] = 3306
    DEFAULT_RDB_USERNAME: str
    DEFAULT_RDB_PASSWORD: str
    DEFAULT_RDB_NAME: str

    DEFAULT_DB_RECORD_REFRESH_SECS: int = 5 * 60

    @property
    def DEFAULT_RDB_URI(self) -> URL:
        dialect_driver = self.DEFAULT_RDB_TYPE.value
        url = URL(
            dialect_driver,
            self.DEFAULT_RDB_USERNAME,
            self.DEFAULT_RDB_PASSWORD,
            self.DEFAULT_RDB_HOST,
            self.DEFAULT_RDB_PORT,
            self.DEFAULT_RDB_NAME,
            query={'charset': 'utf8'}
        )
        return url
        #return f'mysql://{self.DEFAULT_RDB_USERNAME}:{self.DEFAULT_RDB_PASSWORD}@{self.DEFAULT_RDB_HOST}:{self.DEFAULT_RDB_PORT}/{self.DEFAULT_RDB_NAME}?charset=utf8mb4'


settings = Settings(
    DEFAULT_RDB_HOST=os.environ.get('DEFAULT_RDB_HOST', '127.0.0.1'),
    DEFAULT_RDB_PORT=int(os.environ.get('DEFAULT_RDB_PORT', '3306')),
    DEFAULT_RDB_USERNAME=os.environ['DEFAULT_RDB_USER'],
    DEFAULT_RDB_PASSWORD=os.environ['DEFAULT_RDB_PASSWORD'],
    DEFAULT_RDB_NAME=os.environ['DEFAULT_RDB_NAME'],
)
