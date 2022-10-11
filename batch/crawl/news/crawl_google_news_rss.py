import time

import schedule
from fa_crawler.crawler.news.google import (KeywordRSSCrawler, Topic,
                                            TopicRSSCrawler)
from fa_crawler.db.rdb.session import session
from fa_crawler.repository.rdb.news import GoogleNewsRDBRepository
from fa_crawler.utils.logger import Logger

TAG = 'google_news_crawl'
news_rdb_repo = GoogleNewsRDBRepository()


class RDBStoreCallback(TopicRSSCrawler.Callback):

    def on_finished(self, data, params):
        Logger.d(TAG, f'on_finished : {params["topic"]}')

        Logger.d(TAG, '=' * 100)
        Logger.d(TAG, f'start saving data to rdb, len(data) : {len(data)}')
        news_rdb_repo.create_all(session, data_list=data, ignore_existing_ids=True)
        Logger.d(TAG, 'done')

    def on_failed(self, e, params):
        Logger.e(TAG, f'on_failed : {params["topic"]} : {e}')
        Logger.e(TAG, '=' * 100)


def main():

    topics = (
        Topic.BUSSINESS,
        Topic.POLICTICS,
        Topic.WORLD,
        Topic.NATION,
        Topic.TECHNOLOGY,
        Topic.SPORTS,
        Topic.ENTERTAINMENT,
    )

    def job():
        for topic in topics:
            trc = TopicRSSCrawler()
            trc.run(callback=RDBStoreCallback(), topic=topic)
            time.sleep(30)

    schedule.every(30).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
