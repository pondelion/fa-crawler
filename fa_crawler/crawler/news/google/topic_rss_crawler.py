import hashlib
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional, Tuple

import feedparser
from timeout_decorator import timeout

from ....schema.news.google import GoogleNewsSchema
from ...base_crawler import BaseCrawler


class Topic(Enum):
    BUSSINESS = 'https://news.google.com/news/rss/headlines/section/topic/BUSINESS.ja_jp/%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9?ned=jp&hl=ja&gl=JP'
    POLICTICS = 'https://news.google.com/news/rss/headlines/section/topic/POLITICS.ja_jp/%E6%94%BF%E6%B2%BB?ned=jp&hl=ja&gl=JP'
    TECHNOLOGY = 'https://news.google.com/news/rss/headlines/section/topic/SCITECH.ja_jp/%E3%83%86%E3%82%AF%E3%83%8E%E3%83%AD%E3%82%B8%E3%83%BC?ned=jp&hl=ja&gl=JP'
    SPORTS = 'https://news.google.com/news/rss/headlines/section/topic/SPORTS.ja_jp/%E3%82%B9%E3%83%9D%E3%83%BC%E3%83%84?ned=jp&hl=ja&gl=JP'
    ENTERTAINMENT = 'https://news.google.com/news/rss/headlines/section/topic/ENTERTAINMENT.ja_jp/%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%A1?ned=jp&hl=ja&gl=JP'
    WORLD = 'https://news.google.com/news/rss/headlines/section/topic/WORLD.ja_jp/%E5%9B%BD%E9%9A%9B?ned=jp&hl=ja&gl=JP'
    NATION = 'https://news.google.com/news/rss/headlines/section/topic/NATION.ja_jp/%E5%9B%BD%E5%86%85?ned=jp&hl=ja&gl=JP'


class TopicRSSCrawler(BaseCrawler):

    def run(
        self,
        callback: BaseCrawler.Callback = BaseCrawler.DefaultCallback(),
        topic: Topic = Topic.BUSSINESS
    ) -> Tuple[Optional[Any], Optional[Dict[str, Any]]]:
        """_summary_

        Args:
            callback (BaseCrawler.Callback, optional): _description_. Defaults to BaseCrawler.DefaultCallback().
            topic (Topic, optional): _description_. Defaults to Topic.BUSSINESS.

        Raises:
            Exception: _description_

        Returns:
            Tuple[Optional[Any], Optional[Dict[str, Any]]]: _description_
        """

        kwargs = {
            'topic': str(topic).replace('Topic.', '')
        }

        try:
            feed = self._fetch(topic.value)
            entries = feed.entries
            if not self._validate_results(entries):
                raise Exception('Invalid data.')
        except Exception as e:
            callback.on_failed(e, kwargs)
            return None, None

        entries = [self._parse(entry, topic) for entry in entries]
        callback.on_finished(entries, kwargs)
        return entries, kwargs

    @timeout(60)
    def _fetch(self, url):
        return feedparser.parse(url)

    def _validate_results(self, entries) -> bool:
        return all(['published_parsed' in entry for entry in entries])

    def _parse(self, entry: Dict[str, Any], topic: Topic) -> GoogleNewsSchema:
        return GoogleNewsSchema(
            id=hashlib.md5(entry['id'].encode()).hexdigest(),
            published=datetime(*entry['published_parsed'][:6]),
            title=entry['title'],
            summary=entry['summary'],
            url=entry['link'],
            source=entry['source']['title'],
            topic=topic.name,
        )
