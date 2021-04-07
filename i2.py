#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Structure pygame
"""

#--------- importations -----------#

import pygame               # importation de pygame dans un espace propre
from pygame.locals import * # importation des constantes de pygame dans l'espace global 


#--------- fonctions -----------#







#--------- partie principale -----------#

pygame.init()  # lancement de pygame


# dimensions de la fenetre :
largeur = 450 # largeur en pixels
hauteur = 650 # hauteur en pixels
dec_abs=50
dec_ord=50

#toujours encadrer vos programmes pygame par try et finally ce qui permet de
# fermer correctement la fenêtre pygame en cas d'erreur
try:
    fenetre = pygame.display.set_mode((largeur,hauteur))
    
    for i in range(0,7):
        for j in range(0,7):
            pygame.draw.rect(fenetre,(255,255,255),(dec_abs+25+50*i,dec_ord+50*j,25,25))
    for i in range(0,7):
        for j in range(0,7):        
            pygame.draw.rect(fenetre,(255,255,255),(dec_abs+50*i,dec_ord+25+50*j,25,25))
    for i in range(0,7):
        for j in range(0,7):        
            pygame.draw.rect(fenetre,(0,0,255),(dec_abs+50*i,dec_ord+50*j,25,25))
    for i in range(0,7):
        for j in range(0,7):
            pygame.draw.rect(fenetre,(0,0,255),(dec_abs+25+50*i,dec_ord+25+50*j,25,25))    
    pygame.draw.rect(fenetre,(255,255,255),(50,450,350,150))
    perso = pygame.image.load("perso.jpeg").convert_alpha()
    perso_position=(0,0)
    fenetre.blit(perso, (perso_position))
    pygame.display.flip()
    
    # boucle permettant de garder la fenêtre ouverte jusqu'à ce qu'on décide
    # de la fermer
    continuer = True
    while continuer:
        for event in pygame.event.get(): # on prend le premier événement de la pile
            if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                continuer = True
            if event.button == 1:	#Si clic gauche
				#On change les coordonnées du perso
				perso_position=personnage.deplacer()
                
finally:
    pygame.quit()
    
