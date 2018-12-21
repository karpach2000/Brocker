import numpy as np
import math
from math import *

class Finder:

		history = 31 #количество последних точек не учавствующих в выборке
		"""Класс ищет ближаййшие варианты в пространстве вариантов, похожие на заданный вариант"""
		def getDistanses(self, space, array):
			"""Возвращает массив растояний от нашей точки до всех остальных точек"""
			norm = self.__normilize(array)
			distanses = np.array([])
			i = 0
			if space.shape[0] > self.history:
				while i < space.shape[0] - self.history:
					data = space [i]
					deltas = (data - norm) ** 2
					distanse = sqrt(deltas.sum())
					
					distanses = np.append(distanses, distanse)
					i = i +1
				return distanses
			else:
				return distanses


		def getSortedSpace(self, space, array):
			"""Возвращает массив точек в пространстве вариантов
			последняя точка в строке - удаление от искомой точки"""
			distanses = self.getDistanses(space, array)
			distanses = distanses.reshape((distanses.size, 1))
			numSpace = np.concatenate([space, distanses], axis = 1)
			return numSpace

		def __normilize(self, array):
			"""Приводит текущую точку к нормальному виду и добавляет переменные приведения"""
			aMin = np.min(array)
			aMax = np.max(array)
			delta = aMax - aMin
			b = aMin
			if delta != 0:
				k = 1/delta
			else:
				k = 1.0
			array = (array-b)*k
			array = np.concatenate([array, [k]])
			array = np.concatenate([array, [b]])
			return array