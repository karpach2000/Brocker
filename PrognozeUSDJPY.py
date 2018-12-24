import time
import numpy as np
from DinamicSpaceFactory import DinamicSpaceFactory
from Finder import Finder
from PriceGetter import PriceGetter

dspUSDJPY = DinamicSpaceFactory()
pg = PriceGetter()
i = 0
j = 0
ph = np.zeros( 0 , dtype=float)
goodsCount = 0
badsCount = 0
notFoundCount = 0
while i > -1:
	prices = pg.request()
	print(i, ") prices:", '{:.3f}'.format(prices[2].price), " prognoze point:", (i + dspUSDJPY.pointsToResultK * dspUSDJPY.points) )
	dspUSDJPY.addPoint(prices[2].price)
	print("dspUSDJPY.currentPicture: ", dspUSDJPY.currentPicture[-1])
	prognose = dspUSDJPY.getRelativePrognoze()
	prognoseA = dspUSDJPY.getAbsolutePrognoze()
	finder = Finder()

	distanses = finder.getDistanses(dspUSDJPY.space, dspUSDJPY.currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем
	if dspUSDJPY.space.size > 0 and  dspUSDJPY.space.shape[0] > 3 and distanses.size > 2:
		#print("nearest graf 0:\n",dspUSDJPY.space[np.argsort(distanses)[0]] ) #самый похожий график
		#print("nearest graf 1:\n",dspUSDJPY.space[np.argsort(distanses)[1]] )
		#print("nearest graf 2:\n",dspUSDJPY.space[np.argsort(distanses)[2]] )
		if ph.size > dspUSDJPY.pointsToResultK * dspUSDJPY.points:
			print("Prognozed: ", ph[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)])
			print("Was: ", dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)])
			if(ph[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] > dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] and 
				prices[0].price > dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)]):
				print("GOOD") 
				goodsCount = goodsCount + 1
			elif(ph[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] < dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] and 
				prices[0].price < dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)]):
				print("GOOD")
				goodsCount = goodsCount + 1
			elif(ph[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] < dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] and 
				prices[0].price > dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)]):
				print("BAD")
				badsCount = badsCount + 1
			elif(ph[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] > dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)] and 
				prices[0].price < dspUSDJPY.currentPicture[int(-dspUSDJPY.pointsToResultK * dspUSDJPY.points)]):
				print("BAD")
				badsCount = badsCount + 1
			else:
				print("CANT FIND")
				notFoundCount = notFoundCount + 1
		print("goods: ",goodsCount, "bads: ", badsCount, "notFounds: ", notFoundCount)
		prognose = dspUSDJPY.getRelativePrognoze()
		print("nearest prognose 0:\n",prognose[np.argsort(distanses)[0]], "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) ) #самый похожий график
		print("nearest prognose 1:\n",prognose[np.argsort(distanses)[1]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
		print("nearest prognose 2:\n",prognose[np.argsort(distanses)[2]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
		ph = np.append(ph, prognoseA[np.argsort(distanses)[0]] )
		j = j + 1
	elif dspUSDJPY.space.size > 0  and distanses.size > 0:
		print("nearest graf 0:\n",dspUSDJPY.space[np.argsort(distanses)[0]] ) #самый похожий график
		prognoses = dspUSDJPY.getRelativePrognoze()
		print("nearest prognose 0:\n",prognoses[np.argsort(distanses)[0]] ) #самый похожий график
	else:
		print("Have bad data")
		print("dspUSDJPY.space ", dspUSDJPY.space)
		print("dspUSDJPY.currentPicture: ", dspUSDJPY.currentPicture)
	i = i+1
	time.sleep(1)
