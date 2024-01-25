from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

class ChocolateProductLoader(ItemLoader):
    
    default_output_processor = TakeFirst()

    #Remove the pound sign from the price
    price_in = MapCompose(lambda x: x.split("£")[-1])

    #Add the base url to the relative url
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x )