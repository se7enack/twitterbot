#!/usr/bin/env python3

import tweepy
import time
from datetime import datetime

# https://developer.twitter.com/en/apps
auth = tweepy.OAuthHandler('API_key','API_secret_key')
auth.set_access_token('Access_token','Access_token_secret')

user = api.me()
search = input("Please enter hashtag string: ")
numberOfTweets = 365250

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print('Retweeted count: {0}'.format(tweet.retweet_count))
        if 5 <= tweet.retweet_count <= 10:
            tweet.retweet()
            #tweet.favorite()
            now = datetime.now()
            print(now)
            print("https://twitter.com/" + str(tweet.id) + "/status/" + str(tweet.id))
            time.sleep(87)
    except tweepy.TweepError as e:
        print(e)
        
        
