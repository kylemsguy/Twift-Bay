from api.ebay_scrapper import EbayScrapper

def get_ebay_data(item_id):
    product = EbayScrapper.scrape('101870458')
#product.keys()
#dict_keys(['reviews', 'price', 'product'])