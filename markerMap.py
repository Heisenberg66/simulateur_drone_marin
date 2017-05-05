class MarkerMap(object):
	#classe marker contenant les coordonnees des waypoints et l image du marker

	def __init__(self,posX,posY,img):
		self._X=posX
		self._Y=posY
		self._image = img

	def _get_X(self):
		return self._X

	def _get_Y(self):
		return self._Y

	def _set_X(self,posX):
		self._X=posX

	def _set_Y(self,posY):
		self._Y=posY

	def _get_image(self):
		return self._image

	X=property(_get_X,_set_X)
	Y=property(_get_Y,_set_Y)
	image = property (_get_image)