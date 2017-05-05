import sys
import pygame
import random
import numpy #fonctions mathematiques avancees
import pymunk
import pymunk.pygame_util
from pygame.locals import *
from pygame.locals import FULLSCREEN
from markerMap import MarkerMap
from Button import Button
from boat import Boat


#---------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------ fonction redraw ----------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

#redraw la fenetre avec le fond, les boutons, le marker depart et les waypoint
def redraw():
		redraw_empty()
		#on dessine le trace
		drawligne()

		#draw le marker de depart
		fenetre.blit(depart.image,(depart.X,depart.Y))
		
		# on draw les waypoints 
		for wp in waypointList:
					fenetre.blit(wp.image,(wp.X,wp.Y))

		#on draw le label si jamais on a clique sur un pixel non bleu
		if label_impossible == True:
			fenetre.blit(surface, (400,10))


#---------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------- fonction redraw_empty ---------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

# draw la fenetre avec le fond et les boutons
def redraw_empty():
	fenetre.fill(pygame.Color("white"))
	fenetre.blit(pygame.transform.scale(fond,(1080,680)), (0,0))
	margin = 0
	if b1.check_is_started():
		margin=10
	b1.draw(fenetre,(940,550,130,50), (950+margin,560),50)
	b2.draw(fenetre,(940,610,130,50),(945,620),50)






#--------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------- fonction redraw_simulation--------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------

#draw la fenetre avec le fond, les boutons et le bateau 
def redraw_simulation():
	redraw_empty()
	boat1.draw_arms_sonar()
	space.debug_draw(draw_options)



#---------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------- fonction drawligne -----------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

#dessine les lignes entre les waypoints
def drawligne():
	if len(waypointList) >0:
		old_wp = depart
		for wp in waypointList:
			pygame.draw.line(fenetre, (255,255,153),(old_wp.X+15,old_wp.Y+50) , (wp.X+15,wp.Y+50),4)
			old_wp=wp






#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------ Initialisation -----------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

pygame.init();

#ouverture fenetre

fenetre = pygame.display.set_mode((1080,680))

#background
fond = pygame.image.load("img/mapPortMinimes3.png").convert()
fenetre.blit(pygame.transform.scale(fond,(1080,680)), (0,0))

#titre de la fenetre
pygame.display.set_caption("Simulateur de navigation (Q-learning et neural networks)")

#pymunk space
clock = pygame.time.Clock()
space = pymunk.Space() 
space.gravity = (0.0, 0.0)
draw_options = pymunk.pygame_util.DrawOptions(fenetre)


#marker de depard

marker = pygame.image.load("img/markerDepart.png").convert_alpha()
marker= pygame.transform.scale(marker, (31,50))

depart = MarkerMap(485,450,marker)
fenetre.blit(depart.image,(depart.X,depart.Y))


#marker waypoint

waypoint = pygame.image.load("img/markerWayPoint.png").convert_alpha()
waypoint = pygame.transform.scale(waypoint, (31,50))

#init tableau de waypoint

waypointList = []


#boutons

b1= Button("START")
b1.draw(fenetre,(940,550,130,50), (950,560),50)

b2= Button("CLEAR")
b2.change_default_color((135,206,250))
b2.draw(fenetre,(940,610,130,50),(945,620),50)


#bateau
boat1 = Boat(fenetre,depart.X+15, fenetre.get_size()[1]-depart.Y-50,10,space)
boat1.shape.color = (0,255,0)
boat1.create_arms(30)

#autre variables 

index_list = 0 #index du waypoint destination pendant la simulation


#afficher ou non le texte "marker impossible a placer ici"
label_impossible = False


#refresh ecran
pygame.display.flip()

#---------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- Boucle d'evenements ---------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

while True:
	for event in pygame.event.get():

	#-----------------------------------------------------------------------------------------------------------------------------------------------
	#----------------------------------------------------- Action au clic gauche -------------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------------------
		if event.type == MOUSEBUTTONUP and event.button == 1:


		#-------------------------------------------------------------------------------------------------------------------------------------------
		#---------------------------------------------------- clic sur le bouton "start/stop" ------------------------------------------------------
		#-------------------------------------------------------------------------------------------------------------------------------------------
			#	+changer boolean is_started du bouton
			#	+changer apparence du bouton 
			if b1.obj.collidepoint(event.pos):
				

				#si est lance :  
				#	+retour du bateau a la position de depart
				if b1.check_is_started():
					boat1.body.position = depart.X+15, fenetre.get_size()[1]-depart.Y-50 
					index_list=0
					b1.change_started_bool()
					b1.change_appearance()
					redraw()

				#si la simulaiton n'est pas lance
				#	+initialisation de la vitesse du bateau	
				else:
					boat1.speed=300
					b1.change_started_bool()
					b1.change_appearance()
					redraw_empty()

				
		#-------------------------------------------------------------------------------------------------------------------------------------------
		#----------------------------------------------------------- click sur le bouton "clear" ---------------------------------------------------
		#-------------------------------------------------------------------------------------------------------------------------------------------

			elif b2.obj.collidepoint(event.pos) and b1.check_is_started() == False :
				# vider la liste de waypoint
				del waypointList[:]
				#redessiner
				redraw()
		

		#-------------------------------------------------------------------------------------------------------------------------------------------
		#------------------------------------------------- si le clique n'est pas sur 1 des 2 boutons ----------------------------------------------
		#-------------------------------------------------------------------------------------------------------------------------------------------
			#On ne peut placer un point que si la simulation n'est pas lance
			elif b1.check_is_started() == False:

				#verification que le pixel clique est de couleur bleu/vert (160,211,211) 

					#fonction "get_at(x,y)" permet de recuperer la color et la trnasparence du pixel 
				if fenetre.get_at((event.pos[0], event.pos[1])) == (160,211,211,255):
					
					#si le pixel est bleu , cration d'un nouveau marker + ajout dans la liste
					m=MarkerMap(event.pos[0]-waypoint.get_rect().size[0]/2,event.pos[1]-waypoint.get_rect().size[1],waypoint)
					waypointList.append(m);
					
				else:
					
					#si le pixel n est pas bleu , afficher un message a l ecran
					font = pygame.font.Font(None, 25)
					surface = font.render("Impossible de placer un marker ici !", 1, (255,0,0))
					label_impossible = True

				redraw() #redraw la scene avec le nouveau marker ou le message



	#---------------------------------------------------------------------------------------------------------------------------------------------
	#----------------------------------------------- Action sur le le clic droit de la souris ----------------------------------------------------
	#---------------------------------------------------------------------------------------------------------------------------------------------

		if event.type == MOUSEBUTTONUP and event.button == 3:

			#suppression d'un waypoint au clic droit sur celui-ci

			i=0
			collide = 0

			#parcours des waypoints pour verifier sur les coordonnees sur clic sont en collision avec une marker de la liste 
			while i<len(waypointList) and collide == 0:

				#on transforme l'image du marker en rectangle pour utiliser la fontion "collidepoint((x,y))"
				rect = pygame.Rect(waypointList[i].X , waypointList[i].Y, waypointList[i].image.get_rect().size[0], waypointList[i].image.get_rect().size[1])

				if rect.collidepoint(event.pos[0],event.pos[1]):
					collide=1
					del waypointList[i] #on supprime le marker de la liste
				i=i+1

			#si on a supprime un marker, redraw de la fenetre complete
			if collide == 1:
				redraw()

	#---------------------------------------------------------------------------------------------------------------------------------------------
	#-------------------------------------------------------------------- QUIT -------------------------------------------------------------------
	#---------------------------------------------------------------------------------------------------------------------------------------------
		
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()


#-------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------- SIMULATION ----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
	
	#se lance si on clique sur le bouton start et qu'il y a au moins 1 waypoint dans la liste
	if b1.check_is_started() and len(waypointList)>0:

		if index_list==0:
			boat1.set_angle_to_waypoint(waypointList[index_list])

		#si le bateau approche a 3 pixels de du waypoint, on passe au prochain de la liste
		if index_list<len(waypointList) and abs((waypointList[index_list].X+15)-boat1.shape.body.position[0])<3 and abs((waypointList[index_list].Y+50) - (fenetre.get_size()[1]-boat1.body.position[1]))<3:
			index_list=index_list+1

		#si on n est pas au dernier waypoint
		if(index_list<len(waypointList)):
			
			boat1.move_boat(waypointList,index_list) # pour move boat, whyt not give the entire list and the index 
			space.step(1/100.0)
			pygame.display.flip()	
			clock.tick(100)
			redraw_simulation()
		#si on a fini le parcours
		else:
			#retour du bateau au debut 
			boat1.body.position = depart.X+15, fenetre.get_size()[1]-depart.Y-50
			boat1.immobilize_boat()
			b1.change_started_bool()
			b1.change_appearance()
			redraw()


	label_impossible=False
	pygame.display.flip()	


	continue

#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------

