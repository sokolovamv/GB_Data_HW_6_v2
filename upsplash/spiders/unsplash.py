import scrapy
import scrapy
from scrapy.http import HtmlResponse
from upsplash.items import UpsplashItem
from scrapy.loader import ItemLoader


class UnsplashSpider(scrapy.Spider):
    name = "unsplash"
    allowed_domains = ["unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = ["https://unsplash.com/s/photos/beautiful"]
        #self.start_urls = ["https://unsplash.com"]

    def parse(self, response):
        links = response.xpath('//div[@class="ExNPQ"]/div[@class="zmDAx"]/a/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_image)
    
    def parse_image(self, response:HtmlResponse):
        loader = ItemLoader(item=UpsplashItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('category', '//div[@class="MbPKr M5vdR"]/div[@class="VZRk3 rLPoM"]/a/text()')
        loader.add_xpath('images', '//button/div[@class="omfF5"]/div[@class="MorZF"]/img/@srcset')

        yield loader.load_item()
