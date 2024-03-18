import scrapy

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia_spider'
    start_urls = ['https://it.wikipedia.org/wiki/Streghe_(serie_televisiva_1998)']

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        for link in links:
            yield {
                'link': link
            }