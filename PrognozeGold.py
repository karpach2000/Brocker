import time
import numpy as np
from DinamicSpaceFactory import DinamicSpaceFactory
from Finder import Finder
from PriceGetter import PriceGetter

dspGOLD = DinamicSpaceFactory()
pg = PriceGetter()
i = 0
j = 0
ph = np.zeros( 0 , dtype=float)
goodsCount = 0
badsCount = 0
notFoundCount = 0
while i > -1:
	prices = pg.request()
	print(i, ") prices:", '{:.3f}'.format(prices[9].price), " prognoze point:", (i + dspGOLD.pointsToResultK * dspGOLD.points) )
	dspGOLD.addPoint(prices[9].price)
	print("dspGOLD.currentPicture: ", dspGOLD.currentPicture[-1])
	prognose = dspGOLD.getRelativePrognoze()
	prognoseA = dspGOLD.getAbsolutePrognoze()
	finder = Finder()

	distanses = finder.getDistanses(dspGOLD.space, dspGOLD.currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем
	if dspGOLD.space.size > 0 and  dspGOLD.space.shape[0] > 3 and distanses.size > 2:
		#print("nearest graf 0:\n",dspGOLD.space[np.argsort(distanses)[0]] ) #самый похожий график
		#print("nearest graf 1:\n",dspGOLD.space[np.argsort(distanses)[1]] )
		#print("nearest graf 2:\n",dspGOLD.space[np.argsort(distanses)[2]] )
		if ph.size > dspGOLD.pointsToResultK * dspGOLD.points:
			print("Prognozed: ", ph[int(-dspGOLD.pointsToResultK * dspGOLD.points)])
			print("Was: ", dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)])
			if(ph[int(-dspGOLD.pointsToResultK * dspGOLD.points)] > dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)] and 
				prices[0].price > dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)]):
				print("GOOD") 
				goodsCount = goodsCount + 1
			elif(ph[int(-dspGOLD.pointsToResultK * dspGOLD.points)] < dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)] and 
				prices[0].price < dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)]):
				print("GOOD")
				goodsCount = goodsCount + 1
			elif(ph[int(-dspGOLD.pointsToResultK * dspGOLD.points)] < dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)] and 
				prices[0].price > dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)]):
				print("BAD")
				badsCount = badsCount + 1
			elif(ph[int(-dspGOLD.pointsToResultK * dspGOLD.points)] > dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)] and 
				prices[0].price < dspGOLD.currentPicture[int(-dspGOLD.pointsToResultK * dspGOLD.points)]):
				print("BAD")
				badsCount = badsCount + 1
			else:
				print("CANT FIND")
				notFoundCount = notFoundCount + 1
		print("goods: ",goodsCount, "bads: ", badsCount, "notFounds: ", notFoundCount)
		prognose = dspGOLD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognose[np.argsort(distanses)[0]], "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) ) #самый похожий график
		print("nearest prognose 1:\n",prognose[np.argsort(distanses)[1]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
		print("nearest prognose 2:\n",prognose[np.argsort(distanses)[2]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
		ph = np.append(ph, prognoseA[np.argsort(distanses)[0]] )
		j = j + 1
	elif dspGOLD.space.size > 0  and distanses.size > 0:
		print("nearest graf 0:\n",dspGOLD.space[np.argsort(distanses)[0]] ) #самый похожий график
		prognoses = dspGOLD.getRelativePrognoze()
		print("nearest prognose 0:\n",prognoses[np.argsort(distanses)[0]] ) #самый похожий график
	else:
		print("Have bad data")
		print("dspGOLD.space ", dspGOLD.space)
		print("dspGOLD.currentPicture: ", dspGOLD.currentPicture)
	i = i+1
	time.sleep(1)
