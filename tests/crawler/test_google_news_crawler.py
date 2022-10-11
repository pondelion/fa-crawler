from fa_crawler.crawler.news.google import (KeywordRSSCrawler, Topic,
                                            TopicRSSCrawler)


class TestGoogleNewsCrawler:

    def test_topic_rss_crawler(self):
        topics = (
            Topic.BUSSINESS,
            # Topic.POLICTICS,
            # Topic.WORLD,
            # Topic.NATION,
            # Topic.TECHNOLOGY,
            # Topic.SPORTS,
            # Topic.ENTERTAINMENT,
        )
        trc = TopicRSSCrawler()
        for topic in topics:
            trc = TopicRSSCrawler()
            results, params = trc.run(topic=topic)
            print(f'{params} : len={len(results)}')
            print(results[0])
