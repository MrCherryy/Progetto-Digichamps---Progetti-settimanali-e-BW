import scrapy

class NewsTitlesSpider(scrapy.Spider):
    name = 'newstitles'
    start_urls = ['https://www.tgcom24.mediaset.it/news-tag/harry-potter/']

    def parse(self, response):
        titles = response.css('h1::text').extract()
        for title in titles:
            yield {
                'title': title
            }