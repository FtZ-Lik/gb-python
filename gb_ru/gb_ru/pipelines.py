# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class GbRuPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        #print('*********************\n**************************\npipe\n')
        self.mongobase = client.gb_ru

    def process_item(self, item, spider):
        print('###\n##\n#\nproc_item pipe')
        collection = self.mongobase[item.get('username')]
        collection.insert_one(item)
        return item
