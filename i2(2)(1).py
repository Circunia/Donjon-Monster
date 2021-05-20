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
class Personnage :
    
    def __init__ (self, nom, image1, image2, categorie, pv, pa, pd, sorts, position):
        """ self, str, png, png, str, int, int, int, dict, tuple
            Préconditions : aucune
            Rôle : Initialise les attributs de la classe Personnage"""
        
        self.nom = nom #pseudonyme du personnage
        self.im1 = image1 #image qui représente le personnage
        self.im2 = image2 #image qui représente le personnage lorsqu'il se fait attaquer
        self.cat = categorie #statut du personnage (joueur, monstre1, monstre2, monstre3, boss)
        self.pv = pv #nombre de points de vie
        self.pv_t = pv #nombre de points de vie total (non variable)
        self.pa = pa #nombre de points d'action, sert à utiliser les sorts
        self.pd = pd #nombre de points de déplacement, égale au nombre de cases que peut franchir le personnage à chaque tour
        self.sorts = sorts #clés = types de sorts (attaque, soin, défense), valeurs = sorts du personnage stockés dans des listes
        self.pstn = position #coordonnées de l'emplacement du personnage
        
    def est_mort (self) :
        """self(Personnage) -> bool
           Préconditions :
           Rôle : Retourne True si le personnage est mort (pv <= 0), False sinon."""
        if self.pv <= 0 :
            return True
        else :
            return False
    def zone_possible(self, list_m, list_o):
        """self(Personnage), list, list -> list
           Préconditions : le personnage pris en paramètre doit être en vie.
           Rôle : Retourne la liste des cases sur lesquelles peut se déplacer le personnage"""
        xj = self.pstn[0]
        yj = self.pstn[1]
        zone = []
        case = 45
        n = self.pd + 1
        for i in range (0, n):
            for j in range (0, n):
                case1 = (xj + (i * case), yj + (j * case))
                case2 = (xj - (i * case), yj - (j * case))
                case3 = (xj + (i * case), yj - (j * case))
                case4 = (xj - (i * case), yj + (j * case))
                compteur1 = 0
                compteur2 = 0
                compteur3 = 0
                compteur4 = 0
            
                if case1[0] >= 50 and case1[0] < 680 and case1[1] >= 50 and case1[1] < 680 :
                    for monstre in liste_m :
                        if case1[0] == monstre[0] and case1[1] == monstre[1] :
                            compteur1 += 1
                    for obstacle in liste_o :
                        if case1[0] == obstacle[0] and case1[1] == obstacle[1] :
                            compteur1 += 1
                    if compteur1 == 0 :
                        zone.append(case1)
                                    
                if case2[0] >= 50 and case2[0] < 680 and case2[1] >= 50 and case2[1] < 680 :
                    for monstre in liste_m :
                        if case2[0] == monstre[0] and case2[1] == monstre[1] :
                            compteur2 += 1
                    for obstacle in liste_o :
                        if case2[0] == obstacle[0] and case2[1] == obstacle[1] :
                            compteur2 += 1
                    if compteur2 == 0 :
                        zone.append(case2)
                        
                if case3[0] >= 50 and case3[0] < 680 and case3[1] >= 50 and case3[1] < 680 :
                    for monstre in liste_m :
                        if case3[0] == monstre[0] and case3[1] == monstre[1] :
                            compteur3 += 1
                    for obstacle in liste_o :
                        if case3[0] == obstacle[0] and case3[1] == obstacle[1] :
                            compteur3 += 1
                    if compteur3 == 0 :
                        zone.append(case3)
                        
                if case4[0] >= 50 and case4[0] < 680 and case4[1] >= 50 and case4[1] < 680 :
                    for monstre in liste_m :
                        if case4[0] == monstre[0] and case4[1] == monstre[1] :
                            compteur4 += 1
                    for obstacle in liste_o :
                        if case4[0] == obstacle[0] and case4[1] == obstacle[1] :
                            compteur4 += 1
                    if compteur4 == 0 :
                        zone.append(case4)
            n = n - 1
        zone_p = []
        for coordonnees in zone :
            if coordonnees not in zone_p :
                zone_p.append(coordonnees)
        return zone_p
    
def affiche(perso,liste_m,liste_o):
    """
    """
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.draw.rect(fenetre, (255,255,255), (0, 0, 1300, 700))
    
    font=pygame.font.SysFont("broadway",24,bold=False,italic=False)
    texte=font.render("Donjon Monster",2,(0,0,0))
    fenetre.blit(texte,(275,0))
    
    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (225,206,154), (50+90*i, 50+90*j, 45, 45))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (225,206,154), (95+90*i, 95+90*j, 45, 45))
    
    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (250,240,197), (95+90*i, 50+90*j, 45, 45))
            
    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (250,240,197), (50+90*i, 95+90*j, 45, 45))
    #affichage de la zone de sort
    x = 320
    y = 320
    zone = [[(x, y-45)], [(x-45,y)], [(x, y+45)],[(x+45,y)]]
    for case in zone:
        pygame.draw.rect(fenetre, (100,140,130), (case[0][0],case[0][1], 45, 45))
    pygame.draw.rect(fenetre, (200,240,230), (x,y, 45, 45))
    
    #affichage de la zone sur laquelle le personnage peut se déplacer
    zone_po = perso.zone_possible(liste_o, liste_m)
    for i in zone_po:
        pygame.draw.rect(fenetre,(0,255,0),(i[0],i[1],45,45))   
    #affichage du personnage
    (x,y)=perso.pstn
    pygame.draw.rect(fenetre,(255,0,0),(x,y,45,45))
    #affichage des monstres
    t=0
    for j in range(len(liste_m)):
        x,y=liste_m[j]
        t=t+1
        if j==0:
            monstre2 = pygame.image.load("monstre2.png").convert_alpha()
            fenetre.blit(monstre2,(x, y))
        if j==1:
            monstre1 = pygame.image.load("monstre1.png").convert_alpha()
            fenetre.blit(monstre1,(x, y))
#         if j==2:
#             monstre3=pygame.image.load("monstre3.png").convert_alpha()
#             fenetre.blit(monstre3,(x, y))
    #affichage des obstacles
    k=0
    for l in range(len(liste_o)):
        monstre=liste_o[l]
        k=k+1
        pygame.draw.rect(fenetre,(19,25,70),(liste_o[l][0],liste_o[l][1],45,45))
    
      
       
   
    pygame.display.flip()

# dimensions de la fenetre :
largeur = 1300 # largeur en pixels
hauteur = 700 # hauteur en pixels


#toujours encadrer vos programmes pygame par try et finally ce qui permet de
# fermer correctement la fenêtre pygame en cas d'erreur
try:
    fenetre = pygame.display.set_mode((largeur,hauteur))
    perso=Personnage("bob","image1","image2","monstre",100,100,2,"attaque",(140,320))
    liste_o = [(500,95), (185,500), (455,545)]
    liste_m = [(365,95),(320,320),(365,590),(545,230),(545,410)]
    zone_possible=[(50,95),(95,140),(50,140)]
    affiche(perso,liste_m,liste_o)
    
    
    
    
    # boucle permettant de garder la fenêtre ouverte jusqu'à ce qu'on décide
    # de la fermer
    continuer = True
    while continuer:
        for event in pygame.event.get(): # on prend le premier événement de la pile
            if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                continuer = False
            if event.type==MOUSEBUTTONDOWN :
                 (x,y)=event.pos
                 l=y//45
                 c=x//45
                 perso.pstn=(c*45,l*45)
            affiche(perso,liste_m,liste_o)
                    
finally:
    pygame.quit()






