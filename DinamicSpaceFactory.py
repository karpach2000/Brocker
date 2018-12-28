import numpy as np
from numpy import matrix

class DinamicSpaceFactory:
	"""Generating  space of variants from grafics"""

	def __init__(self):
		self.points = 75 #колличество точек в графике / мерность пространства
		self.pointsToResultK = 0.1 #отношение шага для прогноза к мерности пространсва
		self.maxSpaceSize = 900000
		self.space = np.zeros((0, self.points + 2), dtype=float)
		self.cordinate = np.zeros( self.points , dtype=float)
		self.cordinateI = 0
		self.currentPicture = np.zeros( self.points , dtype=float)
		self._currentPictureFulFlag = 0
		self.ph = np.zeros( 0 , dtype=float)

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

	def isCurentPictureLie(self):
		a = self.currentPicture[0]
		for cp in self.currentPicture:
			if a != cp:
				return False
			a = cp
		return True



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