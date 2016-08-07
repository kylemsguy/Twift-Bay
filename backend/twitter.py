import tweepy

from env_vars import get_env_var

CONSUMER_KEY = get_env_var('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = get_env_var('TWITTER_CONSUMER_SECRET')

ACCESS_TOKEN = get_env_var('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = get_env_var('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_tweets(username):
    target_tweets = api.user_timeline(username, count=2300)
    return [t.text for t in target_tweets]