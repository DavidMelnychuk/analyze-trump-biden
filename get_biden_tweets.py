import tweepy
import csv

# User credentials to access Twitter API
# Put in .ENV File if making public on github
ACCESS_TOKEN = '1021581972227776513-PqahU1pcZSeqAJHqsccSuUB7BystUi'
ACCESS_SECRET = 'LJJok1yWAhUCI371MnwBmxtsDGSMrzi51aaON3X1GButI'
CONSUMER_KEY = 'sGvMZG52HeaBqBywIT0Ttx4ZD'
CONSUMER_SECRET = 'ULyYcj0q0TgS0eTIJpAjanWeqAGeLh9ZuLofQYes33klEMSGAn'

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 3200 is the maximum number of tweets available from a twitter user timeline
num_tweets = 3200

biden_tweets_csv = open('biden.csv', 'w', encoding="utf_8_sig", newline='')
csv_writer = csv.writer(biden_tweets_csv)
csv_writer.writerow(['text', 'created_at', 'retweet_count', 'favorite_count', 'is_retweet', 'id_str'])
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
