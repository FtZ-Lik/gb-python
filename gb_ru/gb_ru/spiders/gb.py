import scrapy
import my_login

class GbSpider(scrapy.Spider):
    name = 'gb'
    allowed_domains = ['gb.ru']
    start_urls = ['https://gb.ru/login']
    url = 'https://gb.ru/login'
    

    def parse(self, response):
        csrf = 'yVyefoMCBxN7EVhxDVBGz3gv0HCCt5czqbzUGujg/X+LZX5GB7LlRRJBStpyt2nF6QqvRu4aUYV7Qy8LBMxsFg=='
        yield scrapy.FormRequest(
            self.url, 
            method='POST', 
            callback=self.login,
            formdata={'user_email': my_login.login, 'user_password': my_login.password},
            headers={'csrf-token' : csrf}
            )
        
    def login(self, response):
        print('###############################3\n####################################\nlogin\n************************\n')
        print(response)
        print('*\n**\n***\n*****\n')
        j_body = response.json()
        print(j_body)
        # if j_body.get('authenticated'):

        #     yield response.follow(
        #         f'/{self.parse_user}',
        #         callback=self.user_data_parse,
        #         cb_kwargs={'username': self.parse_user}
        #     )
            
    