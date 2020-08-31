import tweepy
import csv
from dotenv import load_dotenv
import os

load_dotenv()

# User credentials to access Twitter API
# Put your twitter credentials in a .env File if making public

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 3200 is the maximum number of tweets available from a twitter user timeline
num_tweets = 3200

biden_tweets_csv = open('test.csv', 'w', encoding="utf_8_sig", newline='')
csv_writer = csv.writer(biden_tweets_csv)
csv_writer.writerow(['text', 'created_at', 'retweet_count',
                     'favorite_count', 'is_retweet', 'id_str'])
biden_tweets = []

for tweet in tweepy.Cursor(api.user_timeline,
                           screen_name='JoeBiden',
                           count=200,
                           tweet_mode='extended',
                           include_rts=True,
                           ).items(num_tweets):

    if "retweeted_status" in tweet._json:
        csv_writer.writerow([tweet.full_text, tweet.created_at, tweet.retweet_count, tweet.favorite_count,
                             True, tweet.id_str])
    else:
        csv_writer.writerow([tweet.full_text, tweet.created_at, tweet.retweet_count, tweet.favorite_count,
                             False, tweet.id_str])
    biden_tweets.append(tweet)
    print(tweet)

biden_tweets_csv.close()
print('# tweets: ', len(biden_tweets))
