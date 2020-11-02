import tweepy
import time

# https://developer.twitter.com/en/apps
auth = tweepy.OAuthHandler('API_key','API_secret_key')
auth.set_access_token('Access_token','Access_token_secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = "Python"
numberOfTweets = 365250

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print('Retweeted {0}'.format(tweet.retweet_count))
        if tweet.retweet_count > 1:
            tweet.retweet()
            time.sleep(87)
            # tweet.favorite()
            # print('Tweet Liked')
    except tweepy.TweepError as e:
        print(e)
        
