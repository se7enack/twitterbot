#!/usr/bin/env python3

import tweepy
import time
from datetime import datetime
from apikeys import apikeys

api_key = apikeys['api_key']
api_secret_key = apikeys['api_secret_key']
access_token = apikeys['access_token']
access_token_secret = apikeys['access_token_secret']

auth = tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = input("Please enter hashtag string: ")
numberOfTweets = 365250

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print('Retweeted count: {0}'.format(tweet.retweet_count))
        if 1 <= tweet.retweet_count <= 3:
            tweet.retweet()
            tweet.favorite()
            now = datetime.now()
            print(now)
            print("https://twitter.com/" + str(tweet.id) + "/status/" + str(tweet.id))
            time.sleep(90)
    except tweepy.TweepError as e:
        print(e)

        
