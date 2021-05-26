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


def recompense():
    """ Personnage -> str, str
        Préconditions : None
        Rôle : Le joueur choisit entre deux cadeaux avant de passer au niveau suivant. Modification des attributs du joueur en conséquence. """

    dict_recompense = {"Point de Vie Niveau 1 " : 100, "Point de Vie NIveau 2" : 200, "Point de vie Niveau 3" : 300, "Dégâts supplémentaires Niveau 1" : 50, "Dégâts supplémentaires Niveau 2" : 100, "Dégâts supplémentaires Niveau 2" : 150 }
    liste_recompense_keys = list(dict_recompense.keys())
    liste_recompense_keys_pv = liste_recompense_keys[0:2]
    liste_recompense_keys_degats =  liste_recompense_keys[2:]
    recompense1 = choice(liste_recompense_keys)
    recompense2 = choice(liste_recompense_keys)
    # print("Choisis l'une des deux récompenses suivantes avant de passer au niveau suivant.")
    #affichage des deux récompenses
    recompense = #

    if recompense in liste_recompense_keys_pv:
        perso.pv_t + dict_recompense[recompense]



def victoire(joueur, liste_adversaire):
    """ Personnage, list -> bool
        Préconditions : None
        Rôle : Rôle : Si le joueur a des pv (est en vie, (pv > 0)) et que tout les monstres n'ont plus de pv (sont morts, (pv <= 0)) retourner TRUE, si tout les monstres ne sont pas morts retourne "continue", sinon retourner FALSE. """

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
