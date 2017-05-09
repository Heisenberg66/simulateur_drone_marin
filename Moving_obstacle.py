import pymunk
import pygame
import math
from random import randint

# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- Class Moving_obstacle -------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------


class Moving_obstacle(pymunk.Body):


#------------------------------------------------------------- Constructor ----------------------------------------------------------------------
	def __init__(self,sc,posX,posY,rad,space):
		self._mass=1
		self._radius=rad
		self._moment = pymunk.moment_for_circle(self._mass, 0, self._radius)
		self._body = pymunk.Body(self._mass, self._moment)
		self._body.position = posX, posY 
		self._shape = pymunk.Circle(self._body, self._radius) 
		space.add(self._body, self._shape)
		self.p = int(self._shape._body.position.x), 600-int(self._shape._body.position.y)
		self._speed= 100
		self.screen = sc
		direction = pymunk.Vec2d(1, 0).rotated(self._shape.body.angle)
		self._shape.body.velocity = self._speed * direction	


# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- GETTERS / SETTERS -----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------

	def _get_body(self):
		return self._body

	def _get_speed(self):
		return self._speed

	def _set_speed(self,spd):
		self._speed=spd

	def _get_shape(self):
		return self._shape



#------------------------------------------------------------- Fonction draw circle -------------------------------------------------------------

	# dessine un cercle sur la fenetre , situe en dessous du body pygame, il permet au sonar de detecter le cirle car il ne detecte pas le body pymunk 
	# car celui-ci se trouve dans le "space" pymunk et non dans la "fenetre" pygame

	def draw_circle(self):
		self.check_collisison()
		pygame.draw.circle(self.screen,(255,0,0),(int(self._body.position[0]),int(self.screen.get_size()[1]-self._body.position[1])),self._radius,0)


#-------------------------------------------------------------- Fonction check collision --------------------------------------------------------

# verifie que le body est sur l eau 

	def check_collisison(self):
		
		if self.check_collision_in_square():
			self._speed=-100
			rand = randint(0,1)
			if rand == 0:
				self._shape.body.angle+=math.radians(90)
			else:
				self._shape.body.angle+=math.radians(-90)

			self._speed=100	
		

		direction = pymunk.Vec2d(1, 0).rotated(self._shape.body.angle)
		self._shape.body.velocity = self._speed * direction	


#------------------------------------------------------- Focntion check collision square --------------------------------------------------------

# hitbox de l'objet , c est un carre pour simplifie les choses.
# on verifie si un des pixels de carre n'est pas de la couleur de l'eau

	def check_collision_in_square(self):

		i=int(self._body.position[0]-self._radius)
		j=int(self.screen.get_size()[1]-self._body.position[1]-self._radius)
		width = 2*self._radius

		while i<(int(self._body.position[0]-self._radius)+width) and \
		j< (int(self.screen.get_size()[1]-self._body.position[1]-self._radius)+width):
			if self.screen.get_at((i,j)) != (160,211,211,255):
				return True
			i+=1
			j+=1

		return False





#-----------------------------------------------------------------------------------------------------------------------------------------------		
#--------------------------------------------------------------- Property ----------------------------------------------------------------------		
#-----------------------------------------------------------------------------------------------------------------------------------------------		


	body = property (_get_body)
	speed = property (_get_speed,_set_speed)
	shape = property (_get_shape)




