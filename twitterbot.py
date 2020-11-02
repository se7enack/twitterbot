import tweepy
import time

# https://developer.twitter.com/en/apps
auth = tweepy.OAuthHandler('API_key','API_secret_key')
auth.set_access_token('Access_token','Access_token_secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = "Python"
numberOfTweets = 11

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        time.sleep(900)
        print('Tweet Liked')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
