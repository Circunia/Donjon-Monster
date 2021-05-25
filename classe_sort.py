#----------Debut de la classe----------#

class Sort:

    def __init__(self, nom, degats, type_sort, cout, description):
        """ Type : self, str, int, str, list, int, str -> void
          Préconditions : None
          Rôle : Initialise les attributs de la classe Sort. """

        self.nom = nom #nom donné au sort
        self.degats = degats # nombre de pv retirés par le sort
        self.type = type_sort # attaque, soin, défense
        self.cout = cout # nombre de pa que nécessite le sort
        self.desc = description # description du sort

#perso = joueur
#adv = adversaire

    def action_sort(self, perso, adv):
        """ self, Personnage, Personnage -> void
             Préconditions : self.pv != 0
             Rôle : En fonction du type du sort, lance le sort sur l'adversaire ou le joueur correspondant. """

        if perso.cat == Joueur:
            if self.type == "attaque" :
                attaque_action(self, adv)
            elif self.type == defense:
                if self.type == "defense":
                    defense_action(self, adv)
            #elif perso.cat == Boss:
            elif self.type == "Augmentation":
                augmentation_action(self, perso)

            else:
                soin_action(self, perso)

        #perte de PA
        perso.pa = perso.pa - self.cout

    def est_zone(self, perso, liste_monstres):
        """ Personnage, list[Personnage], Sort -> list
            Préconditions : None
            Rôle : Détermine si un ou plusieurs monstres se trouve dans la zone d'action du sort et renvoit False si la liste de monstres est vide sinon la liste de coordonnées des monstres dans la zone. """

        #position du joueur
        x = perso.pstn[0]
        y = perso.pstn[1]

        #--------------Coordonnées des sorts--------------#

        # var = [(face),(left), (right), (back)]
        zone = {"Explosion" : [(x, y-90), (x, y-135), (x, y-180), (x-45,y-90), (x-45,y-135), (x-45, y-180), (x+45,y-90), (x+45, y-135), (x+45, y-180)],
        "Fleches Empoisonnees" : [[(x, y-180), (x-45, y-180), (x+45, y-180)], [(x, y+180), (x-45, y+180), (x+45, y+180)]],
        "Coup de couteau" : [[(x, y-45)], [(x-45,y)], [(x, y+45)],[(x+45,y)]],
        "Augmentation" : [(x,y)],
        "Immobilisation" : ([(x-45,y),(x-90, y), (x-135, y), (x-180,y)],[(x+45,y),(x+90, y), (x+135, y), (x+180,y)]),
        "Eclair" : [[(x,y-180)], [(x-180, y)], [(x+180, y)], [(x,y+180)]],
        "Benediction" : [(x,y)],
        #haut, droite, gauche, bas
        "Illumination" : [ [(x, y-90), (x, y-135), (x, y-180), (x-45,y-90), (x-45,y-135), (x-45, y-180), (x+45,y-90), (x+45, y-135), (x+45, y-180), (x,y-45), (x-45, y-45), (x+45, y-45)],
        [(x+90,y+45), (x+135,y+45), (x+180, y+45),(x+90, y), (x+135, y), (x+180, y), (x+90,y-45), (x+135, y-45), (x+180, y-45),(x+45,y), (x+45,y-45), (x+45, y+45)],
        [(x-90, y), (x-135, y), (x-180, y), (x-90,y-45), (x-135,y-45), (x-180, y-45), (x-90,y+45), (x-135, y+45), (x-180, y+45), (x-45, y), (x-45, y+45), (x-45, y-45)],
        [(x, y+90), (x, y+135), (x, y+180), (x+45,y+90), (x+45,y+135), (x+45, y+180), (x-45,y+90), (x-45, y+135), (x-45, y+180), (x,y+45), (x+45, y+45), (x-45, y+45)] ]"}

        coord_sort = []
        for nom in range(len(zone)):
            if zone[nom] == self.nom:
                coord_sort.append(zone[self.nom])
                print(zone)
                print(coord_sort)

        if perso.cat == "Joueur":
            liste_monstre_in_zone = [] #liste de monstres dans la zone d'action du sort
            for i in range(len(liste_monstres)):
                if liste_monstres[i].pstn in coord_sort:
                    liste_monstre_in_zone.append(liste_monstres[i])
                    if liste_monstre_in_zone == []:
                        return False
                    else:
                        return liste_monstre_in_zone and coord_sort

    # def zone_coord(self, dico_coordonnees, liste_monstres, perso):
    #     """ Sort, dict -> list[2-uplet]
    #         Préconditions : None
    #         Rôle : Associe des coordonnées à un sort. """
    #
    #     print(dico_coordonnees) #zone
    #     #position du joueur
    #     x = perso.pstn[0]
    #     y = perso.pstn[1]
    #     print(x,y)
    #
    #     for nom in range(len(dico_coordonnees)):
    #         if dico_coordonnees[i] == self.nom:
    #             zone = dico_coordonnees[self.nom]
    #             print(zone)
    #             print(est_zone(perso, liste_monstres, zone))


#-----------Actions des sorts------------#

    #-----Attaque------#
    def attaque_action(self, adv):
        """ Sort, Personnage -> void
            Préconditions : perso.pv != 0
            Rôle : A l'aide d'une attaque fait perdre des points de vie à ses adversaires."""

        adv.pv = adv.pv - self.degats

    #-----Defense-----#
    def augmentation_action(self, perso):
        """ Sort, Personnage -> void
            Préconditions : perso.pv != 0
            Rôle : Augmente le nombre de pv du joueur de 5% en fonction du nombre de pv_t. """

        perso.pv_t = 1,05*perso.pv_t

    def defense_action(self, adv):
        """ Sort, Personnage -> void
            Préconditions : perso.pv != 0
            Rôle : Supprime les pd de l'adversaire."""

        if self.nom == "Eclair":
            nb = 2
        if self.nom == "Immobilisation":
            nb = adv.pd
        adv.pd = adv.pd - nb


    #------Soin------#
    def soin_action(self, perso):
        """ Sort, Personnage -> void
            Préconditions : perso.pv != 0
            Rôle : Augmente le nombre de point de vie du joueur. """

        if self.nom == "Bénédiction":
            perso.pv = perso.pv + perso.pv_t*0.2
        if self.nom == "Illumination":
            perso.pv = perso.pv + self.degats #degats = pv rendu









#-----------Création des sorts---------#
#def __init__(self, nom, degats, type, zone, cout, description):

#-----Attaque-----#
explosion = Sort("Explosion", 130, "attaque", 3, "Fais exploser une bombe infligeant des degats de zone.")
fleches_empoisonnees = Sort("Flèches empoisonnées", 200, "attaque", 2, "Envoie 3 flèches empoisonnées sur son adversaire.")
coup_de_couteau = Sort("Coup de couteau", 50, "attaque", 1, "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen." )
coup_de_couteau1 = Sort("Coup de couteau", 100, "attaque", 2, "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen.")
coup_de_couteau2 = Sort("Coup de couteau", 150, "attaque", 3, "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen.")


#-----Defense-----#
augmentation = Sort("Augmentation", None, "defense", 4, "Le joueur augmente son nombre de point de vie total pour le reste de la partie.")
eclair = Sort("Eclair", None, "defense", 2, "Envoie un éclair qui va restraindre son adversaire en lui enlevant des pd pour un tour.")
immobilisation = Sort("Immobilisation", None, "defense", 4, "Immobilise son adversaire en créeant une faille sur 4 cases.")

#-----Soin--------#
benediction = Sort("Bénédiction", None, "soin", 5, "Bénis le joueur en lui régénerant 20% de son nombre de point de vie total. ")
illumination = Sort("Illumination", 200, "soin", 1, "Soigne le joueur de 200 pv en abatant son sceptre de lumière.")
illumination1 = Sort("Illumination", 50, "soin", 1, "Soigne le joueur de 50 pv en abatant son sceptre de lumière.")
illumination2 = Sort("Illumination", 100, "soin", 1, "Soigne le joueur de 100 pv en abatant son sceptre de lumière.")




#------------------TEST-------------------#
liste_coord = (25,50)
