# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value):
    value = value[0].strip()
    return value

def process_image(value:str):
    print()
    if value.startswith('//'):
        value = 'https:' + value.split()[0]
    else:
        value = value.split()[1]
    return value

class UpsplashItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    categoty = scrapy.Field(output_processor=TakeFirst())
    images = scrapy.Field(input_processor=MapCompose(process_image))
    _id = scrapy.Field()
    

