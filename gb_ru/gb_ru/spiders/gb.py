import scrapy
import my_login

class GbSpider(scrapy.Spider):
    name = 'gb'
    allowed_domains = ['gb.ru']
    start_urls = ['https://gb.ru/login']
    url = 'https://gb.ru/login'
    

    def parse(self, response):
        #csrf = response.xpath('//input[@name="csrf-token"]/@value')
        csrf = 'dRQZzxFd/RhYUdb28S8OLzBYakyFACUJfnV5DnlfL9At6ZpC3QZGx401nmtLqeqLHyjFrKzfxC+cliwrrNfI3Q=='
        print(f'###############################3\n####################################\n{csrf}\n************************\n')
        yield scrapy.FormRequest.from_response(response, 
            self.url, 
            callback=self.after_login,
            formdata={'utf8' : "✓", 'user[email]': my_login.login, 'user[password]': my_login.password, 'authenticity_token' : csrf, 'user[remember_me]' : "0"},
            headers={'User-Agent' :	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0'}
            )
        
    def after_login(self, response):
        print('###############################3\n####################################\nlogin\n************************\n')
        with open('response.html', 'w') as response_file:
            response_file.write(response.text())
        print('*\n**\n***\n*****\n')
        j_body = response.json()
        print(j_body)
        
            
    