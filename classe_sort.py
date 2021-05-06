#----------Debut de la classe----------#

class Sort:

    def __init__(self, nom, degats, type_sort, zoneh, zonel, projection, cout, description):
      """ Type : self, str, int, str, list, int, int, str -> void
          Préconditions : None
          Rôle : Initialise les attributs de la classe Sort. """

      self.nom = nom #nom donné au sort
      self.degats = degats # nombre de pv retirés par le sort
      self.type = type_sort # attaque, soin, défense
      self.zoneh = zone # définit le nombre de cases en hauteur que le sort peut utiliser
      self.zonel = zone # définit le nombre de cases en longueur que le sort peut utiliser
      self.proj = projection # distance entre le joueur et la zone
      self.cout = cout # nombre de pa que nécessite le sort
      self.desc = description # description du sort

#perso = joueur
#adv = adversaire

    def action_sort(self, perso, adv):
         """ self, Personnage, Personnage -> void
             Préconditions : self.pv != 0
             Rôle : En fonction du type du sort, lance le sort sur l'adversaire ou le joueur correspondant. """

        if condition_sort(): #True
        # choix du sort lancé
        if self.type == "attaque" :
            attaque_action(self, adv)
        elif self.type == defense:
            if self.nom == "defense":
                defense_action(self, adv)
            else:
                augmentation_action(self, perso)

        else:
            soin_action(self, perso)
        #perte de PA
        perso.pa = perso.pa - self.cout

    def zone_action(self, perso):
        """ self, Personnage -> list[t-uplet]
            Préconditions : None
            Rôle : Retourne une liste correspondant à la zone d'action du sort."""
        list_zone = []
        #x = perso.pstn[0] #coordonnées du personnage (position de départ)
        #y = perso.ptsn[1] #coordonnées du personnage (possition de départ)
        x = perso[0]
        y = perso[1]

        for hauteur in range(self.zoneh):
            self.list_zone.append( (x+25,y) )
            for longueur in range(self.zonel):
                self.list_zone.append( (x, y+25) )
        return list_zone
    #définis seulement des zones rectangulaires ( à améliorer)

# x = perso.pstn[0]
# y = perso.pstn[1]
# zone_explosion = [(x+25, y), (x+50, y)]
# zone_explosion = [(perso.pstn[0]+25, perso.pstn[1]), (perso.pstn[0]+50, perso.pstn[1])]

# var = [(face),(left), (right),   (back)]
zone_explosion = [(x, y-50), (x, y-75), (x, y-100), (x-25,y-50), (x-25,y-75), (x-25, y-100), (x+25,y-50), (x+25, y-75), (x+25, y-100)] # 1
zone_fleches_empoisonnees = [(x, y-100), (x-25, y-100), (x+25, y-100), (x, y+100), (x-25, y+100), (x+25, y+100)] # 2
zone_coup_de_couteau = [(x, y-25), (x-25,y), (x, y+25),(x+25,y)] # 3
zone_augmentation = [(x,y)]
zone_eclair = [()]
zone_benediction
zone_illumination



def est_zone(perso, liste_monstres, zone):
    """ Personnage, list[Personnage], Sort -> list
        Préconditions : None
        Rôle : Détermine si un ou plusieurs monstres se trouve dans la zone d'action du sort, si oui  """

    if perso.cat == "Joueur":
        liste_monstre_in_zone = [] #liste de monstres dans la zone d'action du sort
        for i in range(len(liste_monstres)):
            if liste_monstres[i].pstn in zone:
                liste_monstre_in_zone.append(liste_monstres[i])
            return liste_monstre_in_zone



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
            perso.pv = perso.pv + 200

#-----------Création des sorts---------#
#def __init__(self, nom, degats, type, 'zoneh, zonel, projection,' cout, description):

#-----Attaque-----#
explosion = Sort("Explosion", 50, "attaque", 3, 3, 2, 3, "Fais exploser une bombe infligeant des degats de zone.")
fleches_empoisonnees = Sort("Flèches empoisonnées", 30, "attaque", 0, 3, 1, "Envoie 3 flèches empoisonnées sur son adversaire.")
coup_de_couteau = Sort("Coup de couteau", 10, "attaque", 1,                     "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen." )
coup_de_couteau1 =
coup_de_couteau2 =


#-----Defense-----#
augmentation = Sort("Augmentation", None, "defense", 0, 0, 0, 4, "Le joueur augmente son nombre de point de vie total pour le reste de la partie.")
eclair = Sort("Eclair", None, "defense", 0, 0, 5, 2, "Envoie un éclair qui va restraindre son adversaire en lui enlevant des pd pour un tour.")

#-----Soin--------#
benediction = Sort("Bénédiction", None, "soin", 0, 0, 0, 3, "Bénis le joueur en lui régénerant 30% de son nombre de point de vie total. ")
illumination = Sort("Illumination", None, "soin", 0, 0, 0, 1, "Soigne le joueur de 200 pv en abatant son sceptre de lumière.")
illumination1 =
illumination2 =



#------------------TEST-------------------#
liste_coord = (25,50)
zone_action(explosion, liste_coord)
