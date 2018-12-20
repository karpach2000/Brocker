import urllib.request
import numpy as np
import json
class PriceGetter():
	"""При помощи Гет запроса получаем курсы валют"""
	url = 'https://quotes.instaforex.com/api/quotesTick?m=json'

	def request(self):
		"""Запросить курсы валют"""
		response = urllib.request.urlopen(self.url)
		text = response.read()
		data = json.loads(text)
		array = np.zeros(0, dtype = Price)
		for d in data:
			p = Price()
			p.priceName = d['symbol']
			p.priceSell = d['bid']
			p.priceBuy = d['ask']
			p.price = (p.priceSell + p.priceBuy)/2
			#print(p.toString())
			array =  np.append(array, p)
		return array

class Price:
	"""Представляет текущий курс валют"""
	priceName = 'EURUSD'
	price = 30
	priceSell = 29
	priceBuy = 31	

	def toString(self):
		return self.priceName +" "+'{:.3f}'.format(self.price) +" "+'{:.3f}'.format(self.priceSell) +" "+'{:.3f}'.format(self.priceBuy)