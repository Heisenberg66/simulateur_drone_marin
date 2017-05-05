import pygame
from math import cos,sin,radians
class Point_sonar(object):

	# Classe Point_sonar

	# Constructeur 
	# 	- Coordonnees du point
	#	- fenetre pygame
	#	- diametre 
	#	- bool : en collision avec un object

	def __init__(self,sc,posX,posY):
		self._X = posX
		self._Y = posY
		self.screen = sc
		self._radius = 2
		self._collide_with_object = False

	# Affichage du point

	def draw_point(self):

		pygame.draw.circle(self.screen, (0,0,0), (int(round(self._X)) ,int(round(self.Y))), self._radius, 0)

	# Getters / Setters

	def _get_X(self):
		return self._X

	def _get_Y(self):
		return self._Y

	def _set_X(self,posX):
		self._X=posX

	def _set_Y(self,posY):
		self._Y=posY

	def _radius(self):
		return self._radius

	def _get_collide_with_object(self):
		return self._collide_with_object

	# Rotation du point autour du point "origin"

	def rotate_point(self,origin,angle):
		    	
		x = self._X - origin[0]
		y = self._Y - origin[1]
		newx = (x*cos(radians(angle))) - (y*sin(radians(angle)))
		newy = (x*sin(radians(-angle))) + (y*cos(radians(-angle)))
		newx += origin[0]
		newy += origin[1]

		self._X=newx
		self._Y=newy

	# Translation du point aux nouvelles coordonnees

	def translate_point(self,x,y):
		self._X=x
		self._Y=y

	

	# Verifie que le pixel est bleu/vert et qu'il est dans la fenetre

	def check_collision(self):

		
		if(self._X>0 and self._Y>0 and self._X<self.screen.get_size()[0] and self._Y<self.screen.get_size()[1] and \
			self.screen.get_at((int(round(self._X)),int(round(self._Y))))!=(160,211,211,255)):
			
			self._collide_with_object=True
		else:
			self._collide_with_object=False


	
	X=property(_get_X,_set_X)
	Y=property(_get_Y,_set_Y)
	radius = property(_radius)
	collide_with_object=property(_get_collide_with_object)
