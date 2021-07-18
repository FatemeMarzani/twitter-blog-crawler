import scrapy
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

class PostSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://blog.twitter.com/'
    ]

    def __init__(self):
    
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=opts)
        self.driver.get('https://blog.twitter.com/')

    def parse(self,response):
         while True:
            self.driver.get(response.url)
            for post in self.driver.find_elements_by_css_selector('div.results-loop__result'):

                yield {'title': post.find_elements_by_css_selector('.result__copy a')[0].text,
                       'author':post.find_elements_by_css_selector('.result__byline p a')[0].text,
                       'date':post.find_elements_by_css_selector('.result__byline p time')[0].text
                }

            try:
                self.driver.find_element_by_css_selector('a.js-load-more').click()
            except Exception: 
                break

 