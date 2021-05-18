#     Ce fichier sert à regrouper toutes nos parties de codes pour améliorer le travail collectif, on peut accéder au code des autres intégralement pour tester nos fonctions
# et laisser des personnages et des monstres à réutiliser pour les autres. Le travail stocké est celui finis par ceux qui en sont en charge.

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

class Sort:


    def __init__(self, nom, degats, type, zoneh, zonel, projection, cout, description):
      """ Type : self, str, int, str, list, int, int, str -> void
          Préconditions : None
          Rôle : Initialise les attributs de la classe Sort. """

      self.nom = nom #nom donné au sort
      self.degats = degats # nombre de pv retirés par le sort
      self.type = type # attaque, soin, défense
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

        if self.type == attaque:
            attaque_action(self, adv)
        elif self.type == defense:
            if self.nom == "Augmentation":
                augmentation_action(self, perso)
            else:
                defense_action(self, adv)
        else:
            soin_action(self, perso)
        #perte de PA
        perso.pa = perso.pa - self.cout

    def zone_action(self, perso):
        """ self, Personnage -> list[t-uplet]
            Préconditions : None
            Rôle : Retourne une liste correspondant à la zone d'action du sort."""
        list_zone = []
        x = perso.pstn[0] #coordonnées du personnage (position de départ)
        y = perso.ptsn[1] #coordonnées du personnage (possition de départ)

        for hauteur in range(self.zoneh):
            self.list_zone.append( (x+25,y) )
            for longueur in range(self.zonel):
                self.list_zone.append( (x, y+25) )
        return list_zone

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
#def __init__(self, nom, degats, type, zoneh, zonel, projection, cout, description):

#-----Attaque-----#
explosion = Sort("Explosion", 50, "attaque", 3, 3, 2, 3, "Fais exploser une bombe infligeant des degats de zone.")
fleches_empoisonnees = Sort("Flèches empoisonnées", 30, "attaque", 0, 3, 1, "Envoie 3 flèches empoisonnées sur son adversaire")

#-----Defense-----#
augmentation = Sort("Augmentation", None, "defense", 0, 0, 0, 4, "Le joueur augmente son nombre de point de vie total pour le reste de la partie.")
eclair = Sort("Eclair", None, "defense", 0, 0, 5, 2, "Envoie un éclair qui va restraindre son adversaire en lui enlevant des pd pour un tour.")

#-----Soin--------#
benediction = Sort("Bénédiction", None, "soin", 0, 0, 0, 3, "Bénis le joueur en lui régénerant 30% de son nombre de point de vie total. ")
illumination = Sort("Illumination", None, "Soin", 0, 0, 0, 1, "Soigne le joueur de 200 pv en abatant son sceptre de lumière.")