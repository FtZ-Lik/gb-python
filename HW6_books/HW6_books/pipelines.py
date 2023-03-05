# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class Hw6BooksPipeline:
    def __init__(self):
        client = MongoClient()
        self.mongo_db = client.parser_book
    
    
    def process_item(self, item, spider):
        print('\n###\n', item, '\n###')
        collection = self.mongo_db[spider.name]
        if not len(list(collection.find({'link' : item['link']}))):
            collection.insert_one(item)
            print("Добавленно\n\n")
        else:
            print("Не добавленно - повтор\n\n")
        return item
