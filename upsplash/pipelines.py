# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class UpsplashPipeline:
    def process_item(self, item, spider):
        return item

class ImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img_url in item['photos']:
                try:
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)

        #return super().get_media_requests(item, info)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
        #return super().item_completed(results, item, info)

"""
class UpsplashPipeline:
    def process_item(self, item, spider):
        return item
        """
