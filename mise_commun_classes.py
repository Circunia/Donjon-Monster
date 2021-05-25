#Mise en commun des classes Personnage et Sort.

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
            elif perso.cat == Boss:
                if self.type == "Augmentation":
                    augmentation_action(self, perso)

            else:
                soin_action(self, perso)

        #perte de PA
        perso.pa = perso.pa - self.cout


    def est_zone(self, perso, liste_monstres):
        """ Sort, Personnage, list -> list, list
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
        [(x, y+90), (x, y+135), (x, y+180), (x+45,y+90), (x+45,y+135), (x+45, y+180), (x-45,y+90), (x-45, y+135), (x-45, y+180), (x,y+45), (x+45, y+45), (x-45, y+45)] ]}

        print(zone[self.nom])
        coord_sort = []
        for nom in range(len(zone)):
            #if nom ? == self.nom:
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

        perso.pv_t = 1.05 * perso.pv_t

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



#-------------- Classe Personnage ------------------#
liste_case = []
for i in range (14) :
    for j in range (14) :
        c1 = (50+i*45, 50 + j*45)
        liste_case.append(c1)
#print(len(liste_case))
#print(liste_case)

#graphe
graphe1 = []
for i in range(len(liste_case)):
    graphe1.append([0] * len(liste_case))

for i in range (0, 13, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 12 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (14, 27, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 26 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (28, 41, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 40 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (42, 55, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 54 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (56, 69, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 68 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (70, 83, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 82 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (84, 97, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 96 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (98, 111, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 110 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (112, 125, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 124 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (126, 139, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 138 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (140, 153, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 152 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (154, 167, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 166 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (168, 181, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1
    graphe1[i][i+14] = 1
    graphe1[i+14][i] = 1
    if i == 180 :
        graphe1[i+1][i+15] = 1
        graphe1[i+15][i+1] = 1

for i in range (182, 195, 1):
    graphe1[i][i+1] = 1
    graphe1[i+1][i] = 1


def definir_obstacle (g, liste_obstacle, liste_case):
    """list, list -> void
       Préconditions : len(liste_case) == len(g) et g représente un graphe
       Rôle : Indique la position des obstacles sur le graphe de façon à ce la liaison entre un sommet contenant un obstacle et un qui lui est sommet adjacent ne soit pas possible"""
    liste_o = []
    for i in range (len(liste_obstacle)):
        for j in range (len(liste_case)):
            if liste_case[j] == liste_obstacle[i]:
                liste_o.append(j)
    for obstacle in liste_o :
        if obstacle > 0 :
            graphe1[obstacle][obstacle-1] = 0
            graphe1[obstacle-1][obstacle] = 0
        if obstacle < 195 :
            graphe1[obstacle][obstacle+1] = 0
            graphe1[obstacle+1][obstacle] = 0
        if obstacle < 182 :
            graphe1[obstacle][obstacle+14] = 0
            graphe1[obstacle+14][obstacle] = 0
        if obstacle > 13 :
            graphe1[obstacle][obstacle-14] = 0
            graphe1[obstacle-14][obstacle] = 0


def liste_successeurs(g, i):
    """list, int -> list[int]
    Précondition : 0 <= i < len(g)
    Rôle : retourne la liste des successeurs de i"""
    liste = []
    for j in range(len(g)):
        if g[i][j] == 1:
            liste.append(j)
    return liste

def distances (g, s):
    """list, int -> dict
       Préconditions : g représente un graphe et s est un sommet existant dans g
       Rôle : Retourne un dictionnaire avec les sommets comme clés et les distances entre ces sommets et s en valeurs"""
    distance = {}
    d = 0
    deja_visites = [s]
    courants = [s]
    suivants = []
    while courants != []:
        for sommet in courants :
            distance[sommet] = d
            for successeurs in liste_successeurs(g, sommet) :
                if not successeurs in deja_visites :
                    suivants.append(successeurs)
                    deja_visites.append(successeurs)
        d = d + 1
        courants = suivants
        suivants = []
    return distance

def plus_court_chemin(g, depart, arrivee):
    """list, int, int -> list
    Préconditions : 0 <= depart < len(g), 0 <= arrivee < len(g)
    Rôle : Retourne les sommets parcourus pour aller du sommet de depart au sommet d'arrivee"""
    chemin = [arrivee]
    distances_d = distances(g, depart)
    distance_a = distances_d[arrivee]
    sommet_p = arrivee
    while not depart in chemin :
        predecesseurs = liste_successeurs(g, sommet_p)
        sommets = []
        for sommet, distance in distances_d.items():
            if distance == distance_a - 1 :
                sommets.append(sommet)
        for sommet in sommets :
            for predecesseur in predecesseurs :
                if sommet == predecesseur :
                    sommet_p = predecesseur
                    break
        distance_a = distance_a - 1
        chemin = [sommet_p] + chemin
    return chemin

def chemin (g, depart, arrivee, liste_case):
    """list, int, int, list -> list
       Préconditions : len(liste_case) == len(g) et g représente un graphe, 0 <= depart < len(g), 0 <= arrivee < len(g)
       Rôle : Retourne une liste de coordonnées de case a emprunté pour rejoindre le sommet arrivee à partir du sommet depart"""
    chemin_graphe = plus_court_chemin(g, depart, arrivee)
    chemin = []
    for case in chemin_graphe :
        chemin.append(liste_case[case])
    return chemin

def conversion_cc (coordonnees, liste_case):
    """tuple, list -> int
       Préconditions : coordonnees in liste_case
       Rôle : Retourne le numero de la case représentée par les coordonnées en paramètre"""
    for i in range(len(liste_case)):
        if coordonnees == liste_case[i]:
            return i


from random import randint

class Personnage :

    def __init__ (self, nom, image1, categorie, pv, pv_t, pa, pd, sorts, position):
        """ self, str, png, png, str, int, int, int, dict, tuple
            Préconditions : aucune
            Rôle : Initialise les attributs de la classe Personnage"""

        self.nom = nom #pseudonyme du personnage
        self.im1 = image1 #image qui représente le personnage
        #self.im2 = image2 #image qui représente le personnage lorsqu'il se fait attaquer
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
        return zone_p #retourne une liste de cases (avec leurs coordonnées) sur lesquelles le joueur peut se déplacer
                      # en fonction de ses pd


    def deplacer(self, liste_m, liste_o):
        """self(Personnage), list, list -> void
           Préconditions : le personnage pris en paramètre doit être en vie.
           Rôle : Change la position du personnage en fonction de ses pd et de la requête
                  de l'utilisateur si le personnage est le joueur."""
        # if self.cat == "Joueur" :
        #     zone = self.zone_possible(liste_m, liste_o)
        #         self.pstn =   # appel à une fonction qui retourne les coordoonnées de la case sur laquelle l'utilisateur a cliqué
        # elif self.cat == "Monstre1":
        #     position_joueur = conversion_cc(Joueur.pstn, liste_case)
        #     position_monstre = conversion_cc(self.pstn, liste_case)
        #     chemin_m = chemin(grille, position_monstre, position_joueur, liste_case)
        #     while self.pd > and len(chemin_m) > 0 :
        #         self.pstn = chemin_m.pop(0)
        #         self.pd = self.pd - 1
        # elif self.cat == "Monstre2":
        #     position_joueur = conversion_cc(Joueur.pstn, liste_case)
        #     position_monstre = conversion_cc(self.pstn, liste_case)
        #     chemin_m = chemin(grille, position_monstre, position_joueur, liste_case)
        #     while self.pd > and len(chemin_m) > 0 :
        #         self.pstn = chemin_m.pop(0)
        #         self.pd = self.pd - 1
        # elif self.cat == "Monstre3":
        #     zone_p = self.zone_possible(liste_m, liste_o)
        #     for i in range(self.pd):
        #         n = randint(0, len(zone_p))
        #         self.pstn = (zone_p[n][0], zone_p[n][1])
        #         self.pd = self.pd - 1
        #
        # else :
        #     zone_p = self.zone_possible(liste_m, liste_o)
        #     for i in range(self.pd):
        #         n = randint(0, len(zone_p))
        #         self.pstn = (zone_p[n][0], zone_p[n][1])
        #         self.pd = self.pd - 1


    def action (self) :
        """self(Personnage) -> void
           Préconditions :
           Rôle : fait agir les sorts en fonction du type de personnage"""
        # if self.cat == "Joueur" :
        #     while self.pa > 0 and #fonction qui détermine si le joueur a fini son tour ou non
        #     sort_j = #appel à la fonction qui sélectionne le sort sur lequel le joueur a cliqué
        #     monstre = #appel à la fonction qui sélectionne le monstre sur lequel le joueur clique
        #     sort_j.action_sorts(self, monstre)
        # elif self.cat == "Monstre1":
        #     if self.pa >= self.sorts["attaque"][0].cout:
        #             self.sorts["attaque"][0].action_sorts(self, Joueur)

        if self.cat == "Monstre2": #elif
            if self.pv < 150 :
                if self.pa >= self.sorts["soin"][0].cout:
                    self.sorts["soin"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
            elif not Joueur.pstn in zone_coup_de_couteau1 : #liste de coordonnées des cases sur lesquelles agit le sort (Lilas)
                if self.pa >= self.sorts["soin"][0].cout:
                    self.sorts["soin"][0].action_sorts(self, Joueur)
            else :
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)

        elif self.cat == "Monstre3" :
            if self.pv < 200 :
                if self.pa >= self.sorts["soin"][0].cout :
                    self.sorts["soin"][0].action_sorts(self, Joueur)
                n = randint(0,1)
                if self.pa >= self.sorts["attaque"][n].cout:
                    self.sorts["attaque"][n].action_sorts(self, Joueur)
            else :
                n = randint(0,1)
                if self.pa >= self.sorts["attaque"][n].cout:
                    self.sorts["attaque"][n].action_sorts(self, Joueur)
                n = randint(0,1)
                if self.pa >= self.sorts["attaque"][n].cout:
                    self.sorts["attaque"][n].action_sorts(self, Joueur)
        else :
            if self.pv < 300 :
                if self.pa >= self.sorts["soin"][0].cout :
                    self.sorts["soin"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout :
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
            elif Joueur.pstn in zone_eclair : #liste de coordonnées des cases sur lesquelles agit le sort (Lilas)
                n = randint(0,1)
                if n == 0 :
                    if self.pa >= self.sorts["defense"][0].cout :
                        self.sorts["defense"][0].action_sorts(self, Joueur)
                else :
                    if self.pa >= self.sorts["attaque"][0].cout :
                        self.sorts["attaque"][0].action_sorts(self, Joueur)
            else :
                if self.pa >= self.sorts["attaque"][1].cout :
                    self.sorts["attaque"][1].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout :
                    self.sorts["attaque"][0].action_sorts(self, Joueur)

#--------------Coordonnées des sorts--------------#
#-----------Création des sorts---------#
#def __init__(self, nom, degats, type, cout, description):

#-----Attaque-----#
explosion = Sort("Explosion", 130, "attaque", 3, "Fais exploser une bombe infligeant des degats de zone.")
fleches_empoisonnees = Sort("Flèches empoisonnées", 200, "attaque", 2, "Envoie 3 flèches empoisonnées sur son adversaire.")
coup_de_couteau = Sort("Coup de couteau", 50, "attaque", 1, "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen." )
coup_de_couteau1 = Sort("Coup de couteau", 100, "attaque", 2, "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen.")
coup_de_couteau2 = Sort("Coup de couteau", 150, "attaque", 3, "Poignarde son adversaire de 3 coups de couteaux dans l'abdomen.")


#-----Defense-----#
augmentation = Sort("Augmentation", None, "defense", 4, "Le joueur augmente son nombre de point de vie total pour le reste de la partie.")
eclair = Sort("Eclair", None, "defense", 2, "Envoie un éclair qui va restraindre son adversaire en lui enlevant des pd pour un tour.")
immobilisation = Sort("Immobilisation", None,"defense", 4, "Immobilise son adversaire en créeant une faille sur 4 cases.")

#-----Soin--------#
benediction = Sort("Bénédiction", None, "soin", 5, "Bénis le joueur en lui régénerant 20% de son nombre de point de vie total. ")
illumination = Sort("Illumination", 200, "soin", 1, "Soigne le joueur de 200 pv en abatant son sceptre de lumière.")
illumination1 = Sort("Illumination", 50, "soin", 1, "Soigne le joueur de 50 pv en abatant son sceptre de lumière.")
illumination2 = Sort("Illumination", 100, "soin", 1, "Soigne le joueur de 100 pv en abatant son sceptre de lumière.")

#-----personnage--------#
Joueur = Personnage("You", "joueur.png", "Joueur", 1200, 1200, 7, 4, {"attaque" : [explosion, fleches_empoisonnees], "soin" : [benediction], "defense" : [immobilisation]}, (140, 320))

#Niveau 1


monstre1_1_niv1 = Personnage("Lezardo", "monstre1.png", "Monstre1", 300, 300, 2, 1, {"attaque" : [coup_de_couteau]}, (365,95))
monstre1_2_niv1 = Personnage("Lezardo", "monstre1.png", "Monstre1", 300, 300, 2, 1, {"attaque" : [coup_de_couteau]}, (365,365))
monstre1_3_niv1 = Personnage("Lezardo", "monstre1.png", "Monstre1", 300, 300, 2, 1, {"attaque" : [coup_de_couteau]}, (365,590))
monstre2_1_niv1 = Personnage("Croco", "monstre2.png", "Monstre2", 500, 500, 2, 3, {"attaque" : [coup_de_couteau1], "soin": [illumination]}, (545,230))
monstre2_2_niv1 = Personnage("Croco", "monstre2.png", "Monstre2", 500, 500, 2, 3, {"attaque" : [coup_de_couteau1], "soin": [illumination]}, (545,410))

liste_o = [(500,95), (185,500), (455,545)]
liste_m = [monstre1_1_niv1, monstre1_2_niv1, monstre1_3_niv1,monstre2_1_niv1 ,monstre2_1_niv1]




#----------------------Test---------------------#

benediction.est_zone(Joueur, liste_m)
