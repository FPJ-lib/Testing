#https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/?ref=rp
#https://www.upgrad.com/blog/build-twitter-sentiment-analysis-python/

'''
IMPORT:

Its the one working:

Take out:
RT;
Accounts:
Links.


$ pip install -U textblob #Error
$ python -m textblob.download_corpora
'''

import re 
import tweepy 
from tweepy import OAuthHandler 
#from textblob import TextBlob 
import pandas as pd 

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

	def get_tweets(self, query, count = 10): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 

		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count, lang='en') 


			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {}


				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 

				print('\nRetweets:\t',tweet.retweet_count)
				print('Tweet:   \t', parsed_tweet['text'],'####END###')

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
	tweets = api.get_tweets(query = 'F1', count = 70) 
	
	#i=1
	output =[]
	for tweet in tweets:
		#print(i,'\t',tweet['text'])
		#i+=1
		#print('\nType:\t',type(tweet))
		output.append(tweet['text'])
	return output

df = main()
#for i in df:
#	print('\n',i)

print()
df = pd.DataFrame(df, columns=['tweets'])
print(df)

df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Twitter/df', index=False)
print('\nOver')