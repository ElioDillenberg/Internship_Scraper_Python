import scrapy

class   WelcomeToTheJungle(scrapy.Spider):
    name = "WelcomeToTheJungle"

    start_urls= [
        "https://www.welcometothejungle.com/fr/jobs?refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Fullstack&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Backend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Science&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Autres&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Recherche%20%2F%20R%26D&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Frontend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Engineering&page=1&configure%5Bfilters%5D=website.reference%3Awttj_fr&configure%5BhitsPerPage%5D=30&aroundLatLng=48.8546%2C2.3477&aroundQuery=Paris%2C%20France&aroundRadius=20000&aroundPrecision=20000"
    ]

    def parse(self, response):
        for link in response.xpath("//ul[@class='ais-Hits-list']/li/article/a"):
            offer = link.xpath(".//@href").get()
            yield response.follow(offer, callback=self.parse_offer)
            yield {
                'offer': "https://www.welcometothejungle.com" + link.xpath(".//@href").get()
            }
            # alternative that enters each link to parse shiet
            # offer = link.xpath(".//@href")
            # yield response.follow(offer, callback=self.parse_offer)

        next_page = response.xpath("//li[@class='ais-Pagination-item ais-Pagination-item--nextPage']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_offer(self, response):
        # plain_text = response.xpath("//body//text").get()
        # print(plain_text)
        # ''.join(response.select("//body//text()").extract()).strip()
        # yield {
        #     'data': response.xpath("//body//text").get()
        # }

        yield {
            'offer': response.request.url
        }
        # for link in response.xpath("//body"):
        #     yield {
        #         'link': response.request.url
        #     } 
        