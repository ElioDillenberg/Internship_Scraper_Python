import scrapy

class   WelcomeToTheJungle(scrapy.Spider):
    name = "WelcomeToTheJungle"

    start_urls= [
        "https://www.welcometothejungle.com/fr/jobs?page=16&configure%5Bfilters%5D=website.reference%3Awttj_fr&configure%5BhitsPerPage%5D=30&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Backend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Fullstack&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Project%20%2F%20Product%20Management&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Science&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Autres&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=DevOps%20%2F%20Infra&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Recherche%20%2F%20R%26D&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Frontend&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Engineering&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=QA&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Hardware&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Dev%20Mobile&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=T%C3%A9l%C3%A9coms%20%2F%20R%C3%A9seaux&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=S%C3%A9curit%C3%A9&aroundLatLng=48.8546%2C2.3477&aroundQuery=Paris%2C%20France&aroundRadius=50000&aroundPrecision=50000"
    ]
    def parse(self, response):
        a = response.css('.ais-Hits-item').getall()
        yield {'link': a}

    # def parse(self, response):
    #     print("START\n\n\n\n\n\n\n")
        # for sel in response.xpath("//li[@class='ais-Hits-list']/article/a"):
        # offer_link = response.xpath("//ul/li/a").extract
        # offer_link = sel.xpath("@href").extract()
        # yield {'link': offer_link}
        # print (offer_link)
        # for offer in response.xpath("//li[@class='ais-Hits-list']").extract():
            # print("coucou\n\n\n\n\n\n")
            # yield {
                # 'link': offer.xpath(".//li[@class ='ais-Hits-list']/article/a").extract()
            # }
        # next_page = response.xpath("//li[@class]='ais-Pagination-item ais-Pagination-item--nextPage'/a/@href").extract()
        # if next_page is not None:
        #     next_page_link = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link, callback=self.parse)