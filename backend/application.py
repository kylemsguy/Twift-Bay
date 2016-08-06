import sqlite3

from flask import Flask, jsonify, request, g

from env_vars import get_env_var
import bluemix

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
    data = bluemix.analyse_text(request.args['text'])
    return jsonify(**data)


if __name__ == '__main__':
    app.run()
