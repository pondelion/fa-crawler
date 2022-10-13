from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
from pytrends.request import TrendReq
from timeout_decorator import timeout

from ...schema.trend import GoogleTrendSchema
from ..base_crawler import BaseCrawler


class GoogleTrendsCrawler(BaseCrawler):

    def run(
        self,
        pn: str = 'japan',
        callback: BaseCrawler.Callback = BaseCrawler.DefaultCallback(),
    ) -> Tuple[Optional[Any], Optional[Dict[str, Any]]]:
        now_dt = datetime.now()
        kwargs = {
            'datetime': now_dt
        }

        try:
            trends = self._fetch(pn)
        except Exception as e:
            callback.on_failed(e, kwargs)
            return None, None

        callback.on_finished(trends, kwargs)
        return trends, kwargs

    @timeout(60)
    def _fetch(self, pn: str, hl: str = 'ja-jp') -> List[GoogleTrendSchema]:
        pytrend = TrendReq(hl=hl, tz=540)
        dt_crawl = datetime.now()
        df = pytrend.trending_searches(pn=pn)
        objs = [GoogleTrendSchema(datetime=dt_crawl, keyword=str(v[0])) for v in df.values]
        return objs
