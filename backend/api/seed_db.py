from ebay_scrapper import EbayScrapper

with open('../seed_data.csv', 'r') as f:
    product_ids = [product_id.strip() for product_id in f]
    for product_id in product_ids:
        print(product_id)
        p = EbayScrapper.scrape(product_id)