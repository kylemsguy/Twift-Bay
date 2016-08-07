import unicodedata
import json

from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy

import bluemix
import twitter
from api.ebay_scrapper import EbayScrapper
from api.insight import Insight
from env_vars import get_env_var


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = get_env_var('DATABASE_URL')
db = SQLAlchemy(application)

import models as m


@application.route('/')
def home():
    return "HAI WRLD!"

@application.route('/api/suggest-gift', methods=['GET'])
def get_suggestions():
    twitter_user = request.args['user']
    pid_to_distance = {}
    tweet_data = _get_tweet_data()
    model = m.EbayProduct.query
    for i in model:
        model[i.product_id] = Insight.personality_distance(tweet_data, i.personality_data)

    


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
