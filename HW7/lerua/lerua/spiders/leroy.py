import scrapy
from lerua.items import LeruaItem
from scrapy.loader import ItemLoader

class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/lighting/outdoor-lighting/solar-lamps/']

    def parse(self, response):
        next_page = response.xpath("//a[contains(@class, 'next')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_goods)
        
        links = response.xpath("//li[contains(@class, 'product-card')]/a[1]/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_goods)
        
    def parse_goods(self, response):
        loader = ItemLoader(item=LeruaItem(), response=response)
        
        loader.add_xpath('name', "//div[@class='product-essential__left-col']/h1[contains(@class, 'product-essential__name')]/text()")
        loader.add_xpath('price', "//div[@class='product-essential__right-col']//div[contains(@class, 'curent-price')]//span[@class='price']/span/span[1]/text()")
        loader.add_value('imgs', ['https://www.castorama.ru' + link for link in response.xpath("//div[contains(@class, 'product-media__top-slider')]/*/li[contains(@class, 'top-slide swiper-slide')]/div/img[1]/@data-src").getall()])
        loader.add_value('link', response.url)
        #print(['https://www.castorama.ru' + link for link in response.xpath("//div[contains(@class, 'product-media__top-slider')]/*/li[contains(@class, 'top-slide swiper-slide')]/div/img[1]/@data-src").getall()])
        yield loader.load_item()
