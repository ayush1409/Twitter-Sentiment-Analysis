import tweepy
from textblob import TextBlob

consumer_key = 'Vq4bB2uFtk8HPnTqeZiLeazKD'
consumer_secret =  'X82CzwP36l1HR2U5g2sMnsoDayq2AEF0LGUWCheD9bcnm4tfjO'

access_token =  '912685818661134336-ol8QdSYGhjF40fpSwFikOdS69P7akXL'
access_token_secret =  'Th2c1FUSULuivBHlsjCmkrXI69bEr3FCTcTMpR9PTCJhq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')		# search all tweets about "Donald Trump"

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print('\n',analysis.sentiment)

# sentiment(polarity, subjectivity)
# polarity : it measures how positive or negative a text is (1 positive, 0 negative)
