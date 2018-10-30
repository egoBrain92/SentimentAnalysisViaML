from twython import Twython
from textblob import TextBlob
import json
import pandas as pd


# Load credentials from json file
with open("../../twitter_credentials2.json", "r") as file:
    creds = json.load(file)

# Instantiate an object and print key and secret
print("CONSUMER_KEY" + creds['CONSUMER_KEY'])
print("CONSUMER_SECRET" + creds['CONSUMER_SECRET'])

python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'Trump',
         'result_type': 'popular',
         'count': 5,
         'lang': 'en',
         'tweet_mode' : 'extended',
         }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
mythonTweetsReturn = python_tweets.search(**query)['statuses'];
#print(mythonTweetsReturn)
print()

listOfTweets = ""
i = 1;
for status in mythonTweetsReturn:
    tempString = str(i)
    singleTweet = status['full_text']
    singleTweet = singleTweet.replace("\n", "")
    singleTweet = singleTweet.replace("\r", "")
    listOfTweets += tempString + ": " + singleTweet
    listOfTweets += "\n"
    i = i + 1;

print(listOfTweets)

'''
for status in mythonTweetsReturn:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)
'''
