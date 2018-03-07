import tweepy
from textblob import TextBlob

consumer_key = 'enter here'
consumer_secret =  'enter here'

access_token =  'enter here'
access_token_secret =  'enter here'

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
