import numpy as np
from DinamicSpaceFactory import DinamicSpaceFactory
dspEURUSD = DinamicSpaceFactory()
from PriceGetter import PriceGetter
pg = PriceGetter()
prices = pg.request()
dspEURUSD.addPoint(prices[0].price)
prognose = dspEURUSD.getRelativePrognoze()
finder = Finder()
distanses = finder.getDistanses(dspEURUSD.space, dspEURUSD.currentPicture) #Расстояния от точек в пространстве вариантов до графика который мы ищем
distanses.#Распечатаем 3 самых похожих графика.
print("nearest graf 0:\n",space[dspEURUSD.argsort(distanses)[0]] ) #самый похожий график
print("nearest graf 1:\n",space[dspEURUSD.argsort(distanses)[1]] )
print("nearest graf 2:\n",space[dspEURUSD.argsort(distanses)[2]] )