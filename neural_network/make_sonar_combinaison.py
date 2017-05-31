import numpy as np
import pygame

def make_combinaisons(screen):

	liste = np.array([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]) # rajouter un 9 pour la vitesse
	
	# for speed in range(100,300):
	# 	sp = speed

	for i in range(-1,10):
		liste1 = np.array([0,0,0,0,0,0,0,0,0,0])
		if i != -1:
			liste1[i] = 1

		for j in range(-1,10):
			liste2 = np.array([0,0,0,0,0,0,0,0,0,0])
			if j != -1:
				liste2[j] = 1

			for z in range(-1,10):
				liste3 = np.array([0,0,0,0,0,0,0,0,0,0])
				if z != -1:
					liste3[z]=1
				liste_concat =np.concatenate((liste1,liste2,liste3), axis=0)
				# liste_finale = np.hstack([sp, liste_concat])
				liste = np.vstack((liste,liste_concat)).astype(np.float32) # change liste_concat to list_finale
	liste = np.delete(liste, 0, axis=0)


	return liste




