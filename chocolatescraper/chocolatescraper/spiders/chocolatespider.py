import scrapy
from chocolatescraper.items import ChocolateProduct
from chocolatescraper.itemloaders import ChocolateProductLoader

class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        #get all products on page
        products = response.css('product-item')
        

        for product in products:
            chocolate = ChocolateProductLoader(item=ChocolateProduct(), selector=product)

            #here is how data is formatted
            #used a customized dict to store data
            chocolate.add_css('name', "a.product-item-meta__title::text")
            chocolate.add_css('price', 'span.price::text', re=r'£(\d+\.\d+)')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')

            yield chocolate.load_item()
            

        #get next page
        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)
