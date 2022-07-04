import tweepy
from twilio.rest import Client
from datetime import datetime, timezone
import os
import pprint

#Twilio Phone Number: +19707164834

now = datetime.now(timezone.utc).astimezone()
now.isoformat()

#Twilio API Account SID and AUTH TOKEN
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

#Twitter API Keys and tokens
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
auth = tweepy.Client(bearer_token)

screen_name = "grailed"
user = auth.get_user(username = screen_name)
grailed_id = user.data.id #User Id of GRAILED Twitter Account
username = user.data.username
name = user.data.name

keywords = "Dior OR Gucci"
query = 'keyword:{} from:{} -is.retweet'.format(grailed_id, keywords)
tweet_fields = "created_at"
tweets = auth.search_recent_tweets(
    query = query,
    tweet_fields = tweet_fields
)

for tweet in tweets.data:
    print(tweet.text)
    print(tweet.created_at)

max_recency_tweet_id = tweets.data[0].id