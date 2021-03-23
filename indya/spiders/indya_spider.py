import scrapy
from indya.items import IndyaItem

class QuotesSpider(scrapy.Spider):
    name = 'indya_spider'
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
    ]
    
    def parse(self,response):
        items = IndyaItem()

        for i in range(len(response.css('#JsonProductList p::text').extract())):
            description = response.css('#JsonProductList p::text')[i].extract()
            price = response.css('#JsonProductList span:nth-child(1)')[i].css('::text').extract()
            image_url = response.css('#JsonProductList .lazy')[i].css('::attr(data-original)').extract()
            items['description'] = description
            items['price'] = price
            items['image_url'] = image_url
            yield items