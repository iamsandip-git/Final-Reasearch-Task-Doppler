import scrapy
import re
import json
from datetime import datetime
from utils import DatabaseUtils


class SetopatiSpider(scrapy.Spider):
    name = "setopati"
    allowed_domains = ["www.setopati.com"]
    start_urls = ["https://www.setopati.com"]

    def __init__(self, *args, **kwargs):
        super(SetopatiSpider, self).__init__(*args, **kwargs)

        try:
            with open("setopati_news.json", "r", encoding="utf-8") as file:
                self.data_list = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            self.data_list = []

        self.db_utils = DatabaseUtils()

    def parse(self, response):
        links = response.css("a")
        pattern = re.compile(
            r"https://www\.setopati\.com/(exclusive|banking|politics|social|kinmel|sports|nepali-brand|art|global|ghumphir|opinion|blog|cover-story)/\.*"
        )

        for indv_link in links:
            href = indv_link.css("::attr(href)").get()
            if pattern.match(href):
                found = any(item["link"] == href for item in self.data_list)
                if not found:
                    yield response.follow(
                        href,
                        callback=self.parse_news,
                        meta={"link": href, "source": "setopati"},
                    )

    def parse_news(self, response):
        title = response.css("h1.news-big-title::text").get()
        image_url = response.css("div#featured-images img::attr(src)").get()
        link = response.meta["link"]
        source = response.meta["source"]
        scraped_data = {
            "title": title,
            "image_url": image_url,
            "link": link,
            "source": source,
        }
        self.data_list.append(scraped_data)
        self.db_utils.insert_data(
            "api_news",
            {
                "title": title,
                "image_url": image_url,
                "link": link,
                "created_at": datetime.now(),
                "source": source,
            },
        )
        yield scraped_data

    def closed(self, reason):
        with open("setopati_news.json", "w", encoding="utf-8") as json_file:
            json.dump(self.data_list, json_file, ensure_ascii=False, indent=4)

        self.db_utils.close_connection()
