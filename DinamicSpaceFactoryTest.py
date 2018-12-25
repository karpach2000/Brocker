import time
import numpy as np
import pandas as pd
from DinamicSpaceFactory import DinamicSpaceFactory
from Finder import Finder
from PriceGetter import PriceGetter



class Present():
	#curentPoint = 10
	def __init__(self):
		self.tipe = "EURUSD"
		self.price = 1.2
		self.prognose1 = 1.3
		self.prognose2 = 1.3
		self.prognose3 = 1.3
		#prognosePoint = 20
		self.lastPrice = 0.9
		self.prognosed = 1.0
		self.result = "GOOD"
		self.goods = 0
		self.bads = 0
		self.nfs = 0

	def printIt(self):
		print(self.tipe)
		print("    price: ", self.price, " prognoze: ", self.prognose1)
		print("lastPrice: ", self.lastPrice, " prognosed: ", self.prognosed, " price: ", self.price, " ", self.result )
		print("goods: ", self.goods, " bads: ", self.bads, " nfs: ", self.nfs)


pg = PriceGetter()
finder = Finder()
presents = np.zeros(0,dtype= Present)
dsps = np.zeros(0, dtype = DinamicSpaceFactory)

#создаем фабрики пространств для каждой валюты и выводилки результатов 
for p in pg.request():
	d = DinamicSpaceFactory()
	dsps = np.append(dsps, d)
	presents = np.append(presents, Present())


i = 0
while i > -1:
	k = 0
	prices = pg.request()

	print("\n........................................................................................")
	print("\n........................................................................................")
	print("\n\nITERATION ", i)
	while k <  dsps.size:
		#print(i, ") prices:", '{:.3f}'.format(prices[k].price), " prognoze point:", (i + dsp.pointsToResultK * dsp.points) )
		#генерим требуемые нам переменные
		print("__________________________________________________________________________________________")
		distanseToPrognoze = int(-dsps[k].pointsToResultK * dsps[k].points) #прогноз до текущей точки 

		#Заполняем форму отчета
		presents[k].tipe = prices[k].priceName
		presents[k].price = prices[k].price

		#генерим многомерное пространство и прогнозы
		dsps[k].addPoint(prices[k].price)


		#ищем совпадения
		distanses = finder.getDistanses(dsps[k].space, dsps[k].currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем


		if dsps[k].space.size > 0 and  dsps[k].space.shape[0] > 3 and distanses.size > 2: #проверяем достаточно ли у меня данных для каких либо выводов
			if dsps[k].ph.size > dsps[k].pointsToResultK * dsps[k].points:

				#заполняем форму отчета
				presents[k].prognosed = dsps[k].ph[distanseToPrognoze]
				presents[k].lastPrice = dsps[k].currentPicture[distanseToPrognoze]
				
				#смотрим сбылся ли прогноз и двигаем счетчики
				if(dsps[k].ph[distanseToPrognoze] > dsps[k].currentPicture[distanseToPrognoze] and 
					prices[0].price > dsps[k].currentPicture[distanseToPrognoze]):
					presents[k].result = "GOOD" 
					presents[k].goods = presents[k].goods + 1
				elif(dsps[k].ph[distanseToPrognoze] < dsps[k].currentPicture[distanseToPrognoze] and 
					prices[0].price < dsps[k].currentPicture[distanseToPrognoze]):
					presents[k].result = "GOOD" 
					presents[k].goods = presents[k].goods + 1
				elif(dsps[k].ph[distanseToPrognoze] < dsps[k].currentPicture[distanseToPrognoze] and 
					prices[0].price > dsps[k].currentPicture[distanseToPrognoze]):
					presents[k].result = "BAD" 
					presents[k].bads = presents[k].bads + 1
				elif(dsps[k].ph[distanseToPrognoze] > dsps[k].currentPicture[distanseToPrognoze] and 
					prices[0].price < dsps[k].currentPicture[distanseToPrognoze]):
					presents[k].result = "BAD" 
					presents[k].bads = presents[k].bads + 1
				else:
					presents[k].result = "CANT FIND" 
					presents[k].nfs = presents[k].nfs + 1
			#Прогнозируем
			prognose = dsps[k].getRelativePrognoze()
			prognoseA = dsps[k].getAbsolutePrognoze()
			#print(distanses)
			presents[k].prognose1 = prognoseA[np.argsort(distanses)[0]]
			presents[k].prognose2 = prognoseA[np.argsort(distanses)[1]]
			presents[k].prognose3 = prognoseA[np.argsort(distanses)[2]]
			#print("nearest prognose 0:\n",prognose[np.argsort(distanses)[0]], "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) ) #самый похожий график
			#print("nearest prognose 1:\n",prognose[np.argsort(distanses)[1]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
			#print("nearest prognose 2:\n",prognose[np.argsort(distanses)[2]] , "   ", '{:.3f}'.format(prognoseA[np.argsort(distanses)[0]]) )
			dsps[k].ph = np.append(dsps[k].ph, prognoseA[np.argsort(distanses)[0]] )
			presents[k].printIt()
			#print(k)
		elif dsps[k].space.size > 0  and distanses.size > 0:
			print(presents[k].tipe, ": ", dsps[k].currentPicture) #самый похожий график
			prognoses = dsps[k].getRelativePrognoze()
		else:
			print("Have bad data ", prices[k].price)
			print(presents[k].tipe, ": ", dsps[k].currentPicture) #самый похожий график
		k = k +1
	i = i+1
	
	time.sleep(6)



