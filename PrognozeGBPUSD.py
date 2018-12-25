import time
import numpy as np
from DinamicSpaceFactory import DinamicSpaceFactory
from Finder import Finder
from PriceGetter import PriceGetter

dspGBPUSD = DinamicSpaceFactory()
pg = PriceGetter()
i = 0
j = 0
ph = np.zeros( 0 , dtype=float)
goodsCount = 0
badsCount = 0
notFoundCount = 0
while i > -1:
	prices = pg.request()
	print(i, ") prices:", '{:.3f}'.format(prices[1].price), " prognoze point:", (i + dspGBPUSD.pointsToResultK * dspGBPUSD.points) )
	dspGBPUSD.addPoint(prices[1].price)
	print("dspGBPUSD.currentPicture: ", dspGBPUSD.currentPicture[-1])
	prognose = dspGBPUSD.getRelativePrognoze()
	prognoseA = dspGBPUSD.getAbsolutePrognoze()
	finder = Finder()

	distanses = finder.getDistanses(dspGBPUSD.space, dspGBPUSD.currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем
	if dspGBPUSD.space.size > 0 and  dspGBPUSD.space.shape[0] > 3 and distanses.size > 2:
		#print("nearest graf 0:\n",dspGBPUSD.space[np.argsort(distanses)[0]] ) #самый похожий график
		#print("nearest graf 1:\n",dspGBPUSD.space[np.argsort(distanses)[1]] )
		#print("nearest graf 2:\n",dspGBPUSD.space[np.argsort(distanses)[2]] )
		if ph.size > dspGBPUSD.pointsToResultK * dspGBPUSD.points:
			print("Prognozed: ", ph[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)])
			print("Was: ", dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)])
			if(ph[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] > dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] and 
				prices[0].price > dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)]):
				print("GOOD") 
				goodsCount = goodsCount + 1
			elif(ph[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] < dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] and 
				prices[0].price < dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)]):
				print("GOOD")
				goodsCount = goodsCount + 1
			elif(ph[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] < dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] and 
				prices[0].price > dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)]):
				print("BAD")
				badsCount = badsCount + 1
			elif(ph[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] > dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)] and 
				prices[0].price < dspGBPUSD.currentPicture[int(-dspGBPUSD.pointsToResultK * dspGBPUSD.points)]):
				print("BAD")
				badsCount = badsCount + 1
			else:
				print("CANT FIND")
				notFoundCount = notFoundCount + 1
		print("goods: ",goodsCount, "bads: ", badsCount, "notFounds: ", notFoundCount)
		prognose = dspGBPUSD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognose[np.argsort(distanses)[0]], "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) ) #самый похожий график
		print("nearest prognose 1:\n",prognose[np.argsort(distanses)[1]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[1]]) )
		print("nearest prognose 2:\n",prognose[np.argsort(distanses)[2]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[2]]) )
		ph = np.append(ph, prognoseA[np.argsort(distanses)[0]] )
		j = j + 1
	elif dspGBPUSD.space.size > 0  and distanses.size > 0:
		print("nearest graf 0:\n",dspGBPUSD.space[np.argsort(distanses)[0]] ) #самый похожий график
		prognoses = dspGBPUSD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognoses[np.argsort(distanses)[0]] ) #самый похожий график
	else:
		print("Have bad data")
		print("dspGBPUSD.space ", dspGBPUSD.space)
		print("dspGBPUSD.currentPicture: ", dspGBPUSD.currentPicture)
	i = i+1
	time.sleep(1)
