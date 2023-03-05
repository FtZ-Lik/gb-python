import scrapy
from HW6_books.items import Hw6BooksItem

class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/books/?price_min=&price_max=&age_min=&age_max=&form-pubhouse=&russianonly=1&id_genre=570&paperbooks=1&otherbooks=1&available=1&nrd=1']
    
    def parse(self, response):
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        
        content_path = "//div[contains(@class, 'genres-catalog')]/div/div/div/div/div[contains(@class, 'products-row-outer')]/div/div[contains(@class, 'genres-carousel__item')]"
        books_name_list = response.xpath(content_path + "/div/div/a[contains(@class, 'product-title-link')]/span[contains(@class, 'product-title')]/text()").getall()
        author_name_list = response.xpath(content_path + "/div/div[contains(@class, 'product-cover')]/following::div[1]/a[1]/@title").getall()
        old_price_list = response.xpath(content_path + "/div/div[contains(@class, 'product-cover')]/div/div[contains(@class, 'price-label')]/div/div/span[@class = 'price-old' or not(contains(@title, '%'))]/span/text()").getall()
        new_price_list = response.xpath(content_path + "/div/div[contains(@class, 'product-cover')]/div/div[contains(@class, 'price-label')]/div/div/span[@class = 'price-val']/span/text()").getall()
        link_list = ['https://www.labirint.ru' + s for s in response.xpath(content_path + "/div/div/a[contains(@class, 'product-title-link')]/@href").getall()]
        result = []
        for i in range(len(books_name_list)):
            yield Hw6BooksItem(name = books_name_list[i], author = author_name_list[i], old_price = old_price_list[i], new_price = new_price_list[i], link = link_list[i])
        print(f'\n###\n###\n###\n{result}\n###\n###\n###\n')
