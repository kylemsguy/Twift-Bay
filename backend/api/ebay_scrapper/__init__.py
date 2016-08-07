import requests
from bs4 import BeautifulSoup  

class EbayScrapper:

    @staticmethod
    def scrape(product_id=''):
        product_id = str(product_id)
        r = requests.get('http://www.ebay.com/p/' + product_id)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        product_name = soup.find_all('div', class_='product-header')[0].h1.text
        price = float(soup.find_all('meta', itemprop='price')[0].get('content'))

        target = 'http://www.ebay.com/urw/product-reviews/' + product_id
        target += '?pgn='
        page_number = 1
        blob = ''

        while page_number <= 5:
            r = requests.get(target + str(page_number))
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            reviews_section = soup.select("#reviewsContentWrapper")
            if reviews_section == []:
                break
            reviews = reviews_section[0].find_all(
                'div', class_='ebay-review-section')
            for review in reviews:
                section_r = review.select('div.ebay-review-section-r')[0]
                title = section_r.select('p.review-item-title')[0].text
                if section_r.select('p.review-item-content') != []:
                    body = section_r.select(
                        'p.review-item-content')[0].text.replace('Read full review...', '')

                blob += title + ' ' + body + '\n\n'
            page_number += 1

        return {
            'product': product_name,
            'price': price,
            'reviews': blob
        }