import scrapy
from scrapy_splash import SplashRequest

class   intra42(scrapy.Spider):
    name = "intra42"

    start_urls= [
        "https://companies.intra.42.fr/en/offers?filter%5Bcontract_type%5D=stage&filter%5Btarget%5D=&filter%5Bexpertise_id%5D=&filter%5Bcountry%5D=&seen=&rev_sort=&search="
    ]

    def start_requests(self):
        for url in self.start_urls:
            print("coucou1")
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait': 2})

    def parse(self, response):
        for link in response.xpath("//div[@class='page-content']/div/h3/a"):
            print("coucou2")
            offer = link.xpath(".//@href").get()
            yield SplashRequest(url=offer, callback=self.parse_offer, endpoint='render.html', args={'wait': 1})
        
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            yield SplashRequest(url=next_page, callback=self.parse, endpoint='render.html', args={'wait': 1})

    def parse_offer(self, response):
        print("coucou3")
        text = response.xpath("//div[@class='show-offer']//text()").getall()
        joined_text = ''.join(text).lower()
        offer = response.xpath("//div[@class='show-left company-name']/h2//text()").get()
        if self.language.lower() in joined_text:
            yield {
               offer + " (" + self.language + ")": response.request.url,
            }