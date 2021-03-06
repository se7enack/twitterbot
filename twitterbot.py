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
    for tweet in tweepy.Cursor(api.search, hashtag).items(5):
        try:
            print('Retweeted count: {0}'.format(tweet.retweet_count))
            if 1 <= tweet.retweet_count <= 3:
                tweet.favorite()
                tweet.retweet()
                now = datetime.now()
                print(now)
                print("https://twitter.com/" + str(tweet.id) + "/status/" + str(tweet.id))
                time.sleep(360)
        except tweepy.TweepError as e:
            print(e)


def follow():
    # Follow people that follow you
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print(follower.screen_name)


def unfollow():
    # Unfollow people that don't follow you
    nag()
    print("You are about to unfollow people that don't follow the account @%s." % api.verify_credentials().screen_name)
    print("Type 'yes' to confirm")
    unfollowthem = input(": ")
    if unfollowthem.lower() == 'yes':
        followers = api.followers_ids(twitter_handle)
        friends = api.friends_ids(twitter_handle)
        for friend in friends:
            if friend not in followers:
                print("Unfollowing {0}".format(api.get_user(friend).screen_name))
                api.destroy_friendship(friend)
            else:
                print("Keeping {0}".format(api.get_user(friend).screen_name))


def showfollowers():
    # Show people who follow you
    print(api.friends_ids(twitter_handle))
    friends = api.friends_ids(twitter_handle)
    for friend in friends:
        print("{0}".format(api.get_user(friend).screen_name))


def unfollowall():
    # Unfollow people that don't follow you
    nag()
    print("You are about to unfollow everyone for the account @%s." % api.verify_credentials().screen_name)
    print("Type 'yes' to confirm")
    unfollowthemall = input(": ")
    if unfollowthemall.lower() == 'yes':
        friends = api.friends_ids(twitter_handle)
        for friend in friends:
            print("Unfollowing {0}".format(api.get_user(friend).screen_name))
            api.destroy_friendship(friend)


def deleteallposts():
    # Delete all posts
    nag()
    print("You are about to delete all tweets for the account @%s." % api.verify_credentials().screen_name)
    print("Type 'yes' to confirm")
    deletethemall = input(": ")
    if deletethemall.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            api.destroy_status(status.id)
            print("Deleted:", status.id)


def menu():
    print(60 * '-')
    print("                   # T W I T T E R B O T                    ")
    print(60 * '-')
    print("0. > Reply to tweets <")
    print("1. > Like and retweet posts with a certain Hashtag <")
    print("2. > Follow users who follow you <")
    print("3. > Show your followers <")
    print("4. > Unfollow users who no longer follow you <")
    print("5. > Unfollow all of your followers! <")
    print("6. > Delete all of your posts! <")
    print(60 * '-')

    choice = input('Enter your choice [0-6] : ')
    try:
        choice = int(choice)
    except:
        menu()

    if choice == 0:
        search = input("What do you want to search for?: ")
        reply = input("What should your reply be?: ")
        talk(search, reply)
    elif choice == 1:
        search = input("Please enter hashtag: #")
        retweet(search)
    elif choice == 2:
        follow()
    elif choice == 3:
        showfollowers()
    elif choice == 4:
        unfollow()
    elif choice == 5:
        unfollowall()
    elif choice == 6:
        deleteallposts()
    else:
        menu()


def talk(search, reply):
    twt = api.search(q=search)

    t = [search,
         search.upper(),
         search.lower(),
         search.capitalize(),
         search.title()]

    for s in twt:
        for i in t:
            if i in s.text:
                sn = s.user.screen_name
                m = "@%s" % sn + " " + reply
                s = api.update_status(m, s.id)
                print("tweeted @%s" % sn)
                time.sleep(5)
            else:
                print("\"" + i + "\" \"" + s.text + "\"\n")
                time.sleep(1)


def nag():
    print("""\
                   _    _    ___   ______   _   _   _____   _   _   _____   _
                  | |  | |  / _ \  | ___ \ | \ | | |_   _| | \ | | |  __ \ | |
                  | |  | | / /_\ \ | |_/ / |  \| |   | |   |  \| | | |  \/ | |
                  | |/\| | |  _  | |    /  | . ` |   | |   | . ` | | | __  | |
                  \  /\  / | | | | | |\ \  | |\  |  _| |_  | |\  | | |_\ \ |_|
                   \/  \/  \_| |_/ \_| \_| \_| \_/  \___/  \_| \_/  \____/ (_)
 """)


menu()
    
