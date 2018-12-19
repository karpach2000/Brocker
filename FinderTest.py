import numpy as np
from MySpaceFactory import MySpaceFactory
from Finder import Finder

L = np.array(range(20)) #график для обучения
want = np.array([9, 10, 11, 12]) #график похожий на который мы ищем
msf = MySpaceFactory() 
space = msf.generateSpace(L) #расположение графиков в пространсве вариантов
finder = Finder()
distanses = finder.getDistanses(space, want) #Расстояния от точек в пространстве вариантов до графика который мы ищем
print("distanses:           ",  distanses)
print("min distanse:        ",  np.min(distanses)) 
#Распечатаем 3 самых похожих графика.
print("nearest graf 0:\n",space[np.argsort(distanses)[0]] ) #самый похожий график
print("nearest graf 1:\n",space[np.argsort(distanses)[1]] )
print("nearest graf 2:\n",space[np.argsort(distanses)[2]] )
#Произведем прогноз
prognose = msf.getRelativePrognoze(space)
print(prognose)
