import scrapy
from scrapy_selenium import SeleniumRequest

class   WelcomeToTheJungle(scrapy.Spider):
    name = "WelcomeToTheJungle"

    start_urls= [
        "https://www.welcometothejungle.com/fr/jobs"
    ]

    def parse(self, response):
        for link in response.xpath("//ul[@class='ais-Hits-list']/li/article/a"):
            yield {
                'link': link.xpath(".//@href").get()
            }
        next_page = response.xpath("//li[@class='ais-Pagination-item ais-Pagination-item--nextPage'/a/@href]").get()
        if next_page is not None:
            print("NEXT PAGE")
            next_page_link = response.urljoin(next_page)
            yield SeleniumRequest(url=next_page_link, callback=self.parse)