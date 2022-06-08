import tweepy
import time

auth = tweepy.OAuthHandler("API_KEY HERE","API_SECRET HERE")
auth.set_access_token("ACCESS_TOKEN HERE","ACCESS_TOKEN_SECRET HERE")

api = tweepy.API(auth, wait_on_rate_limit=True)


search = "#crypto OR #nft"
nrTweets = 500

for tweet in tweepy.Cursor(api.search_tweets, search).items(nrTweets):
    try:
        if not tweet.favorited:
            tweet.favorite()
            print("Tweet Liked")
            time.sleep(60)
    except tweepy.TweepyError as e:
        print(e.reason)
    except StopIteration:
        break
