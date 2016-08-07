import unicodedata
import sqlite3
import json

from flask import Flask, request, g
from flask.ext.sqlalchemy import SQLAlchemy

import bluemix
import twitter
from env_vars import get_env_var


SQLALCHEMY_DATABASE_URI = get_env_var('DATABASE_URL')
application = Flask(__name__)
db = SQLAlchemy(application)


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
