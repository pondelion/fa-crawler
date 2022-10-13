from datetime import date
from typing import List, Optional

from sqlalchemy import Date, cast
from sqlalchemy.orm import Session

from ....db.rdb.models.trend import GoogleTrendModel
from ....schema.trend import GoogleTrendCreateSchema
from ..base import BaseRDBRepository


class GoogleTrendRDBRepository(BaseRDBRepository[GoogleTrendModel, GoogleTrendCreateSchema, GoogleTrendCreateSchema]):

    def __init__(self):
        super().__init__(GoogleTrendModel)

    def get_by_date(self, db: Session, *, date: date) -> Optional[List[GoogleTrendModel]]:
        return db.query(self._model).filter(cast(self._model.datetime, Date) == date).all()

    def get_by_daterange(
        self, db: Session, *, start_date: date, end_date: date
    ) -> Optional[List[GoogleTrendModel]]:
        return db.query(self._model).filter(
            cast(self._model.datetime, Date) >= start_date,
            cast(self._model.datetime, Date) <= end_date,
        ).all()
