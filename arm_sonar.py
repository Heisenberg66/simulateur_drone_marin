import pygame
from point_sonar import Point_sonar

#----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------- Classe Arm_sonar ---------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------

#classe d un bras du sonar detecteur d obstacle

class Arm_sonar(object):

	# Constructeur : 
	# 	- coordonnees du centre du bateau
	# 	- fenetre pygame
	#	- angle d'orientation du bateau
	#	- distance du premier point par rapport au centre du bateau
	#	- ditance entre les points
	# 	- tableau de points constituant le bras

	def __init__(self,sc,x,y,ab):
		self.X_center_boat = x
		self.Y_center_boat = y
		self.screen = sc
		self.angle_boat= ab
		self.distance_from_boat = 15
		self.distance_between_points = 5
		self.nb_point_arm = 10
		self.points_sonar = []


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

	# Creation du bras
	# 	20 points (radius = 2, couleur = noir) a 15 px du centre et 5px d ecart  

	def create_arm(self):
		
		for i in range(1, self.nb_point_arm+1):
			self.points_sonar.append(Point_sonar(self.screen , self.distance_from_boat +  \
				self.X_center_boat+ (self.distance_between_points * i), self.Y_center_boat))

#----------------------------------------------------------------------------------------------------------------------------------------------------

	# Rotation du bras 
	#	roation point par point par rapport au centre du bateau avec un angle donne 

	def rotate_arm (self,angle):
		for p in self.points_sonar:
			p.rotate_point((self.X_center_boat,self.Y_center_boat),angle)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

	# Translation du bras 
	# 	translation des points du bras vers les nouvelles coordonnees

	def translate_arm(self,X,Y):
		self.X_center_boat=X
		self.Y_center_boat=Y
		i=0
		for p in self.points_sonar:
			p.translate_point(self.distance_from_boat +  \
				self.X_center_boat+ (self.distance_between_points * i),self.Y_center_boat)
			i=i+1

#-----------------------------------------------------------------------------------------------------------------------------------------------------

	# Affichage du bras
	# 	on affiche que si le point est dans la fenetre et ne collide pas avec quelque chose autre que l'eau

	def draw_arm(self):
		
		for p in self.points_sonar:
			p.check_collision()
			if(p.collide_with_object):
				break
			else:
				p.draw_point()


#-----------------------------------------------------------------------------------------------------------------------------------------------------