#!/usr/bin/env python3

import tweepy
import time
from datetime import datetime
from apikeys import apikeys

api_key = apikeys['api_key']
api_secret_key = apikeys['api_secret_key']
access_token = apikeys['access_token']
access_token_secret = apikeys['access_token_secret']
twitter_handle = apikeys['twitter_handle']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()


def retweet(hashtag):
    # Like and retweet tweets with a certain hashtag
    numberoftweets = 365250
    for tweet in tweepy.Cursor(api.search, hashtag).items(numberoftweets):
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


def follow():
    # Follow people that follow you
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print(follower.screen_name)


def unfollow():
    # Unfollow people that don't follow you
    followers = api.followers_ids(twitter_handle)
    friends = api.friends_ids(twitter_handle)
    for friend in friends:
        if friend not in followers:
            print("Unfollowing {0}".format(api.get_user(friend).screen_name))
            api.destroy_friendship(friend)
        else:
            print("Keeping {0}".format(api.get_user(friend).screen_name))


def unfollowall():
    # Unfollow people that don't follow you
    followers = api.followers_ids(twitter_handle)
    friends = api.friends_ids(twitter_handle)
    for friend in friends:
        print("Unfollowing {0}".format(api.get_user(friend).screen_name))
        api.destroy_friendship(friend)


def menu():
    print(30 * '-')
    print("     T W I T T E R B O T   ")
    print(30 * '-')
    print("1. Retweet Hashtag")
    print("2. Follow users who follow you")
    print("3. Unfollow users who don't follow you anymore")
    print("4. Unfollow them all!")
    print(30 * '-')

    choice = input('Enter your choice [1-4] : ')
    choice = int(choice)

    if choice == 1:
        search = input("Please enter hashtag: #")
        retweet(search)
    elif choice == 2:
        follow()
    elif choice == 3:
        unfollow()
    elif choice == 4:
        unfollowall()
    else:
        pass


menu()
  
