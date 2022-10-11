import hashlib
from datetime import datetime
from typing import Any, Dict
from urllib.parse import quote

import feedparser
from timeout_decorator import timeout

from ....schema.news.google import GoogleNewsSchema
from ...base_crawler import BaseCrawler


class KeywordRSSCrawler(BaseCrawler):

    def __init__(self):
        self._RSS_URL_FMT = 'https://news.google.com/news/rss/search/section/q/{KEYWORD}/{KEYWORD}?ned=jp&amp;hl=ja&amp;gl=JP'

    def run(
        self,
        keyword: str,
        callback: BaseCrawler.Callback = BaseCrawler.DefaultCallback(),
    ) -> Any:
        """[summary]

        Args:
            keyword (str): [description]
            callback (BaseCrawler.Callback, optional): [description]. Defaults to BaseCrawler.DefaultCallback().
        """

        kwargs = {
            'keyword': keyword
        }

        keyword_encoded = quote(keyword)

        try:
            feed = self._fetch(self._RSS_URL_FMT.format(KEYWORD=keyword_encoded))
            entries = feed.entries
        except Exception as e:
            callback.on_failed(e, kwargs)
            return None, None

        entries = [self._parse(entry, keyword) for entry in entries]
        callback.on_finished(entries, kwargs)
        return entries, kwargs

    @timeout(60)
    def _fetch(self, url):
        return feedparser.parse(url)

    def _parse(self, entry: Dict[str, Any], keyword: str) -> GoogleNewsSchema:
        return GoogleNewsSchema(
            id=hashlib.md5(entry['id'].encode()).hexdigest(),
            published=datetime(*entry['published_parsed'][:6]),
            title=entry['title'],
            summary=entry['summary'],
            url=entry['link'],
            source=entry['source']['title'],
            keyword=keyword,
        )
