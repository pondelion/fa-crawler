from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    @declared_attr
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}'.replace('model', '')
