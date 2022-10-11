from datetime import date
from typing import List, Optional

from sqlalchemy import Date, cast
from sqlalchemy.orm import Session

from ....db.rdb.models.news.google_news import GoogleNewsModel
from ....schema.news.google import GoogleNewsCreateSchema
from ..base import BaseRDBRepository


class GoogleNewsRDBRepository(BaseRDBRepository[GoogleNewsModel, GoogleNewsCreateSchema, GoogleNewsCreateSchema]):

    def __init__(self):
        super().__init__(GoogleNewsModel)

    def get_by_date(self, db: Session, *, date: date) -> Optional[List[GoogleNewsModel]]:
        return db.query(self._model).filter(cast(self._model.published, Date) == date).all()

    def get_by_daterange(
        self, db: Session, *, start_date: date, end_date: date
    ) -> Optional[List[GoogleNewsModel]]:
        return db.query(self._model).filter(
            cast(self._model.published, Date) >= start_date,
            cast(self._model.published, Date) <= end_date,
        ).all()
