import tweepy
from twilio.rest import Client
from datetime import datetime, timezone
import os
import pprint
import time

#Twilio Phone Number: +19707164834

now = datetime.now(timezone.utc).astimezone()
now.isoformat()

#Twilio API Account SID and AUTH TOKEN, Client Configuration
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

#Twitter API Keys and tokens
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
auth = tweepy.Client(bearer_token)

screen_name = "grailed"
user = auth.get_user(username = screen_name)
grailed_id = user.data.id #User Id of GRAILED Twitter Account
username = user.data.username
name = user.data.name
query = 'from:{} -is.retweet'.format(grailed_id)
tweet_fields = "created_at"

def newest_id():
    tweets = auth.search_recent_tweets(
        query = query,
        max_results = 100
    )
    max_recency_tweet_id = tweets.data[0].id
    return max_recency_tweet_id

def notif():
    last_7 = auth.search_recent_tweets(
        query = query,
        since_id = newest_id() #only pulls tweets that are newer than the previously newest tweet
    )
    k1 = input("Enter topic 1 (not case sensitive): ")

    if k1 in last_7.text.lower():
        print("Sending notification...")
        message = client.messages.create(
            to="+17326372256", 
            from_="+19707164834",
            body="""Grailed has tweeted about a topic that you are interested in! 
            Click the following link to be redirected to the tweet: https://twitter.com/SOLELINKS/status/""" + str(last_7.tweet.id))

while True:
    notif()
    time.sleep(172800) #sleeps for 2 days