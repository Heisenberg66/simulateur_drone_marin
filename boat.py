import pymunk
import numpy
import pygame
from math import degrees,radians,sqrt
from arm_sonar import Arm_sonar
from neural_network.make_sonar_combinaison import make_combinaisons
from neural_network.gen_verite_terrain import make_truth
from neural_network.neural_network import Neural_network

# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- Class Boat ------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------


class Boat(pymunk.Body):

	# Constructeur
	# - mass du body pymunk
	# - diametre
	# - inertie
	# - coordonnees
	# - vitesse
	# - liste de Arm_sonar 
	# - fenetre pygame

	def __init__(self,sc,posX,posY,rad,spc):
		self._mass=1
		self._radius=rad
		self._moment = pymunk.moment_for_circle(self._mass, 0, self._radius)
		self._body = pymunk.Body(self._mass, self._moment)
		self._body.position = posX, posY 
		self._shape = pymunk.Circle(self._body, self._radius) 
		self.p = int(self._shape._body.position.x), 600-int(self._shape._body.position.y)
		self._speed= 100
		self.arms_sonar = []
		self.screen=sc
		self.angle_arms = 0
		self._space=spc
		self._maxspeed=300


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

	def _set_maxspeed(self,ms):
		self._maxspeed=ms

	def _get_maxspeed(self):
		return self._maxspeed


# ----------------------------------------------------------------------------------------------------------------------------------------------

	def add_to_space(self):
		self.space.add(self._body,self._shape)

# ----------------------------------------------------------------------------------------------------------------------------------------------

	def remove_from_space(self):
		self.space.remove(self._body,self._shape)


# ----------------------------------------------------------------------------------------------------------------------------------------------

	# Deplace le bateau dans un direction 

	def move_boat(self, wplist,index):
		
		#rotation progressive du bateau 

		#angle pour atteindre le prochain point
		agl = -numpy.arctan2(((wplist[index].Y+50)-(self.screen.get_size()[1]-self.body.position[1])),((wplist[index].X+15)-(self.body.position[0])))
		agl = round(agl,1)


		#reset des angles si on depasse 3.15 ou -3.15
		if self._shape.body.angle >= 3.15:
			self._shape.body.angle = -3.1
		elif self._shape.body.angle <= -3.15:
			self._shape.body.angle = 3.1


		#precision a 0.1
		if abs(self._shape.body.angle - abs(agl)) > 0:
		

			# angle > 0 donc le bateau se dirige vers le haut
			if self._shape.body.angle > 0:

				if (agl >= 0 and agl < self._shape.body.angle) or (agl < 0 and agl > (-3.14+self._shape.body.angle)):
					# tribord
					self._shape.body.angle -= 0.1
				else:
					# babord
					self._shape.body.angle += 0.1

			# angle < 0 donc le bateau se dirige vers le bas 
			else:

				if (agl<=0 and agl>= self._shape.body.angle) or (agl >= 0 and agl< (3.14 + self._shape.body.angle)):
					# tribord
					self._shape.body.angle += 0.1
				else:
					# babord
					self._shape.body.angle -= 0.1



		#ajustement de la vitesse en fonction de l'angle
		self._speed += self.adjust_speed(wplist,index)
		

		#maj des caracteristiques du bateau (direction , velocity)
		self._shape.body.angle = round(self._shape.body.angle,1)
		direction = pymunk.Vec2d(1, 0).rotated(self._shape.body.angle)
		self._shape.body.velocity = self._speed * direction		
		
# ----------------------------------------------------------------------------------------------------------------------------------------------

	#oriente le bateau directement vers l'angle qu'on calcul

	def set_angle_to_waypoint(self,point):
		#calcul de l'angle entre la position du "boat" et la position de la destination
		agl = -numpy.arctan2(((point.Y+50)-(self.screen.get_size()[1]-self.body.position[1])),((point.X+15)-(self.body.position[0])))
		#update l'angle
		self._shape.body.angle = round(agl,1)
		direction = pymunk.Vec2d(1, 0).rotated(self._shape.body.angle)

# ----------------------------------------------------------------------------------------------------------------------------------------------

	# immobilise le bateau 

	def immobilize_boat(self):
		self._speed=0
		direction = pymunk.Vec2d(1, 0).rotated(self._shape.body.angle)
		self._shape.body.velocity = self._speed * direction

# ----------------------------------------------------------------------------------------------------------------------------------------------

	# creation des bras du sonar 

	def create_arms(self,angle):
		#\    |    /
		# \   |   /
		#  \  |  /
		#   \ | /
		#    \|/
		#    ___
		#   / | \
		#  (     )
		#   \___/

		# possibilite de creer un sonar avec 3 "bras"

		self.arms_sonar.append(Arm_sonar(self.screen,self._body.position[0],self.screen.get_size()[1]-self._body.position[1],0))
		self.arms_sonar.append(Arm_sonar(self.screen,self._body.position[0],self.screen.get_size()[1]-self._body.position[1],0))
		self.arms_sonar.append(Arm_sonar(self.screen,self._body.position[0],self.screen.get_size()[1]-self._body.position[1],0))

		for arm in self.arms_sonar:
			arm.create_arm()


		# rotation des bras droit et gauche
		self.angle_arms = 30
		self.rotate_left_right(self.angle_arms)

# ----------------------------------------------------------------------------------------------------------------------------------------------

	# Affichage des bras 

	def draw_arms_sonar(self):

		for arm in self.arms_sonar:

			arm.translate_arm(self._body.position[0],self.screen.get_size()[1]-self._body.position[1])
			self.rotate_left_right(self.angle_arms)
			arm.draw_arm()


# ----------------------------------------------------------------------------------------------------------------------------------------------

	# Rotation des bras droit et gauche 
	# 	le bras au centre garde le meme angle que le bateau 

	def rotate_left_right(self,angle):
		self.arms_sonar[0].rotate_arm(degrees(self._shape.body.angle)+angle)
		self.arms_sonar[1].rotate_arm(degrees(self._shape.body.angle))
		self.arms_sonar[2].rotate_arm(degrees(self._shape.body.angle)-angle)


# ----------------------------------------------------------------------------------------------------------------------------------------------

	# renvoie la distance entre 2 points

	def distance_between_point(self,point):
		return sqrt(pow(point.Y-(self.screen.get_size()[1]-self._body.position[1]-50),2)+pow(point.X-(self._body.position[0]-15),2))

	#distance entre la position du bateau et l'arrive

	def distance_to_finish(self,waypointList,index):
		distance=0
		for i in (index,len(waypointList)-1):
			distance += self.distance_between_point(waypointList[i])

		return distance



# ----------------------------------------------------------------------------------------------------------------------------------------------
	
	# angle du point donne en parametre
		
	def angle_to_point(self,point):
		return -numpy.arctan2(((point.Y+50)-(self.screen.get_size()[1]-self.body.position[1])),((point.X+15)-(self.body.position[0])))


# ----------------------------------------------------------------------------------------------------------------------------------------------

	# angle entre l'angle courant et l'angle donne en parametre

	def difference_angle(self,angle):
		# diff angle 
		agl_diff_from_0 = abs(angle)
		agl_diff_from_pi = 3.14 - abs(angle)

		#diff slef.shape.body.angle

		angle_diff_from_0=abs(self._shape.body.angle)
		angle_diff_from_pi = 3.14 - abs(self._shape.body.angle)

		if (angle>=0 and self._shape.body.angle>=0) or (angle <0 and self._shape.body.angle<0):
			return abs(angle_diff_from_0-agl_diff_from_0)
		elif (angle_diff_from_0+agl_diff_from_0)<(angle_diff_from_pi+agl_diff_from_pi):
			return abs(angle_diff_from_0+agl_diff_from_0)
		else:
			return abs(angle_diff_from_pi+agl_diff_from_pi)





# ----------------------------------------------------------------------------------------------------------------------------------------------

	#ajustement de la vitesse du bateau en fonction de l'angle et la distance du prochain point 

	def adjust_speed (self, wplist, index):

		#distance jusqu'au prochain wp, distance jusqu'au finish, angle 
		distance_to_point = self.distance_between_point(wplist[index])
		distance_until_finish = self.distance_to_finish(wplist,index)

		if(distance_until_finish<100 and distance_until_finish>20 and self.speed>50):
			return -10
		
		elif(self._speed > 80 and distance_to_point <= 50 and index<len(wplist)-1):
			difference_angle = self.difference_angle(self.angle_to_point(wplist[index+1]))
			if difference_angle<= radians(45):
				return 0
			elif difference_angle <= radians (90):
				return -5
			elif difference_angle <= radians(135):
				return -10
			else:
				return -15
		
		elif(self._speed<self._maxspeed and index> 0 and self.distance_between_point(wplist[index-1])>10):
			return 20
		
		else:
			return 0


# --------------------------------------------------------------------------------------------------------------------------------------------------

# dessine un cercle au meme coordonnees que le body pymunk, util pour le sonar (detection des pixels )
	def draw_circle (self):
		pygame.draw.circle(self.screen,(255,0,0),(int(self._body.position[0]),int(self.screen.get_size()[1]-self._body.position[1])),self._radius,0)



# --------------------------------------------------------------------------------------------------------------------------------------------------

# creation et entrainement du reseau de neurones a partir des combinaison et de la verite terrain 
	def init_nn(self):
		combi  = make_combinaisons(self.screen)

		self.nn= Neural_network(self.screen,combi,make_truth(self.screen,combi))

		self.nn.setup_network()

		self.nn.train_network()

	def a(self):
		lol = make_combinaisons(self.screen)

#-----------------------------------------------------------------------------------------------------------------------------------------------		
#--------------------------------------------------------------- Property ----------------------------------------------------------------------		
#-----------------------------------------------------------------------------------------------------------------------------------------------		


	body = property (_get_body)
	speed = property (_get_speed,_set_speed)
	shape = property (_get_shape)
	maxspeed = property(_get_maxspeed,_set_maxspeed)


