import sqlite3

from flask import Flask, request, g

import contracts.general as general_contracts
import contracts.tweet as tweet_contracts

DATABASE = './database.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return "HAI WRLD!"


@app.route('/anatweet', methods=['GET'])
def request_tweet_data():
    pass


if __name__ == '__main__':
    app.run()
