twitter-to-mongo
================

A python script that uses the Tweepy library to pull Tweets with specific keywords from Twitter's Streaming API, and then stores the important fields from the Tweet in a MongoDB collection.

What gets stored in MongoDB?
----------------------------
  - The tweet ID
  - The username of the tweet author
  - The follower count of the tweet author
  - The full body of the tweet
  - Any hashtags used in the tweet
  - The timestamp of the tweet's creation
  - The language of the tweet

Dependencies:
-------------
    (python -m pip install --upgrade pip)

  - Tweepy 4.0.0(pip install tweepy)
  - Pymongo( python -m pip install pymongo )
  - MongoDB ( https://www.mongodb.com)

5 minute setup (Assumes the dependencies are already installed):
------------------
  - Have MongoDB installed on localhost, and create a database called TwitterStream
  - Open the script and add the keywords or hashtags you want to track to the "keywords" variable
  - Save it to your project folder or any easy to access folder
  - Open your console and cd to the folder that you just put the script in
  - Type the command $ python YOURSCRIPTNAME.py
  - Watch as tweets hit the console in realtime, all while being stored in your database
