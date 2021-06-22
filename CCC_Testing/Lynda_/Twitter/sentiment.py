#https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/?ref=rp
#https://www.upgrad.com/blog/build-twitter-sentiment-analysis-python/

'''
IMPORT:
$ pip install -U textblob #Error
$ python -m textblob.download_corpora
'''

import re 
import tweepy 
from tweepy import OAuthHandler 
#from textblob import TextBlob 

class TwitterClient(object): 
	''' 
	Generic Twitter Class for sentiment analysis. 
	'''
	def __init__(self): 
		''' 
		Class constructor or initialization method. 
		'''
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'odl1KBOxmcy0whmKhYPtpAfQJ'
		consumer_secret = 'beEyQTRTTHFWPPxlxmDM6FVkoNwGkCCUKOqp8CJ1ukPtUTMPny'
		access_token = '821372440899125248-b5SHR8xeTUb8ExvfhcPoh1ftfZBL2h0'
		access_token_secret = 'ygoUs2GfnNISWLBNcIsSYHfdY8MDzHwyDCx23A6hQ6K6D'
        #bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPZBIgEAAAAAWTOxJkjW1xc7ZAxAzKVKg3Q2nfI%3DSGcKGKTRstzIq3xLeDUj63b4AbrVgFUMMGCVcLijf4ADbm2Fbh'
		print('\n')
		# attempt authentication 
		try: 
			# create OAuthHandler object 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			# set access token and secret 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("\n\nError: Authentication Failed\n") 

	def clean_tweet(self, tweet):  #Make with RE
		''' 
		Utility function to clean tweet text by removing links, special characters 
		using simple regex statements.  #REGEXXXX
		'''

		#return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
		return ''.join(tweet.split())

	'''
	analysis = TextBlob(self.clean_tweet(tweet))
	def get_tweet_sentiment(self, tweet): 
		
		Utility function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		
		# create TextBlob object of passed tweet text 
        #analysis = TextBlob(self.clean_tweet(tweet))  #############
		analysis = tweet
        # set sentiment 
		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'
	'''

	def get_tweets(self, query, count = 10): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 

		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count) 

			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {} 


				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 
				# saving sentiment of tweet 
				
				#parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				# appending parsed tweet to tweets list 
				if tweet.retweet_count > 0: 
					#print('\nParsed:')
					# if tweet has retweets, ensure that it is appended only once 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet)
						#print(parsed_tweet)
				else: 
					tweets.append(parsed_tweet) 

			# return parsed tweets 
			return tweets 

		except tweepy.TweepError as e: 
			# print error (if any) 
			print("Error : " + str(e)) 

def main(): 
	# creating object of TwitterClient Class 
	api = TwitterClient()
	# calling function to get tweets 
	tweets = api.get_tweets(query = 'Donald Trump', count = 10) 
	
	print('\n\n\nLoop:')
	for tweet in tweets:
		print(tweet)
	


	# picking positive tweets from tweets 
	#ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
	# percentage of positive tweets 
	#print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
	# picking negative tweets from tweets 
	#ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
	# percentage of negative tweets 
	#print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
	# percentage of neutral tweets 
	#print("Neutral tweets percentage: {} %".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))) 

	# printing first 5 positive tweets 
	#print("\n\nPositive tweets:") 
	#for tweet in ptweets[:10]: 
	#	print(tweet['text']) 

	# printing first 5 negative tweets 
	#print("\n\nNegative tweets:") 
	#for tweet in ntweets[:10]: 
	#	print(tweet['text']) 

#if __name__ == "__main__": 
#	# calling main function 
#	main() 

main()

print('\n\n\n\n\n\n\n\n\n')