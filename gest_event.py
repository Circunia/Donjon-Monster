#--------Gestionnaire d'évenement--------#

#importations

from random import *


#--------Fonctions-------#

def tour_par_tour(joueur,):
    """ Personnage,    -> void
        Préconditions : None
        Rôle : Appel chaque fonction du gestionnaire des tâches pour mettre à jour les évenements et fait jouer le personnage suivant. """



    victoire(joueur, liste_adversaire)
    if victoire:
        recompense(joueur)

def recompense(joueur):
    """ Personnage -> str, str
        Préconditions : None
        Rôle : Le joueur choisit entre deux cadeaux avant de passer au niveau suivant. Modification des attributs du joueur en conséquence. """

    dict_recompenses = {}
    dict_recompenses["Point de vie"] = 100
    dict_recompenses["Dégâts suplémentaires"] = 50 # bonus de dégat à ajouter dans la classe sort
    dict



#faire appel à une fonction input graphique qui renvoie la récompense choisi puis continuer et modifier les attributs du joueur. 


    return recompense1 and recompense2



 def victoire(joueur, liste_adversaire):
    """ Personnage, list -> bool
        Préconditions : None
        Rôle : Si le joueur a des pv (est en vie, (pv > 0)) et que tout les monstres n'ont plus de pv (sont morts, (pv <= 0)) retourner TRUE,
               sinon retourner FALSE. """

    nb_mort = 0
    if est_mort(joueur):
        return False
    else:
        for adversaire in liste_adversaire:
            if est_mort(adversaire):
                nb_mort += 1
        if nb_mort == len(liste_adversaire):
            return True
        return False




#----------------TEST-----------------#
victoire(perso1, liste_adversaire)
