#--------Gestionnaire d'évenement--------#

#importations
from random import *


#--------Fonctions-------#

def tour_par_tour(joueur):
    """ Personnage -> void
        Préconditions : None
        Rôle : Appel chaque fonction du gestionnaire des tâches pour mettre à jour les évenements et fait jouer le personnage suivant. """

    statut_victoire = victoire(joueur, liste_adversaire) # True, False, "continue"
    if statut_victoire == "continue" :
        return
    if victoire() :
        #lance la salle suivante
        #recompense(joueur)
    elif victoire() == False:
        reponse = input("Veux tu recommencer le niveau ? Oui/ Non")
        if reponse == Oui :
            #relancer le niveau
        else :
            #retourne à l'accueil
    else :
        #ne rien faire, break ?


def recompense(joueur):
    """ Personnage -> str, str
        Préconditions : None
        Rôle : Le joueur choisit entre deux cadeaux avant de passer au niveau suivant. Modification des attributs du joueur en conséquence. """

    dict_recompenses = {"Point de Vie Niveau " : 100, "Point de Vie" : 200, "Point de vie" : 300, "Dégâts supplémentaires Niveau 1" : 50, "Dégâts supplémentaires"}


#faire appel à une fonction input graphique qui renvoie la récompense choisi puis continuer et modifier les attributs du joueur.


    return recompense1 and recompense2



def victoire(joueur, liste_adversaire):
    """ Personnage, list -> bool
        Préconditions : None
        Rôle : Si le joueur a des pv (est en vie, (pv > 0)) et que tout les monstres n'ont plus de pv (sont morts, (pv <= 0)) retourner TRUE,
               sinon retourner FALSE. """

    nb_mort = 0
    if est_mort(joueur): # défaite
        return False
    else: # victoire
        for adversaire in liste_adversaire:
            if est_mort(adversaire):
                nb_mort += 1
        if nb_mort == len(liste_adversaire):
            return True
        return "continue" # le joueur peut continuer de jouer mais tout les monstres ne sont pas morts.

#----------------TEST-----------------#
victoire(perso1, liste_adversaire)
