import time
import numpy as np
from DinamicSpaceFactory import DinamicSpaceFactory
from Finder import Finder
from PriceGetter import PriceGetter

dspEURUSD = DinamicSpaceFactory()
pg = PriceGetter()
i = 0
j = 0
ph = np.zeros( 0 , dtype=float)
goodsCount = 0
badsCount = 0
notFoundCount = 0
while i > -1:
	prices = pg.request()
	print(i, ") prices:", '{:.3f}'.format(prices[0].price), " prognoze point:", (i + dspEURUSD.pointsToResultK * dspEURUSD.points) )
	dspEURUSD.addPoint(prices[0].price)
	prognose = dspEURUSD.getRelativePrognoze()
	prognoseA = dspEURUSD.getAbsolutePrognoze()
	finder = Finder()

	distanses = finder.getDistanses(dspEURUSD.space, dspEURUSD.currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем
	if dspEURUSD.space.size > 0 and  dspEURUSD.space.shape[0] > 3 and distanses.size > 2:
		#print("nearest graf 0:\n",dspEURUSD.space[np.argsort(distanses)[0]] ) #самый похожий график
		#print("nearest graf 1:\n",dspEURUSD.space[np.argsort(distanses)[1]] )
		#print("nearest graf 2:\n",dspEURUSD.space[np.argsort(distanses)[2]] )
		if ph.size > dspEURUSD.pointsToResultK * dspEURUSD.points:
			print("Prognozed: ", ph[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)])
			print("Was: ", dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)])
			if(ph[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] > dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] and 
				prices[0].price > dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)]):
				print("GOOD") 
				goodsCount = goodsCount + 1
			elif(ph[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] < dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] and 
				prices[0].price < dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)]):
				print("GOOD")
				goodsCount = goodsCount + 1
			elif(ph[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] < dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] and 
				prices[0].price > dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)]):
				print("BAD")
				badsCount = badsCount + 1
			elif(ph[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] > dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)] and 
				prices[0].price < dspEURUSD.currentPicture[int(-dspEURUSD.pointsToResultK * dspEURUSD.points)]):
				print("BAD")
				badsCount = badsCount + 1
			else:
				print("CANT FIND")
				notFoundCount = notFoundCount + 1
		print("goods: ",goodsCount, "bads: ", badsCount, "notFounds: ", notFoundCount)
		prognose = dspEURUSD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognose[np.argsort(distanses)[0]], "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) ) #самый похожий график
		print("nearest prognose 1:\n",prognose[np.argsort(distanses)[1]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
		print("nearest prognose 2:\n",prognose[np.argsort(distanses)[2]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
		ph = np.append(ph, prognoseA[np.argsort(distanses)[0]] )
		j = j + 1
	elif dspEURUSD.space.size > 0  and distanses.size > 0:
		print("nearest graf 0:\n",dspEURUSD.space[np.argsort(distanses)[0]] ) #самый похожий график
		prognoses = dspEURUSD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognoses[np.argsort(distanses)[0]] ) #самый похожий график
	else:
		print("Have bad data")
		print("dspEURUSD.space ", dspEURUSD.space)
		print("dspEURUSD.currentPicture: ", dspEURUSD.currentPicture)
	i = i+1
	time.sleep(30)