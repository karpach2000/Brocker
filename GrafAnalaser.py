import numpy as np
import math
from math import *

class GrafAnalaser:
	"""Класс предназначен для анализа известного граика и определения выгодности сделки"""
	point = 0.7 
	gistMin = 0.1  #значение гистерезиса при котором нужно рвать сделку
	gistMax = 0.1  #значение гистерезиса при котором сделка считается выгодной

	def getAnalise(self, space, currentArray):
			"""Возвращает массив растояний от нашей точки до всех остальных точек"""
			norm = self.__normilize(array)
			distanses = np.array([])
			i = 0
			while i < space.shape[0]:
				data = space [i]
				deltas = (data - norm) ** 2
				distanse = sqrt(deltas.sum())
				
				distanses = np.append(distanses, distanse)
				i = i +1
			return distanses