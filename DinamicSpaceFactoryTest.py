import time
import numpy as np
from DinamicSpaceFactory import DinamicSpaceFactory
from Finder import Finder
from PriceGetter import PriceGetter

dspEURUSD = DinamicSpaceFactory()
pg = PriceGetter()
i = 0
while i > -1:
	prices = pg.request()
	print(i, ") prices:", prices[0].price, ") prognoze point:", (i + dspEURUSD.pointsToResultK*dspEURUSD.points) )
	dspEURUSD.addPoint(prices[0].price)
	prognose = dspEURUSD.getRelativePrognoze()
	finder = Finder()
	distanses = finder.getDistanses(dspEURUSD.space, dspEURUSD.currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем
	if dspEURUSD.space.size > 0 and  dspEURUSD.space.shape[0] > 3:
		print("nearest graf 0:\n",dspEURUSD.space[np.argsort(distanses)[0]] ) #самый похожий график
		print("nearest graf 1:\n",dspEURUSD.space[np.argsort(distanses)[1]] )
		print("nearest graf 2:\n",dspEURUSD.space[np.argsort(distanses)[2]] )
		prognose = dspEURUSD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognose[np.argsort(distanses)[0]] ) #самый похожий график
		print("nearest prognose 1:\n",prognose[np.argsort(distanses)[1]] )
		print("nearest prognose 2:\n",prognose[np.argsort(distanses)[2]] )
	elif dspEURUSD.space.size > 0:
		print("nearest graf 0:\n",dspEURUSD.space[np.argsort(distanses)[0]] ) #самый похожий график
		prognoses = dspEURUSD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognoses[np.argsort(distanses)[0]] ) #самый похожий график
	else:
		print("Have bad data")
		print("dspEURUSD.space ", dspEURUSD.space)
		print("dspEURUSD.currentPicture: ", dspEURUSD.currentPicture)
	i = i+1
	time.sleep(30)