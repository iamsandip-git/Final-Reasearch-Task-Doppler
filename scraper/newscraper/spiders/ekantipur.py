import scrapy
import re
import json
from datetime import datetime
from utils import DatabaseUtils
from config import ekantipur_categories


class EkantipurSpider(scrapy.Spider):
    name = "ekantipur"
    allowed_domains = ["ekantipur.com"]

    def __init__(self, *args, **kwargs):
        super(EkantipurSpider, self).__init__(*args, **kwargs)
        try:
            with open("ekantipur_news.json", "r", encoding="utf-8") as file:
                self.data_list = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            self.data_list = []
        self.db_utils = DatabaseUtils()

    def start_requests(self):
        today = datetime.now().strftime("%Y/%m/%d")
        for indv_category in ekantipur_categories:
            yield scrapy.Request(
                f"https://ekantipur.com/{indv_category}/{today}?json=true",
                callback=self.parse,
            )

    def parse(self, response):
        href_pattern = re.compile(r'<h2><a href="(.*?)">')
        # Try to parse the JSON response first
        try:
            data = json.loads(response.body)
            href_matches = href_pattern.findall(data["html"])
        except json.JSONDecodeError:
            # If the JSON parsing fails, parse the HTML response
            data = response.text
            href_matches = href_pattern.findall(data)
        for indv_href_match in href_matches:
            found = any(item["link"] == indv_href_match for item in self.data_list)
            if not found:
                yield response.follow(
                    indv_href_match,
                    callback=self.parse_news,
                    meta={
                        "link": indv_href_match,
                        "source": "ekantipur",
                    },
                )

    def parse_news(self, response):
        title = response.css("div.article-header h1::text").get()
        image_url = response.css("div.image figure img::attr(data-src)").get()
        link = response.meta["link"]
        source = response.meta["source"]

        if not link.startswith("https://ekantipur.com"):
            link = "https://ekantipur.com" + link

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
        with open("ekantipur_news.json", "w", encoding="utf-8") as json_file:
            json.dump(self.data_list, json_file, ensure_ascii=False, indent=4)
        self.db_utils.close_connection()
