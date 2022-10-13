from fa_crawler.crawler.trend import GoogleTrendsCrawler


class TestGoogleTrendsCrawler:

    def test_crawl(self):
        trc = GoogleTrendsCrawler()
        results, params = trc.run()
        print(results)
