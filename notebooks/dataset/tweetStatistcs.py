import matplotlib.pyplot as plt
import numpy as np
from tweetProccess import FileTreat

class TweetAnalyse():
	def __init__(self):
		self._treat = FileTreat()
		self.badContent = self._treat.getBadWithLabel()
		self.goodContent = self._treat.getGoodWithLabel()

	def loadPolarities(self):
		'''Store the polarities to save time'''
		self.badPolarities = self._treat.getUsersMeanPolarity(self.badContent[0])
		self.goodPolarities = self._treat.getUsersMeanPolarity(self.goodContent[0])

	def showPolarityHist(self, users, key, title):
		'''Shows a histogram'''
		
		#set up the histogram
		plt.hist([user['means'][key] for user in users])
		plt.xlabel('Users')
		plt.ylabel('Neg. Polarity')
		plt.title(title)
		plt.axis([-2, 2, 0, 300])

		plt.show()


x = TweetAnalyse()

x.loadPolarities()
x.showPolarityHist(x.badPolarities, 'neg', 'Negativos')
x.showPolarityHist(x.goodPolarities, 'pos', 'Positivos')