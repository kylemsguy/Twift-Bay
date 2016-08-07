import unicodedata
import sqlite3
import json

from flask import Flask, request, g

import bluemix
import twitter
from env_vars import get_env_var

DATABASE = './database.db'

application = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@application.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@application.route('/')
def home():
    return "HAI WRLD!"


@application.route('/twitter', methods=['GET'])
def request_tweet_data():
    username = request.args['user']
    tweets = twitter.get_tweets(username)
    text = unicodedata.normalize('NFKC', '\n'.join(tweets))
    data = bluemix.analyse_text(text)
    return json.dumps(data)


if __name__ == '__main__':
    application.debug = True
    application.run()
