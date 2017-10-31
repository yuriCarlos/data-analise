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

	def showPolarityHists(self, key, title):
		'''Shows a histogram'''

		x0 = [user['means'][key] for user in self.goodPolarities]
		x1 = [user['means'][key] for user in self.badPolarities]

		width = 0.01
		#set up the histogram
		plt.hist(x0, bins=np.arange(min(x0), max(x0) + width, width), alpha=0.3, label='goodVibes')
		plt.hist(x1, bins=np.arange(min(x1), max(x1) + width, width), alpha=0.3, label='darkMind')
		plt.legend(loc='upper right')
		plt.xlabel('Users')
		plt.ylabel('Neg. Polarity')
		plt.title(title)
		plt.axis([-1, 1, 0, 170])

		plt.show()


x = TweetAnalyse()

x.loadPolarities()
x.showPolarityHists('neg', 'Negativos')
x.showPolarityHists('pos', 'Positivo')
x.showPolarityHists('neu', 'Neutro')
x.showPolarityHists('compound', 'compound')
#x.showPolarityHist(x.goodPolarities, 'pos', 'Positivos')