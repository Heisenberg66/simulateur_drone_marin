import pygame
from markerMap import MarkerMap
from trajet_boat import Trajet_boat
from init_trajet_boat import Init_trajet_boat
from random import randint


# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- Class Simulation_Bateau -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------


class Simulation_bateau(object):

	# Constructeur
	# 	- screen pygame
	#	- liste des trajets initialises dans la classe Init_trajet_boat (12 au total
	# 	- une liste de couleurs pour l'affichage des trajets en appuyant sur la bar escpace
	# 	- un list vide contenant les trajets en cours 

	# 	au lencement de la simulation, on tire au sort 5 trajets qu'on met dans la liste "trajet_en_cours" 
	# 	la fonction "run" fait evoluer un bateau sur ce trajet 
	# 	un fois le trajet fini, on en choisit un nouveau et on remet le trajet fini dans "list_trajet"

	def __init__(self,sc,space):
		self.screen = sc

		# init de l'object Init_trajet_boat 
		self.init_trajet = Init_trajet_boat()

		# liste contenant les 12 trajets
		self.list_trajet = []

		# ajout des trajet par appel des fonction de la classe Init_trajet_boat
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_1()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_2()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_3()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_4()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_5()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_6()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_7()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_8()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_9()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_10()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_11()))
		self.list_trajet.append(Trajet_boat(self.screen,space,self.init_trajet.init_trajet_12()))


		# liste de couleurs
		self.color = []
		self.color.append((255,0,0))
		self.color.append((0,0,0))
		self.color.append((0,255,0))
		self.color.append((0,0,255))
		self.color.append((255,255,0))
		self.color.append((255,0,255))
		self.color.append((0,255,255))
		self.color.append((255, 51, 153))
		self.color.append((51, 204, 255))
		self.color.append((0, 102, 0))
		self.color.append((102, 0, 204))
		self.color.append((255, 128, 0))


		# liste des trajets en cours
		self.trajet_en_cours = []


	#-----------------------------------------------------------------------------------------------------------------------------------------------

	# dessine les trajets sur la map avec une couleur differente

	def draw_lignes(self):
		i=0
		for trajet in self.list_trajet:
			trajet.draw_ligne(self.color[i])
			i+=1
	

	# ----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction start
	# selectionne 5 trajets , ajoute le bateau correspondant de le space pymunk
	# initialise l'angle de depart du body pymunk

	def start(self):
		for i in range(0,5):
			self.select_trajet()


	# ----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction stop
	# remet les bateaux des trajets en cours a leur position de depart
	# enleve les body pymunk du space
	# on transfert les trajets dans la "list_trajets"

	def stop(self):

		for tb in self.trajet_en_cours:
			tb.boat.body.position = tb.position_depart
			tb.boat.remove_from_space()
			self.list_trajet.append(tb)

		del(self.trajet_en_cours[:])


	# ----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction run
	# si le trajet est terminer, en selectionner un nouveau

	def run(self):
		for tb in self.trajet_en_cours:
			if tb.run() == False:
				
				# supprimmer le body pymunk du space et supprimer le trajet de la list de trajet en cours
				tb.boat.remove_from_space() 
				self.trajet_en_cours.remove(tb)

				# selection d'un nouveau trajet
				self.select_trajet()

				# ajout de l'ancien trajet dans la list de trajets
				self.list_trajet.append(tb)



	#----------------------------------------------------------------------------------------------------------------------------------------------

	# fonction select_trajet
	# selectionne un trajet aleatoire de "list_trajet" et le transfert dans "trajet_en_cours"


	def select_trajet(self):
		rand = randint(0,len(self.list_trajet)-1)
		self.trajet_en_cours.append(self.list_trajet[rand])
		del(self.list_trajet[rand])
		self.trajet_en_cours[-1].boat.add_to_space()
		self.trajet_en_cours[-1].boat.set_angle_to_waypoint(self.trajet_en_cours[-1].listwp[0])



