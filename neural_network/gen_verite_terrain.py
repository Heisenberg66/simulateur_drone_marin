import numpy as np
import pygame

def make_truth(screen,combinaisons):

	
	liste = np.array([9,9,9])
	m=np.array([0,1,0]) # milieu
	g=np.array([1,0,0]) # gauche
	d=np.array([0,0,1]) # droite
	for cb in combinaisons:
		bras_gauche = cb[0:9]
		bras_milieu = cb[10:19]
		bras_droit = cb[20:29]

		if np.sum(bras_gauche) == 1:
			if np.sum(bras_droit) == 1:
				#rester au milieu
				liste = np.vstack((liste,m)).astype(np.float32)
			else:
				liste = np.vstack((liste,d)).astype(np.float32)
		elif np.sum(bras_droit) == 1:
			if np.sum(bras_gauche) == 1:
				liste = np.vstack((liste,m)).astype(np.float32)
			else:
				liste = np.vstack((liste,g)).astype(np.float32)
		elif np.sum(bras_milieu) == 1:
			if np.sum(bras_gauche) == 1:
				liste = np.vstack((liste,d)).astype(np.float32)
			else:
				liste = np.vstack((liste,g)).astype(np.float32)
		else:
			liste = np.vstack((liste,m)).astype(np.float32)
	liste = np.delete(liste, 0, axis=0)

	return liste




