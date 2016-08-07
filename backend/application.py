import unicodedata
import json

from flask import Flask, request, abort, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy

import bluemix
import twitter
from api.ebay_scrapper import EbayScrapper
from api.insight import Insight
from env_vars import get_env_var


application = Flask(__name__, static_url_path='')
application.config['SQLALCHEMY_DATABASE_URI'] = get_env_var('DATABASE_URL')
db = SQLAlchemy(application)

import models as m


@application.route('/')
def home():
    return application.send_static_file('index.html')

@application.route('/api/suggest-gift', methods=['GET'])
def get_suggestions():
    ret_val = []
    tweet_data = _get_tweet_data()
    model = m.EbayProduct.query
    for i in model:
        ret_val.append({
            'product_id': i.product_id,
            'product_name': i.product_name,
            'product_img_link': i.product_img_link,
            'product_price': i.product_price,
            'product_url': i.product_url,
            'personality_distance': Insight.personality_distance(
                tweet_data, json.dumps(i.personality_data),
            ) - (0.1 * min(i.times_clicked, i.times_suggested) / (i.times_suggested+1)),
            'personality_data': i.personality_data,
        })

    ret_val.sort(key=lambda x: x['personality_distance'])

    to_return = ret_val[:10]

    update_query = m.EbayProduct.query.filter(
        m.EbayProduct.product_id.in_([x['product_id'] for x in to_return])
    )

    for x in update_query:
        x.times_suggested += 1

    db.session.commit()

    return json.dumps(to_return)


@application.route('/api/query-product', methods=['GET'])
def get_distance():
    twitter_data = _get_tweet_data()
    product_id = request.args['product_id']
    model = m.EbayProduct.query.filter_by(product_id=product_id).first()
    if not model:
        product_data = EbayScrapper.scrape(product_id)
        personality_data = bluemix.analyse_text(product_id['reviews'])
        model = m.EbayProduct()
        model.product_id = product_id
        model.product_name = product_data['product']
        model.product_price = product_data['price']
        model.product_img_link = product_data['image']
        model.product_url = product_data['abs_url']
        model.personality_data = personality_data
        db.session.add(model)
        db.session.commit()

    return str(Insight.personality_distance(twitter_data, json.dumps(model.personality_data)))

@application.route('/api/click-suggestion', methods=['POST'])
def clicked_item():
    product_id = request.args['product_id']
    model = m.EbayProduct.query.filter_by(product_id=product_id).first()
    if not model:
        abort(400)

    model.times_clicked += 1
    db.session.commit()

    return "Success!"

# This is just a debug endpoint
@application.route('/api/twitter', methods=['GET'])
def request_tweet_data():
    return _get_tweet_data()

# Another debug endpoint
@application.route('/api/ebay', methods=['POST'])
def get_ebay_data():
    added_objs = []
    item_ids = request.get_json()
    if not item_ids:
        abort(400)
    for i in item_ids:
        model = m.EbayProduct.query.filter_by(product_id=i).first()
        if model:
            print("Skipping already added product with id {}".format(i))
            added_objs.append({
                'product_id': model.product_id,
                'personality_data': model.personality_data,
            })
            continue
        product_data = EbayScrapper.scrape(i)
        data = bluemix.analyse_text(product_data['reviews'])
        model = m.EbayProduct()
        model.product_id = i
        model.product_name = product_data['product']
        model.product_price = product_data['price']
        model.product_img_link = product_data['image']
        model.product_url = product_data['abs_url']
        model.personality_data = data
        db.session.add(model)
        db.session.commit()
        added_objs.append({
            'product_id': i,
            'personality_data': data,
        })
        print("Added new product with id {}".format(i))

    return json.dumps(added_objs)

def _get_tweet_data():
    username = request.args['user']
    model = m.TwitterUser.query.filter_by(user_id=username).first()
    if not model:
        tweets = twitter.get_tweets(username)
        text = unicodedata.normalize('NFKC', '\n'.join(tweets))
        data = bluemix.analyse_text(text)
        model = m.TwitterUser()
        model.user_id = username
        model.personality_data = json.dumps(data)
        db.session.add(model)
        db.session.commit()
        data = json.dumps(data)
    else:
        data = model.personality_data

    return data

def _get_ebay_data(tweet_data):
    '''Get 100 or whatever closest ebay products'''
    pass

if __name__ == '__main__':
    application.debug = True
    application.run()
