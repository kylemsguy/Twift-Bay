import unicodedata
import json

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

import bluemix
import twitter
from env_vars import get_env_var


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = get_env_var('DATABASE_URL')
db = SQLAlchemy(application)

import models as m


@application.route('/')
def home():
    return "HAI WRLD!"


@application.route('/twitter', methods=['GET'])
def request_tweet_data():
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

if __name__ == '__main__':
    application.debug = True
    application.run()
