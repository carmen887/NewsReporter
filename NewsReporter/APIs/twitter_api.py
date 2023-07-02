import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['twitter']['consumer_key']
consumer_key_secret = config['twitter']['consumer_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

from tweepy.auth import OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = 'ultimahsv'
keywords = "#ULTIMAHORA AND SeguridadCiudadana"
limit=500

tweets = tweepy.Cursor(api.search_tweets, q=keywords, tweet_mode='extended').items(limit)

columns = ['User', 'Tweet']
data = []
for tweet in tweets: data.append([tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)
df.to_csv('tweets.csv')
