import scrapy

class   WelcomeToTheJungle(scrapy.Spider):
    name = "WelcomeToTheJungle"

    start_urls= [
        "https://www.welcometothejungle.com/fr/jobs"
    ]

    def parse(self, response):
        for link in response.xpath("//ul[@class='ais-Hits-list']/li/article/a"):
            # link = link.xpath(".//@href")
            # yield scrapy.Request(link, callback=self.parse_offer)
            yield {
                'link': link.xpath(".//@href").get()
            }
        next_page = response.xpath("//li[@class='ais-Pagination-item ais-Pagination-item--nextPage']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_offer(self, response):
        for link in response.xpath("//ul[@class='ais-Hits-list']/li/article/a"):
            link = link.xpath(".//@href")
            yield {
                'link': link.xpath(".//@href").get()
            }
