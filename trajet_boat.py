import pygame
from boat import Boat
from markerMap import MarkerMap
import random


# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- Class Trajet_boat -----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------


class Trajet_boat(object):

	# Constructeur
	# 	- screen pygame
	#	- list de waypoint correspondant au trajet
	#	- un boat
	# 	- on memorise la position de depart

	def __init__(self,sc,space,list_waypoint):
		self.screen = sc
		self._listwp = list_waypoint
		self._boat=self.initBoat(sc,space)
		self._position_depart=self.boat.body.position
		del(self._listwp[0])
		self._index=0
		self._boat.shape.color = (255,0,0)

# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- GETTERS / SETTERS -----------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------


	def _get_position_depart(self):
		return self._position_depart

	def _get_boat(self):
		return self._boat

	def _get_listwp(self):
		return self._listwp

	def _get_index(self):
		return self._index

	def _set_index(self,i):
		self._index=i



# ----------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction initBoat
	# creation d'un objet boat
	# vitesse aleatoire
	# diametre aleatoire

	def initBoat(self,sc,space):
		boat = Boat(sc,self._listwp[0].X+15,self.screen.get_size()[1]-self._listwp[0].Y-50,random.randint(5,10),space)
		boat.speed=random.randint(10,20)*10
		boat.maxspeed=boat.speed
		return boat


# ----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction draw_ligne
	# dessine le trajet avec une couleur donnee en parametre

	def draw_ligne(self,color):
		old_wp = MarkerMap(self.boat.body.position[0]-15,self.screen.get_size()[1]-self.boat.body.position[1]-50,None)
		for wp in self._listwp:
			pygame.draw.line(self.screen, color,(old_wp.X+15,old_wp.Y+50) , (wp.X+15,wp.Y+50),4)
			old_wp=wp


# ----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction run


	def run(self):
		
		# draw circle pour la detection avec le sonar
		self._boat.draw_circle()

		# prochain waypoint si on approche du waypoint
		if self._index<len(self._listwp) and abs((self._listwp[self._index].X+15)-self._boat.shape.body.position[0])<3 and \
		abs((self._listwp[self._index].Y+50) - (self.screen.get_size()[1]-self._boat.body.position[1]))<3:
				self._index+=1
				
				

		#si on n est pas au dernier waypoint
		if(self._index<len(self._listwp)):
			self._boat.move_boat(self._listwp,self._index) # deplacement du bateau sur le trajet
			return True

		#si on a fini le parcours
		else:
		#retour du bateau au debut 
			self._boat.body.position = self._position_depart[0],self._position_depart[1]
			self._boat.immobilize_boat()
			return False


#-----------------------------------------------------------------------------------------------------------------------------------------------		
#--------------------------------------------------------------- Property ----------------------------------------------------------------------		
#-----------------------------------------------------------------------------------------------------------------------------------------------		


	position_depart = property (_get_position_depart)
	boat = property (_get_boat)
	listwp = property(_get_listwp)
	index = property(_get_index,_set_index)