import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'test.csv'
    }
    start_urls = [
        'https://www.dwd.de/DE/derdwd/it/_functions/Teasergroup/bufr_de.html?nn=16102']

    def parse(self, response):

        for row in response.xpath(
                '//*[@class="tablewithborder docutils"]//tbody//tr'):
            yield {
                'first': row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle': row.xpath('td[3]//text()').extract_first(),
            }
