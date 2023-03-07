# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class LeruaPipeline:
    def __init__(self):
        client = MongoClient()
        self.mongo_db = client.parser_goods
        
        
    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        if not len(list(collection.find({'link' : item['link']}))):
            collection.insert_one(item)
            print("Добавлено\n\n")
        else:
            print("Не добавлено - повтор\n\n")
        return item

class LeruaImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['imgs']:
            for img in item['imgs']:
                try:
                    yield Request(img)
                except Exception as e:
                    print(e)
                    
    # def item_completed(self, results, item, info):
    #     item['imgs'] = [itm[1] for itm in results if itm[0]]
    #     return item
                    