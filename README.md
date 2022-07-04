# Twitter Bot #

This script will utilize the Twitter API through Tweepy, along with a SMS Messaging service through Twilio to provide users with updates on Grailed's twitter posts. Specifically, a user can decide which tweets to be notified about via SMS, instead of receiving push notifications for all tweets that Grailed posts on its account.

## Specifications ##
* ***input_bot.py*** will allow for a user to input a twitter handle, along with one keyword to filter to. The user will only receive notifications that fulfill the inputs that they have given.
* ***grailed_bot.py*** will allow for a user to input 4 parameters/keywords to filter to (such as a specific brand). The user will only receive notifications from the GRAILED twitter page of tweets made including the specified parameters.
* ***newest_tweet_id.txt*** stores the most recent tweet id from the previous running instance of the script. This allows for all future notifications to only include tweets that were made after the previous instance. This file is currently being used for both input_bot.py and grailed_bot.py.
* ***send_sms.py*** is a sample script taken from Twilio, providing the basic framework for setting up the SMS service for the script. Each user should implement their own Account SID and AUTH TOKEN in the bot scripts.
