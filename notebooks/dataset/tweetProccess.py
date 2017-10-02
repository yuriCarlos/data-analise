import json, os


class FileTreat():
	'''This is class is proposed to treat the data of collected tweets'''

	def __init__(self):
		self.__FILEPATH = os.path.dirname(os.path.abspath(__file__)) + '/src/tweetSeguidoresmydarkmind2.json'
		self.__FILEGOODPATH = os.path.dirname(os.path.abspath(__file__)) + '/src/tweetSeguidoresGoodVibeCatalog2.json'
		self._content = self._openFile(self.__FILEPATH)
		self._goodContent = self._openFile(self.__FILEGOODPATH)
																																																																																																																																																																																																																																														

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



#file = FileTreat()

#print(file.getTweets())
