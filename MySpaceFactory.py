import numpy as np
from numpy import matrix

class MySpaceFactory():
	"""Generating  space of variants from grafics"""

	points = 4 #колличество точек в графике / мерность пространства
	pointsToResultK = 0.3 #отношение шага для прогноза к мерности пространсва


	def generateSpace(self, array):
		"""Генерирует точки в пространсве вариантов из графиков"""
		space = np.zeros((0, self.points + 2), dtype=float)
		i = self.points
		while i < array.size:
			j = i-self.points
			ar = array[j:i]
			aMin = np.min(ar)
			aMax = np.max(ar)
			# space = np.append([space], [[a]])
			line = self.__normilize(ar)
			space = np.concatenate([space, [line]])
			i = i + 1
		return space

	def getAbsolutePrognoze(self, space):
		"""Получает массив прогноззируемых значений графиков -1 если прогноз не возможен"""
		step = int(self.points * self.pointsToResultK )
		prognoze = np.array([])
		i = 0
		while i < space.shape[0]:
			endPoint =  i + step 
			if endPoint < space.shape[0]:
				#print(space[endPoint, 0])
				prognoze = np.append(prognoze, space[endPoint, -3]/space[endPoint, -2]+space[endPoint, -1])
			else:
				prognoze = np.append(prognoze, -1)
			i=i+1
		return prognoze

	def getRelativePrognoze(self, space):
		"""Получает массив прогноззируемых значений графиков относительно последней точки исследуемого графика-1 если прогноз не возможен"""
		step = int(self.points * self.pointsToResultK )
		prognoze = np.array([])
		i = 0
		while i < space.shape[0]:
			endPoint =  i + step 
			if endPoint < space.shape[0]:
				#print(space[endPoint, 0])
				prognoze = np.append(prognoze, space[endPoint, -3]/space[endPoint, -2]+space[endPoint, -1] - (space[i, -3]/space[i, -2]+space[i, -1]))
			else:
				prognoze = np.append(prognoze, -1)
			i=i+1
		return prognoze



	def __normilize(self, array):
		"""Приводит текущую точку к нормальному виду и добавляет переменные приведения"""
		aMin = np.min(array)
		aMax = np.max(array)
		delta = aMax - aMin
		b = aMin
		k = 1/delta
		array = (array-b)*k
		array = np.concatenate([array, [k]])
		array = np.concatenate([array, [b]])
		return array
		


