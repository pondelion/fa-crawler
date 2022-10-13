import time
import traceback

import schedule
from fa_crawler.crawler.trend import GoogleTrendsCrawler
from fa_crawler.db.rdb.session import session
from fa_crawler.repository.rdb.trend import GoogleTrendRDBRepository
from fa_crawler.utils.logger import Logger

TAG = 'google_trend_crawl'
google_trend_rdb_repo = GoogleTrendRDBRepository()


class RDBStoreCallback(GoogleTrendsCrawler.Callback):

    def on_finished(self, data, params):
        Logger.d(TAG, f'on_finished : {params}')

        Logger.d(TAG, '=' * 100)
        Logger.d(TAG, f'start saving data to rdb, len(data) : {len(data)}')
        try:
            google_trend_rdb_repo.create_all(session, data_list=data)
            Logger.d(TAG, 'done')
        except Exception as e:
            Logger.e(TAG, f'failed to save rdb : {e} : {traceback.format_exc()}')

    def on_failed(self, e, params):
        Logger.e(TAG, f'on_failed : {params} : {e}')
        Logger.e(TAG, '=' * 100)


def main():

    def job():
        gtc = GoogleTrendsCrawler()
        gtc.run(callback=RDBStoreCallback())

    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
