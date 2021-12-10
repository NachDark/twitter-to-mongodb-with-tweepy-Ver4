# ===============================================
# twitter-to-mongo.py v1.0 Created by Nacho Gaona
# ===============================================
import pymongo
import json
from tweepy.streaming import Stream
from tweepy import OAuthHandler
import datetime
import tweepy


# The MongoDB connection info. This assumes your database name is TwitterStream, and your collection name is tweets.
connection =  pymongo.MongoClient('localhost', 27017)
db = connection.TwitterStream


collection = db.tweets


# Optional - Only grab tweets of specific language
language = ['en']

# You need to replace these with your own values that you get after creating an app on Twitter's developer portal.
consumer_key = "XX"
consumer_secret = "XX"
access_token = "XX-XX"
access_token_secret = "XX"



# The below code will get Tweets from the stream and store only the important fields to your database
class MyStreamListener(Stream):

    def on_data(self, data):

        # Load the Tweet into the variable "t"
        t = json.loads(data)

        # Pull important data from the tweet to store in the database.
        tweet_id = t['id_str']  # The Tweet ID from Twitter in string format
        username = t['user']['screen_name']  # The username of the Tweet author
        followers = t['user']['followers_count']  # The number of followers the Tweet author has
        text = t['text']  # The entire body of the Tweet
        hashtags = t['entities']['hashtags']  # Any hashtags used in the Tweet
        dt = t['created_at']  # The timestamp of when the Tweet was created
        language = t['lang']  # The language of the Tweet

        # Convert the timestamp string given by Twitter to a date object called "created". This is more easily manipulated in MongoDB.
        created = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')

        # Load all of the extracted Tweet data into the variable "tweet" that will be stored into the database
        tweet = {'id':tweet_id, 'username':username, 'followers':followers, 'text':text, 'hashtags':hashtags, 'language':language, 'created':created}

        # Save the refined Tweet data to MongoDB
        collection.insert_one(tweet)

        # Optional - Print the username and text of each Tweet to your console in realtime as they are pulled from the stream
        print(username + ':' + ' ' + text)
        return True

    # Prints the reason for an error to your console
    def on_error(self, status):
        print (status)

# Some Tweepy code that can be left alone. It pulls from variables at the top of the script
if __name__ == '__main__':


  
    myStreamListener_new = MyStreamListener(consumer_key,consumer_secret,access_token,access_token_secret)
    myStreamListener_new.filter(track=['Pique'])



    ###########################
    #in case you want check updates from twitter timeline
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)

    #api = tweepy.API(auth)
    #public_tweets = api.home_timeline()
    #for tweete in public_tweets:  #this is another example to check the timeline from twits
    #    print (tweete.text)
