import numpy as np
from numpy import matrix

class DinamicSpaceFactory():
	"""Generating  space of variants from grafics"""

	points = 30 #колличество точек в графике / мерность пространства
	pointsToResultK = 0.3 #отношение шага для прогноза к мерности пространсва
	maxSpaceSize = 10000
	space = np.zeros((0, points + 2), dtype=float)
	cordinate = np.zeros( points , dtype=float)
	cordinateI = 0
	currentPicture = np.zeros( points , dtype=float)
	_currentPictureFulFlag = 0

	def addPoint(self, point):
		"""Добавить точку"""
		if self._currentPictureFulFlag < 1:
				self.currentPicture[self.cordinateI] = point
		else:
				self.currentPicture = np.append(self.currentPicture, point)
				self.currentPicture   = np.delete(self.currentPicture , (0), axis=0)

		if self.cordinateI < self.points -1 :
			self.cordinate[self.cordinateI] = point
			self.cordinateI = self.cordinateI + 1
		else:
			self._currentPictureFulFlag = 1
			self.cordinate[self.cordinateI] = point
			self.cordinateI = 0

		if self._currentPictureFulFlag > 0:
			line = self.__normilize(self.cordinate)
			self.space = np.concatenate([self.space, [line]])

		if self._currentPictureFulFlag > 0:
			line = self.__normilize(self.cordinate)
			self.space = np.concatenate([self.space, [line]])

		if self.space.shape[1] > self.maxSpaceSize:
			self.space  = np.delete(self.space , (0), axis=0)
			
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
				prognoze = np.append(prognoze, self.space[endPoint, -3]/self.space[endPoint, -2]+self.space[endPoint, -1] / (self.space[i, -3]/self.space[i, -2] + self.space[i, -1]))
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
		if delta != 0:
			k = 1/delta
		else:
			k = 1.0
		array = (array-b)*k
		array = np.concatenate([array, [k]])
		array = np.concatenate([array, [b]])
		return array