import numpy as np
from numpy import matrix

class DinamicSpaceFactory():
	"""Generating  space of variants from grafics"""

	points = 100 #колличество точек в графике / мерность пространства
	pointsToResultK = 0.3 #отношение шага для прогноза к мерности пространсва
	maxSpaceSize = 10000
	space = np.zeros((0, self.points + 2), dtype=float)
	cordinate = np.zeros( self.points , dtype=float)
	cordinateI = 0
	currentPicture = np.zeros( self.points , dtype=float)
	_currentPictureFulFlag = 0

	def addPoint(self, point):
		"""Добавить точку"""
		if cordinateI < points - 1:
			cordinate[cordinateI] = point
			cordinateI = cordinateI + 1
			if _currentPictureFulFlag < 1:
				currentPicture[cordinateI] = point
			else:
				currentPicture = np.append(currentPicture, point)
				currentPicture   = np.delete(currentPicture , (0), axis=0)

		elif:
			_currentPictureFulFlag = 1
			cordinate[cordinateI] = point
			cordinateI = 0
			line = self.__normilize(cordinate)
			space = np.concatenate([space, [line]])

		if self.space.shape[1] > maxSpaceSize:
			space  = np.delete(space , (0), axis=0)
			
	def getAbsolutePrognoze(self):
		"""Получает массив прогноззируемых значений графиков -1 если прогноз не возможен"""
		step = int(self.points * self.pointsToResultK )
		prognoze = np.array([])
		i = 0
		while i < self.space.shape[0]:
			endPoint =  i + step 
			if endPoint < self.space.shape[0]:
				#print(space[endPoint, 0])
				prognoze = np.append(prognoze, self.space[endPoint, -3]/self.space[endPoint, -2]+self.space[endPoint, -1])
			else:
				prognoze = np.append(prognoze, -1)
			i=i+1
		return prognoze

	def getRelativePrognoze(self):
		"""Получает массив прогноззируемых значений графиков относительно последней точки исследуемого графика-1 если прогноз не возможен
		Каждой точке в пространстве вариантов соответсвует свой прогноз"""
		step = int(self.points * self.pointsToResultK )
		prognoze = np.array([])
		i = 0
		while i < self.space.shape[0]:
			endPoint =  i + step 
			if endPoint < self.space.shape[0]:
				#print(space[endPoint, 0])
				prognoze = np.append(prognoze, self.space[endPoint, -3]/self.space[endPoint, -2]+self.space[endPoint, -1] - (self.space[i, -3]/self.space[i, -2] + self.space[i, -1]))
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