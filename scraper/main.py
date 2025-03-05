from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from newscraper.spiders.setopati import SetopatiSpider
from newscraper.spiders.ekantipur import EkantipurSpider


def run_spider():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(SetopatiSpider)
    process.crawl(EkantipurSpider)
    process.start()


if __name__ == "__main__":
    run_spider()
