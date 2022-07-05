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

screen_name = input("Enter the twitter handle you would like to search for: \n")
user = auth.get_user(username = screen_name)
twit_user_id = user.data.id #User Id of Twitter Account
username = user.data.username
name = user.data.name
query = 'from:{} -is.retweet -is.reply'.format(twit_user_id) #filters out retweets and replies from twitter account
storage = 'newest_tweet_id.txt'

tweets = auth.search_recent_tweets(
    query = query,
    max_results = 100
)

max_recency_tweet_id = tweets.data[0].text

def get_newest_id(storage):
    if os.stat(storage).st_size == 0: #checks if storage file is empty
        newest_id = max_recency_tweet_id #sets newest_id to the tweet id with the maximum recency as calculated above
        return newest_id
    else:
        read = open(storage, 'r')
        newest_id = int(read.read().strip())
        read.close()
        return newest_id

#saves newest_id to the storage file for record-keeping purposes and to be used in the next query
def set_newest_id(newest_id, storage):
    write = open(storage, 'w')
    write.write(str(newest_id))
    write.close()
    return


def notif():
    newest_id = get_newest_id(storage)
    most_recent_tweets = auth.search_recent_tweets(
        query = query,
        since_id = newest_id,
        max_results = 100 #only pulls tweets that are newer than the previously newest tweet
    )

    for r in most_recent_tweets.data:
        newest_id = r.id
        set_newest_id(newest_id, storage)

    k1 = input("Enter topic 1 (not case sensitive): ")
    for tweet in most_recent_tweets.data:
        if k1 in tweet.text.lower():
            print("Sending notification...")
            message = client.messages.create(
                to="+17326372256", 
                from_="+19707164834",
                body="""The account you are searching for has tweeted about a topic that you are interested in!\n
                This is the tweet: \n
                {}\n
                Click the following link to be redirected to the tweet: https://twitter.com/{}/status/""".format(tweet.text,user.data.username) + str(tweet.id))
            print(message.sid)
      
while True:
    notif()
    time.sleep(30) #sleeps for 30 seconds