from api.ebay_scrapper import EbayScrapper

def get_ebay_data(item_id):
    return EbayScrapper.scrape(item_id)
#product.keys()
#dict_keys(['reviews', 'price', 'product'])
