import json, os
from nltk.sentiment.vader import SentimentIntensityAnalyzer as si
import matplotlib.pyplot as plt
import numpy as np


class FileTreat():
	'''This is class is proposed to treat the data of collected tweets'''

	def __init__(self):
		self.__FILEPATH = os.path.dirname(os.path.abspath(__file__)) + '/src/tweetSeguidoresmydarkmind2.json'
		self.__FILEGOODPATH = os.path.dirname(os.path.abspath(__file__)) + '/src/tweetSeguidoresGoodVibeCatalog2.json'
		#do a json parse of tweets
		self._content = self._openFile(self.__FILEPATH)
		self._goodContent = self._openFile(self.__FILEGOODPATH)
		#gets all content from those tweets with a label
		#the return is an tuple containing ()
		self._allContent = self.getWithLabel()
																																																																																																																																																																																																																																														

	def _openFile(self, path):
		'''Get the content in a json format and do a parse to python dictionary format, storing in the class'''

		#parsed tweets
		tweets = []
		
		i = 1
		f = open(path, 'r')
		for line in f.readlines():
			try:
				#do a parse
				tweets.append(json.loads(line.replace('\\', ''), strict=False))
				#print(i)
				#i = i +1
			except ValueError:
				continue

		f.close()
		return tweets

	def _getTweetsContent(self, items):
		'''gets only the text of each tweet'''
		content = []
		for reg in items:
			#content.extend(reg['tweets'])
			for item in reg['tweets']:
				content.append(item['text'])

		return content

	def getGoodTweets(self):
		return self._getTweetsContent(self._goodContent)

	def getBadTweets(self):
		return self._getTweetsContent(self._content)

	def getTweets(self):
		tweets = self.getGoodTweets()
		tweets.extend(self.getBadTweets())

		return tweets

	def getBadWithLabel(self):
		tweets = self._content
		Y = [ -1 for i in range(len(tweets))]

		return (tweets, Y)

	def getGoodWithLabel(self):
		tweets = self._goodContent
		Y = [ 1 for i in range(len(tweets))]

		return (tweets, Y)

	def getWithLabel(self):
		'''
		gets all the data from the dataset with label.
		returns 
		'''
		tuplg = self.getGoodWithLabel()
		tuplb = self.getBadWithLabel()

		tuplg[0].extend(tuplb[0])
		tuplg[1].extend(tuplb[1])

		return tuplg


	def getUserMeanPolarity(self, user):
		'''
		these method receive an dictionary in the format {'user': '@userTag', 'tweets': [{}, {}, ..., {}]}
		and gets the mean of sentiment polarity for each user based on polarity of these tweets.
		returns a list in the format [{'user': '@userName', 'means': {'neg': 0.0, 'pos': 0.0, 'neu': 0.0, 'compound': 0.0}]
		'''
		if user is None:
			return

		analyser = si()
		#hold polarity values
		means = {'neg': 0.0, 'pos': 0.0, 'neu': 0.0, 'compound': 0.0}

		if len(user['tweets']) == 0:
			return {'user' : user['user'], 'means': means}

		#get values
		for tweet in user['tweets']:
			polarity = analyser.polarity_scores(tweet['text'])

			means['neg'] 		= means['neg'] + polarity['neg']
			means['pos'] 		= means['pos'] + polarity['pos']
			means['neu'] 		= means['neu'] + polarity['neu']
			means['compound'] 	= means['compound'] + polarity['compound']
			
		#do a simple mean
		size = len(user['tweets'])
		means['neg'] 		= means['neg'] / size
		means['pos'] 		= means['pos'] / size
		means['neu'] 		= means['neu'] / size
		means['compound'] 	= means['compound'] / size
		
		means['user'] = user['user']

		return { 'user': user['user'], 'means': means}


	def getBadUsersMeanPolarity(self):
		return self.getUsersMeanPolarity(self._content)

	def getBadUsersMeanPolarity(self):
		return self.getUsersMeanPolarity(self._goodContent)

	def getUsersMeanPolarity(self, users):
		lista = []
		for user in users:
			lista.append(self.getUserMeanPolarity(user))
		return lista



#file = FileTreat()


#print(file.getUsersMeanPolarity(None))


'''plt.hist([0,8,6,8,0,7,65,64,56,45,3,4,6,345,34,5,345,3,2,24,23,4,23,42,34,3,24,34,3,4,34], facecolor='green', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()'''