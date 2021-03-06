#----------Debut de la classe Sort----------#

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

    def action_sort(self, perso):
        """ self, Personnage, Personnage -> void
             Préconditions : self.pv != 0
             Rôle : En fonction du type du sort, lance le sort sur l'adversaire ou le joueur correspondant. """

        if perso.cat == "Joueur":
            if self.type == "attaque" :
                liste_monstre_in_zone = self.monstres_in_zone(perso, liste_m)
                for monstre in liste_monstre_in_zone :
                    self.attaque_action(monstre)

            elif self.type == "defense":
                liste_monstre_in_zone = self.monstres_in_zone(perso, liste_m)
                for monstre in liste_monstre_in_zone :
                    self.defense_action(monstre)
            else:
                self.soin_action(perso)
        else:
            if self.type == "attaque" :
                zone_sort = self.est_zone_s(perso, Joueur)
                if Joueur.pstn in zone_sort :
                    self.attaque_action(Joueur)

            elif self.type == "defense":
                if self.nom == "Augmentation" :
                    self.augmentation_action(perso)
                else :
                    zone_sort = self.est_zone_s(perso, Joueur)
                    if Joueur.pstn in zone_sort :
                        self.defense_action(Joueur)
            else:
                zone_sort = self.est_zone_s(perso, Joueur)
                self.soin_action(perso)
        perso.pa = perso.pa - self.cout


    def est_zone_s(self, perso, joueur):
        """ Personnage, list[Personnage], Sort -> list
            Préconditions : None
            Rôle : Détermine si un ou plusieurs monstres se trouve dans la zone d'action du sort et renvoit False si la liste de monstres est vide sinon la liste de coordonnées des monstres dans la zone. """

        #position du joueur
        x = perso.pstn[0]
        y = perso.pstn[1]

        #--------------Coordonnées des sorts--------------#

        # var = [(face),(left), (right), (back)]
        zone = {"Explosion" : [[(x+90, y), (x+135, y), (x+180, y), (x+90, y+45), (x+135, y+45), (x+180, y+45), (x+90, y-45), (x+135, y-45), (x+180, y-45)],[(x, y-90), (x, y-135), (x, y-180), (x-45,y-90), (x-45,y-135), (x-45, y-180), (x+45,y-90), (x+45, y-135), (x+45, y-180)],[(x, y+90), (x, y+135), (x, y+180), (x-45,y+90), (x-45,y+135), (x-45, y+180), (x+45,y+90), (x+45, y+135), (x+45, y+180)],[(x-90, y), (x-135, y), (x-180, y), (x-90, y+45), (x-135, y+45), (x-180, y+45), (x-90, y-45), (x-135, y-45), (x-180, y-45)]],
        "Flèches empoisonnées" : [[(x+180, y), (x+180, y+45), (x+180, y-45)],[(x, y-180), (x-45, y-180), (x+45, y-180)], [(x, y+180), (x-45, y+180), (x+45, y+180)], [(x-180, y), (x-180, y-45), (x-180, y+45)]],
        "Coup de couteau" : [[(x+45,y)],[(x, y-45)],[(x, y+45)] ,[(x-45,y)]],
        "Augmentation" : [(x,y)],
        "Immobilisation" : [[(x+45,y),(x+90, y), (x+135, y), (x+180,y)],[(x, y-45), (x, y-90), (x, y-135), (x, y-180)] ,[(x, y+45), (x, y+90), (x, y+135), (x, y+180)], [(x-45,y),(x-90, y), (x-135, y), (x-180,y)]],
        "Eclair" : [[(x+180, y)], [(x,y-180)], [(x,y+180)], [(x-180, y)]],
        "Bénédiction" : [(x,y)],
        "Illumination" : [[(x+90,y+45), (x+135,y+45), (x+180, y+45),(x+90, y), (x+135, y), (x+180, y), (x+90,y-45), (x+135, y-45), (x+180, y-45),(x+45,y), (x+45,y-45), (x+45, y+45)] ,[(x, y-90), (x, y-135), (x, y-180), (x-45,y-90), (x-45,y-135), (x-45, y-180), (x+45,y-90), (x+45, y-135), (x+45, y-180), (x,y-45), (x-45, y-45), (x+45, y-45)],[(x, y+90), (x, y+135), (x, y+180), (x+45,y+90), (x+45,y+135), (x+45, y+180), (x-45,y+90), (x-45, y+135), (x-45, y+180), (x,y+45), (x+45, y+45), (x-45, y+45)], [(x-90, y), (x-135, y), (x-180, y), (x-90,y-45), (x-135,y-45), (x-180, y-45), (x-90,y+45), (x-135, y+45), (x-180, y+45), (x-45, y), (x-45, y+45), (x-45, y-45)] ]}

        zone_s = zone[self.nom]
        zone_c = []
        coordonnees_adv = 0
        if perso.cat == "Joueur" :
            coordonnees_adv = (230, 320)
        else :
            coordonnees_adv = joueur.pstn
        for i in range(len(zone_s)):
            if coordonnees_adv in zone_s[i]:
                zone_c = zone_s[i]

        zone_sort = []
        for case in zone_c :
            if case[0] <= 635 and case[0] >= 50 and case[1] <= 635 and case[1] >= 50:
                zone_sort.append(case)

        return zone_sort

    def monstres_in_zone (self, perso, liste_monstres):
        zone_sort = self.est_zone_s(perso, Joueur)

        if perso.cat == "Joueur":
            liste_monstre_in_zone = [] #liste de monstres dans la zone d'action du sort
            for i in range(len(liste_monstres)):
                if liste_monstres[i].pstn in zone_sort:
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

        perso.pv_t = 1.05*perso.pv_t

    def defense_action(self, adv):
        """ Sort, Personnage -> void
            Préconditions : perso.pv != 0
            Rôle : Supprime les pd de l'adversaire."""
        nb = 0
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

        soin = 0
        if self.nom == "Bénédiction":
            soin = perso.pv_t*0.2
            if perso.pv + soin > perso.pv_t :
                soin = perso.pv_t - perso.pv
            perso.pv = perso.pv + soin

        if self.nom == "Illumination":
            soin = self.degats
            if perso.pv + soin > perso.pv_t :
                soin = perso.pv_t - perso.pv
            perso.pv = perso.pv + soin #degats = pv rendu



#-----------Création des sorts---------#
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

liste_case = []
for i in range (14) :
    for j in range (14) :
        c1 = (50+j*45, 50 + i*45)
        liste_case.append(c1)

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
       Rôle : Indique la position des obstacles sur le graphe de façon à ce la liaison entre un sommet contenant un obstacle et un sommet qui lui est adjacent ne soit pas possible"""
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

def definir_monstres (g, liste_monstre, liste_case, perso):
    """list, list -> void
       Préconditions : len(liste_case) == len(g) et g représente un graphe
       Rôle : Indique la position des monstres sur le graphe de façon à ce la liaison entre un sommet contenant un monstre et un sommet qui lui est adjacent ne soit pas possible"""
    c_monstre = []
    for monstre in liste_monstre :
        if not monstre.est_mort() :
            if perso.pstn != monstre.pstn:
                c_monstre.append(monstre.pstn)
    liste_o = []
    for i in range (len(c_monstre)):
        for j in range (len(liste_case)):
            if liste_case[j] == c_monstre[i]:
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

def mise_a_jour_monstre (g, liste_monstre, liste_case, perso):
    """list, list -> void
       Préconditions : len(liste_case) == len(g) et g représente un graphe
       Rôle : Indique la position des monstres sur le graphe de façon à ce la liaison entre un sommet contenant un monstre et un sommet qui lui est adjacent ne soit pas possible"""
    c_monstre = []
    for monstre in liste_monstre :
        if not monstre.est_mort() :
            if perso.pstn != monstre.pstn:
                c_monstre.append(monstre.pstn)
    liste_o = []
    for i in range (len(c_monstre)):
        for j in range (len(liste_case)):
            if liste_case[j] == c_monstre[i]:
                liste_o.append(j)
    for obstacle in liste_o :
        if obstacle > 0 :
            graphe1[obstacle][obstacle-1] = 1
            graphe1[obstacle-1][obstacle] = 1
        if obstacle < 195 :
            graphe1[obstacle][obstacle+1] = 1
            graphe1[obstacle+1][obstacle] = 1
        if obstacle < 182 :
            graphe1[obstacle][obstacle+14] = 1
            graphe1[obstacle+14][obstacle] = 1
        if obstacle > 13 :
            graphe1[obstacle][obstacle-14] = 1
            graphe1[obstacle-14][obstacle] = 1

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
    chemin.pop()
    chemin.pop(0)
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

    def __init__ (self, nom, image, categorie, pv, pv_t, pa, pd, sorts, position):
        """ self, str, png, png, str, int, int, int, dict, tuple
            Préconditions : aucune
            Rôle : Initialise les attributs de la classe Personnage"""

        self.nom = nom #pseudonyme du personnage
        self.im1 = image #image qui représente le personnage
        self.cat = categorie #statut du personnage (joueur, monstre1, monstre2, monstre3, boss)
        self.pv = pv #nombre de points de vie
        self.pv_t = pv_t #nombre de points de vie total (non variable)
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
        if self.cat == "Monstre3" or self.cat == "Boss":
            n = 2
        else :
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

                if case1[0] >= 50 and case1[0] <= 635 and case1[1] >= 50 and case1[1] <= 635 :
                    for monstre in liste_m :
                        if case1 == monstre.pstn :
                            compteur1 += 1
                    for obstacle in liste_o :
                        if case1[0] == obstacle[0] and case1[1] == obstacle[1] :
                            compteur1 += 1
                    if compteur1 == 0 :
                        zone.append(case1)

                if case2[0] >= 50 and case2[0] <= 635 and case2[1] >= 50 and case2[1] <= 635 :
                    for monstre in liste_m :
                        if case2 == monstre.pstn :
                            compteur2 += 1
                    for obstacle in liste_o :
                        if case2[0] == obstacle[0] and case2[1] == obstacle[1] :
                            compteur2 += 1
                    if compteur2 == 0 :
                        zone.append(case2)

                if case3[0] >= 50 and case3[0] <= 635 and case3[1] >= 50 and case3[1] <= 635 :
                    for monstre in liste_m :
                        if case3 == monstre.pstn :
                            compteur3 += 1
                    for obstacle in liste_o :
                        if case3[0] == obstacle[0] and case3[1] == obstacle[1] :
                            compteur3 += 1
                    if compteur3 == 0 :
                        zone.append(case3)

                if case4[0] >= 50 and case4[0] <= 635 and case4[1] >= 50 and case4[1] <= 635 :
                    for monstre in liste_m :
                        if case4 == monstre.pstn :
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
        if self.cat == "Joueur" :
            affiche_zone_p(liste_m, liste_o)
            #self.pstn = clique_case(x, y)
            # appel à une fonction qui retourne les coordoonnées de la case sur laquelle l'utilisateur a cliqué
        elif self.cat == "Monstre1":
            pd = self.pd
            definir_obstacle(graphe1, liste_o, liste_case)
            definir_monstres(graphe1, liste_m, liste_case, self)
            position_joueur = conversion_cc(Joueur.pstn, liste_case)
            position_monstre = conversion_cc(self.pstn, liste_case)
            chemin_m = chemin(graphe1, position_monstre, position_joueur, liste_case)
            while pd > 0 and len(chemin_m) > 0 :
                self.pstn = chemin_m.pop(0)
                pd = pd - 1
            mise_a_jour_monstre(graphe1, liste_m, liste_case, self)
        elif self.cat == "Monstre2":
            pd = self.pd
            definir_obstacle(graphe1, liste_o, liste_case)
            definir_monstres(graphe1, liste_m, liste_case, self)
            position_joueur = conversion_cc(Joueur.pstn, liste_case)
            position_monstre = conversion_cc(self.pstn, liste_case)
            chemin_m = chemin(graphe1, position_monstre, position_joueur, liste_case)
            while pd > 0 and len(chemin_m) > 0 :
                self.pstn = chemin_m.pop(0)
                pd = pd - 1
            mise_a_jour_monstre(graphe1, liste_m, liste_case, self)

        elif self.cat == "Monstre3":
            pd = self.pd
            while pd > 0 :
                zone_p = self.zone_possible(liste_m, liste_o)
                n = randint(0, len(zone_p)-1)
                self.pstn = (zone_p[n])
                pd = pd - 1

        else :
            pd = self.pd
            while pd > 0 :
                zone_p = self.zone_possible(liste_m, liste_o)
                n = randint(0, len(zone_p)-1)
                self.pstn = (zone_p[n])
                pd = pd - 1


    def action (self, x, y) :
        """self(Personnage) -> void
           Préconditions :
           Rôle : fait agir les sorts en fonction du type de personnage"""
        if self.cat == "Joueur" :
            n = self.pa
            while self.pa > 0 : #fonction qui détermine si le joueur a fini son tour ou non
                sort_j = clique_sort(x, y)
                sort_j.action_sort(self)
            self.pa = n
        elif self.cat == "Monstre1":
            if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sort(self)

        elif self.cat == "Monstre2":
            x = self.pstn[0]
            y = self.pstn[1]
            zone = [(x+45,y),(x, y-45),(x, y+45),(x-45,y)]
            if self.pv < 150 :
                if self.pa >= self.sorts["soin"][0].cout:
                    self.sorts["soin"][0].action_sort(self)
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sort(self)
            elif not Joueur.pstn in zone : #liste de coordonnées des cases sur lesquelles agit le sort (Lilas)
                if self.pa >= self.sorts["soin"][0].cout:
                    self.sorts["soin"][0].action_sort(self)
            else :
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sort(self)
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sort(self)

        elif self.cat == "Monstre3" :
            if self.pv < 200 :
                if self.pa >= self.sorts["soin"][0].cout :
                    self.sorts["soin"][0].action_sort(self)
                n = randint(0,1)
                if self.pa >= self.sorts["attaque"][n].cout:
                    self.sorts["attaque"][n].action_sort(self)
            else :
                n = randint(0,1)
                if self.pa >= self.sorts["attaque"][n].cout:
                    self.sorts["attaque"][n].action_sort(self)
                n = randint(0,1)
                if self.pa >= self.sorts["attaque"][n].cout:
                    self.sorts["attaque"][n].action_sort(self)
        else :
            x = self.pstn[0]
            y = self.pstn[1]
            zone = [(x+180, y), (x,y-180), (x,y+180), (x-180, y)]
            if self.pv < 300 :
                if self.pa >= self.sorts["soin"][0].cout :
                    self.sorts["soin"][0].action_sort(self)
                if self.pa >= self.sorts["attaque"][0].cout :
                    self.sorts["attaque"][0].action_sort(self)
            elif Joueur.pstn in zone: #liste de coordonnées des cases sur lesquelles agit le sort (Lilas)
                n = randint(0,2)
                if n == 0 or n == 1 :
                    if self.pa >= self.sorts["defense"][0].cout :
                        self.sorts["defense"][0].action_sort(self)
                    if self.pa >= self.sorts["attaque"][0].cout :
                        self.sorts["attaque"][0].action_sort(self)
                else :
                    if self.pa >= self.sorts["attaque"][0].cout :
                        self.sorts["attaque"][0].action_sort(self)
                    if self.pa >= self.sorts["attaque"][0].cout :
                        self.sorts["attaque"][0].action_sort(self)
            else :
                n = randint(0, 4)
                if n== 0 :
                    if self.pa >= self.sorts["defense"][1].cout :
                        self.sorts["defense"][1].action_sort(self)
                if n == 1 :
                    if self.pa >= self.sorts["soin"][0].cout :
                        self.sorts["soin"][0].action_sort(self)
                if n == 2 :
                    if self.pa >= self.sorts["defense"][1].cout :
                        self.sorts["defense"][1].action_sort(self)
                    if self.pa >= self.sorts["soin"][0].cout :
                        self.sorts["soin"][0].action_sort(self)


Joueur = Personnage("You", "joueur.png", "Joueur", 1200, 1200, 7, 4, {"attaque" : [explosion, fleches_empoisonnees], "soin" : [benediction], "defense" : [immobilisation]}, (140, 320))
monstre1_1_niv3 = Personnage("Lezardo", "monstre1.png", "Monstre1", 300, 300, 2, 1, {"attaque" : [coup_de_couteau]}, (455,95))
monstre1_2_niv3 = Personnage("Lezardo", "monstre1.png", "Monstre1", 300, 300, 2, 1, {"attaque" : [coup_de_couteau]}, (455,590))
monstre1_3_niv3 = Personnage("Lezardo", "monstre1.png", "Monstre1", 300, 300, 2, 1, {"attaque" : [coup_de_couteau]}, (230,320))
monstre2_1_niv3 = Personnage("Croco", "monstre2.png", "Monstre2", 500, 500, 3, 3, {"attaque" : [coup_de_couteau], "soin": [illumination]}, (455,320))
monstre3_1_niv3 = Personnage("Renardo", "monstre3.png", "Monstre3", 650, 650, 5, 2, {"attaque" : [coup_de_couteau2, fleches_empoisonnees], "soin": [illumination1]}, (500,140))
monstre3_2_niv3 = Personnage("Renardo", "monstre3.png", "Monstre3", 650, 650, 5, 2, {"attaque" : [coup_de_couteau2, fleches_empoisonnees], "soin": [illumination1]}, (500,545))
Boss_niv3 = Personnage("Skeleto", "Boss.png", "Boss", 900, 900, 5, 2, {"attaque" : [fleches_empoisonnees], "soin" : [illumination2], "defense" : [eclair, augmentation]}, (590,320))
liste_o = [(545,95), (230,545),(320,275),(275,545)]
liste_m = [monstre1_1_niv3, monstre1_2_niv3, monstre1_3_niv3, monstre2_1_niv3, monstre3_1_niv3, monstre3_2_niv3, Boss_niv3]

import time
import pygame
from pygame.locals import *

def affiche (Joueur, liste_m, liste_o):

    pygame.draw.rect(fenetre, (255,255,255), (0, 0, 1300, 700))

    font=pygame.font.SysFont("broadway",24,bold=False,italic=False)
    texte=font.render("Donjon Monster",2,(0,0,0))
    fenetre.blit(texte,(275,0))


    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (225,206,154), (50+90*i, 50+90*j, 45, 45))
#             n = str(50+90*i) +" , " + str (50+90*j)
#             font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
#             texte = font.render(n, 1, (0,0,0))
#             fenetre.blit(texte, (50+90*i, 50+90*j))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (225,206,154), (95+90*i, 95+90*j, 45, 45))
#             n = str(95+90*i) +" , " + str (95+90*j)
#             font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
#             texte = font.render(n, 1, (0,0,0))
#             fenetre.blit(texte, (95+90*i, 95+90*j))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (250,240,197), (95+90*i, 50+90*j, 45, 45))
#             n = str(95+90*i) +" , " + str (50+90*j)
#             font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
#             texte = font.render(n, 1, (0,0,0))
#             fenetre.blit(texte, (95+90*i, 50+90*j+20))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (250,240,197), (50+90*i, 95+90*j, 45, 45))
#             n = str(50+90*i) +" , " + str (95+90*j)
#             font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
#             texte = font.render(n, 1, (0,0,0))
#             fenetre.blit(texte, (50+90*i, 95+90*j +20))

    joueur = pygame.image.load("joueur.png").convert_alpha()
    fenetre.blit(joueur,(Joueur.pstn))

    for monstre in liste_m :
        if not monstre.est_mort():
            monstre1 = pygame.image.load(monstre.im1).convert_alpha()
            fenetre.blit(monstre1,(monstre.pstn[0],monstre.pstn[1]))

    for o in liste_o :
        pygame.draw.rect(fenetre, (49, 140, 230), (o[0],o[1], 45, 45))

    pygame.draw.rect(fenetre, (0,0,0), (725, 50, 530, 630), 4)
    pygame.draw.line(fenetre, (0,0,0), (990, 55), (990, 675), 3)


    c1 = (1005, 65)
    for i in range(len(liste_m)) :
        image = pygame.image.load(liste_m[i].im1).convert_alpha()
        fenetre.blit(image,(1005,65+i*77))
        font = pygame.font.SysFont("Aller", 18, bold = False, italic = False)
        texte = font.render(liste_m[i].nom, 1, (0,0,0))
        fenetre.blit(texte, (1005,115+i*77))
        if liste_m[i].est_mort() == False :
            pygame.draw.rect(fenetre, (255, 0, 0), (1065,85+i*77, int(((100 * liste_m[i].pv) / liste_m[i].pv_t)), 12))
            pygame.draw.rect(fenetre, (0, 0, 0), (1065,85+i*77, 100, 12), 2)
            font2 = pygame.font.SysFont("Aller", 20, bold = False, italic = False)
            t = str(liste_m[i].pv) + "/" + str(liste_m[i].pv_t)
            texte_pv = font2.render(t,1, (0,0,0))
            fenetre.blit(texte_pv, (1170, 85+i*77))
            texte_pd = font.render("PD : ", 1, (0,0,0))
            fenetre.blit(texte_pd, (1075 , 110+77*i))
            for j in range(liste_m[i].pd):
                pygame.draw.rect(fenetre, (87,213,60), (1105 +j*20, 110 + i*77, 12, 12))
            for j in range(liste_m[i].pd):
                pygame.draw.rect(fenetre, (0,0,0), (1105 +j*20, 110 + i*77, 12, 12),2)
        else :
            font1 = pygame.font.SysFont("Aller", 20, bold = False, italic = False)
            texte_d = font1.render("DEAD",1, (0,0,0))
            fenetre.blit(texte_d, (1100, 85+i*77))
            font2 = pygame.font.SysFont("Aller", 20, bold = False, italic = False)
            t = "0" + "/" + str(liste_m[i].pv_t)
            texte_pv = font2.render(t,1, (0,0,0))
            fenetre.blit(texte_pv, (1170, 85+i*77))

    image_joueur = pygame.image.load("joueur.png").convert_alpha()
    fenetre.blit(image_joueur,(740, 65))
    font = pygame.font.SysFont("Aller", 22, bold = False, italic = False)
    texte = font.render(Joueur.nom, 1, (0,0,0))
    fenetre.blit(texte, (800,80))
    pygame.draw.rect(fenetre, (255, 0, 0), (740, 125, int(160*((100 * Joueur.pv) / Joueur.pv_t)/100), 12))
    pygame.draw.rect(fenetre, (0, 0, 0), (740, 125, 160, 12), 2)
    font2 = pygame.font.SysFont("Aller", 20, bold = False, italic = False)
    t = str(Joueur.pv) + "/" + str(Joueur.pv_t)
    texte_pv = font2.render(t,1, (0,0,0))
    fenetre.blit(texte_pv, (910, 125))
    texte_pd = font.render("PD : ", 1, (0,0,0))
    texte_pa = font.render("PA : ", 1, (0,0,0))
    fenetre.blit(texte_pd, (740, 155))
    fenetre.blit(texte_pa, (740, 185))
    for i in range(Joueur.pd):
        pygame.draw.rect(fenetre, (87,213,60), (780 +i*20, 155, 12, 12))
    for i in range(Joueur.pa):
        pygame.draw.rect(fenetre, (223,160,220), (780 +i*20, 185, 12, 12))
    for i in range(4):
        pygame.draw.rect(fenetre, (0,0,0), (780 +i*20, 155, 12, 12),2)
    for i in range(7):
        pygame.draw.rect(fenetre, (0,0,0), (780 +i*20, 185, 12, 12),2)

    texte_s_a = font.render("Sorts d'attaque : ", 1, (0,0,0))
    fenetre.blit(texte_s_a, (740, 215))
    for i in range (len(Joueur.sorts["attaque"])):
        pygame.draw.rect(fenetre, (45,78,98), (740, 240+ i*50, 35, 35))
        texte_ns = font2.render(Joueur.sorts["attaque"][i].nom,1, (0,0,0))
        fenetre.blit(texte_ns, (790, 240+i*50))
        for j in range (Joueur.sorts["attaque"][i].cout):
            pygame.draw.rect(fenetre, (223,160,220), (790 +j*20, 260+ i*50, 12, 12))
            pygame.draw.rect(fenetre, (0,0,0), (790 +j*20, 260+ i*50, 12, 12),2)
    texte_s_a = font.render("Sorts de soin : ", 1, (0,0,0))
    fenetre.blit(texte_s_a, (740, 345))
    for i in range (len(Joueur.sorts["soin"])):
        pygame.draw.rect(fenetre, (45,78,98), (740, 370+ i*50, 35, 35))
        texte_ns = font2.render(Joueur.sorts["soin"][i].nom,1, (0,0,0))
        fenetre.blit(texte_ns, (790, 370+i*50))
        for j in range (Joueur.sorts["attaque"][i].cout):
            pygame.draw.rect(fenetre, (223,160,220), (790 +j*20, 390+ i*50, 12, 12))
            pygame.draw.rect(fenetre, (0,0,0), (790 +j*20, 390+ i*50, 12, 12),2)
    texte_s_a = font.render("Sorts de défense : ", 1, (0,0,0))
    fenetre.blit(texte_s_a, (740, 425))
    for i in range (len(Joueur.sorts["defense"])):
        pygame.draw.rect(fenetre, (45,78,98), (740, 450+ i*50, 35, 35))
        texte_ns = font2.render(Joueur.sorts["defense"][i].nom,1, (0,0,0))
        fenetre.blit(texte_ns, (790, 450+i*50))
        for j in range (Joueur.sorts["defense"][i].cout):
            pygame.draw.rect(fenetre, (223,160,220), (790 +j*20, 470+ i*50, 12, 12))
            pygame.draw.rect(fenetre, (0,0,0), (790 +j*20,470+ i*50, 12, 12),2)


def clique_case (x, y):
    zone = Joueur.zone_possible(liste_m, liste_o)
    for c in zone:
        if x >= c[0] and x < c[0] + 45 :
            if y >= c[1] and y < c[1] + 45:
                return c

def clique_sort (x, y):
    coordonnees_sort = [[explosion, (740, 240)], [fleches_empoisonnees, (740, 290)], [benediction, (740,370)], [immobilisation, (740, 450)]]
    for sort in coordonnees_sort:
        if x >= sort[1][0] and x < sort[1][0] + 35 :
            if y >= sort[1][1] and y < sort[1][1] + 35:
                    return sort[0]

def clique_monstre (liste_m, x1, y1) :
    c_monstre = 0
    coordonnees_monstre = []
    for monstre in liste_m :
        if not monstre.est_mort() :
            coordonnees_monstre.append(monstre.pstn)
    for i in range(len(coordonnees_monstre)):
        if x1 >= coordonnees_monstre[i][0] and x1 <= coordonnees_monstre[i][0] + 45 :
            if y1 >= coordonnees_monstre[i][1] and y1 <= coordonnees_monstre[i][1] + 45:
                c_monstre = coordonnees_monstre[i]
    for monstre in liste_m :
        if monstre.pstn == c_monstre :
            return monstre

def affiche_zone_p (liste_m, liste_o):
    zone_p = Joueur.zone_possible(liste_m, liste_o)
    for case in zone_p :
        pygame.draw.rect(fenetre, (97, 75, 68), (case[0], case[1], 45, 45), 2)
    joueur = pygame.image.load("joueur.png").convert_alpha()
    fenetre.blit(joueur,(Joueur.pstn))
    pygame.display.flip()

def ordre_de_passage(joueur, liste_m):
    """ Personnage, list[Personnage] -> list[Personnage]
        Précondition : None
        Rôle : En début de tour crée une liste qui définit l'ordre dans lequel les personnages jouent. """

    liste_passage = [joueur]
    for monstre in liste_m :
        if not monstre.est_mort():
            liste_passage.append(monstre)
    return liste_passage

def tour_personnage(joueur, liste_m, liste_o) :
    """ Personnage, list[Personnage] - void
        Précondition : None
        Rôle : Fais jouer chaque personnage. """

    liste_passage = ordre_de_passage(joueur, liste_m)
    for personnage in liste_passage:
        if personnage.cat == "Joueur" :
            joueur.deplacer(liste_m, liste_o)
            affiche(joueur, liste_m, liste_o)
            pygame.display.flip()
            joueur.action()
            affiche(joueur, liste_m, liste_o)
            pygame.display.flip()
        else :
            monstre.deplacer(liste_m, liste_o)
            affiche(joueur,liste_m,liste_o)
            pygame.display.flip()
            monstre.action(0,0)
            affiche(joueur,liste_m,liste_o)
            pygame.display.flip()
            time.sleep(1)


# def tour_joueur (joueur, liste_m, liste_o):
#     """Personnage, list, list -> void
#        Préconditions :
#        Rôle  Fait joueur le joueur"""
#
#     joueur.deplacer(liste_m, liste_o)
#     affiche(Joueur,liste_m,liste_o)
#     pygame.display.flip()
# #     joueur.action(x, y)
# #     affiche(Joueur,liste_m,liste_o)
# #     pygame.display.flip()
#     j = False
#
# def tour_monstres (liste_m, liste_o):
#     for monstre in liste_m :
#         if not monstre.est_mort() :
#             monstre.deplacer(liste_m, liste_o)
#             affiche(Joueur,liste_m,liste_o)
#             pygame.display.flip()
#             monstre.action(0,0)
#             affiche(Joueur,liste_m,liste_o)
#             pygame.display.flip()
#             time.sleep(1)

def victoire(joueur, liste_adversaire):
    """ Personnage, list -> bool
        Préconditions : None
        Rôle : Rôle : Si le joueur a des pv (est en vie, (pv > 0)) et que tout les monstres n'ont plus de pv (sont morts, (pv <= 0)) retourner TRUE, si tout les monstres ne sont pas morts retourne "continue", sinon retourner FALSE. """

    nb_mort = 0
    if joueur.est_mort(): # défaite
        return False
    else: # victoire
        for adversaire in liste_adversaire:
            if adversaire.est_mort():
                nb_mort += 1
        if nb_mort == len(liste_adversaire):
            return True
        return "continue" # le joueur peut continuer de jouer mais tout les monstres ne sont pas morts.

def jeu (joueur, liste_m, liste_o):
    continuer = True
    j = True
    while continuer == True :
        if j == True :
            tour_joueur(joueur, liste_m, liste_o)
        if j == False :
            tour_monstres(liste_m, liste_o)
        if joueur.est_mort():
            continuer = False
        n = 0
        for monstre in liste_m :
            if monstre.est_mort() :
                n = n + 1
        if n == len(liste_m) :
            continuer = False
    victoire(joueur, liste_m)


def affichage_accueil():
    """ Précondition : None
        Rôle : Affiche l'accueil du jeu. """

    font_big = pygame.font.Font("neuropolitical.ttf", 50)

    pygame.draw.rect(fenetre, (200,250,45), (100, 100, largeur-200, hauteur-200)) #rectangle accueil
    pygame.draw.rect(fenetre, (0,0,0), (100, 100, largeur-200, hauteur-200), 2) #cadre accueil
    pygame.draw.rect(fenetre, (200, 100, 45), (525, 380, 250, 100)) # rectangle jouer
    pygame.draw.rect(fenetre, (0,0,0), (525, 380, 250, 100), 2) #cadre jouer
    texte_titre = pygame.font.Font.render(font_big, "DONJON MONSTER", True, (0,0,0))
    texte_jouer = pygame.font.Font.render(font_big, "JOUER", True, (0,0,0))

    #affichage des textes
    fenetre.blit(texte_titre, (370, 210))
    fenetre.blit(texte_jouer, (550, 400))

    # if event.type==MOUSEBUTTONDOWN :
    #     (x, y) = event.pos
    #     if x <= 775  and y <= 480 :
    #         if x >= 525  and y >= 380 :
    #             #lancer le niveau

def affichage_victoire_defaite(joueur, liste_m): #affichage vitcoire/defaite
    """ Personnage, list[Personnage] ->  void
        Précondition : None
        Rôle : Affiche un pop qui affiche "défaite" ou "victoire" et pose une question au joueur qui peut répondre par "oui" ou "non". """

    #police d'ecriture
    font = pygame.font.SysFont("lemon_friday.ttf", 50)
    font1_big = pygame.font.Font("neuropolitical.ttf", 50)
    font1_small = pygame.font.Font("neuropolitical.ttf", 30)
    font2_big = pygame.font.Font("Bloodthirsty.ttf", 70)
    font2_small = pygame.font.Font("Bloodthirsty.ttf", 45)

    #texte commun aux deux pop-up
    texte_reponse1 = pygame.font.Font.render(font, "Oui", True, (0,0,0))
    texte_reponse2 = pygame.font.Font.render(font, "Non", True, (0,0,0))

    # var = False
    # if var:
    if  victoire(joueur, liste_m):
        pygame.draw.rect(fenetre, (145, 123, 198), (140, 185, 1000, 280)) # pop up niveau suivant (victoire)
        pygame.draw.rect(fenetre, (130, 80, 100), (275, 365, 200, 50)) # rectangle réponse 1
        pygame.draw.rect(fenetre, (130, 80, 100), (770, 365, 200, 50)) # rectangle réponse 2
        texte_victoire = pygame.font.Font.render(font1_big, "VICTOIRE", True, (0,0,0))
        texte_question1 = pygame.font.Font.render(font1_small, "Souhaitez-vous passer au niveau suivant ?", True, (0,0,0))
        #affichage de tout les textes
        fenetre.blit(texte_victoire, (475, 200))
        fenetre.blit(texte_question1, (220, 275))
        fenetre.blit(texte_reponse1, (340, 375))
        fenetre.blit(texte_reponse2, (835, 375))

    # var = True
    # if var:
    if victoire(joueur, liste_m) == False:
        pygame.draw.rect(fenetre, (203, 67, 67), (140, 185, 1000, 280)) # pop up dead (défaite)
        pygame.draw.rect(fenetre, (130, 80, 100), (275, 365, 200, 50)) # rectangle réponse 1
        pygame.draw.rect(fenetre, (130, 80, 100), (770, 365, 200, 50)) # rectangle réponse 2
        texte_defaite = pygame.font.Font.render(font2_big, "DEFAITE", True, (0,0,0))
        texte_question2 = pygame.font.Font.render(font2_small, "Souhaitez-vous recommencer le niveau ?", True, (0,0,0))
        #affichage de tout les textes
        fenetre.blit(texte_defaite, (515, 200))
        fenetre.blit(texte_question2, (230, 285))
        fenetre.blit(texte_reponse1, (340, 375))
        fenetre.blit(texte_reponse2, (835, 375))

        #contours des rectangles
    pygame.draw.rect(fenetre, (0, 0, 0), (140, 185, 1000, 280), 2) # cadre vitcoire/défaite
    pygame.draw.rect(fenetre, (0, 0, 0), (275, 365, 200, 50), 2) # cadre réponse 1
    pygame.draw.rect(fenetre, (0, 0, 0), (770, 365, 200, 50), 2) # cadre réponse 2


# while continuer :
#     for event in pygame.event.get(): # on prend le premier événement de la pile
#
#         #réponse = oui
#     if event.type==MOUSEBUTTONDOWN :
#         (x, y) = event.pos
#         if x <= 475 and y <= 415 :
#             if x >=275  and y >=365 :
#                 return "Oui"
#
#         #réponse = non
#         if event.type==MOUSEBUTTONDOWN :
#             (x, y) = event.pos
#             if x <= 970 and y <= 415 :
#                 if x >= 770 and y >=365 :
#                     return "Non"

def tour_par_tour(joueur, liste_m, liste_o):
    """ Personnage, list[Personnage], list[2-uplet] -> void
        Préconditions : None
        Rôle : Appel chaque fonction du gestionnaire des tâches pour mettre à jour les évenements et fait jouer le personnage suivant. """

    statut_victoire = victoire(joueur, liste_m) # True, False, "continue"
    if statut_victoire == "continue" :
        #ordre de liste de passage / conditions de qui joue ou non
        tour_monstres(liste_m, liste_o)
        tour_joueur(joueur, liste_m, liste_o)

        #actualise les paramètres et passe au personnage suivant
    if victoire(): #victoire
        reponse = affichage_victoire_defaite(joueur, liste_m)
        if reponse == "Oui" :
            #lance le niveau suivant
            # option : propose une récompense
        else:
            affichage_accueil()
    else : #défaite
        reponse = affichage_victoire_defaite(joueur, liste_m)
        if reponse == "Oui" :
            #relance le niveau
        else :
            affichage_accueil()




pygame.init()
largeur = 1300
hauteur = 700
try :

    fenetre = pygame.display.set_mode((largeur, hauteur))

    liste_o = [(545,95), (230,545),(320,275),(275,545)]

    liste_m = [monstre1_1_niv3, monstre1_2_niv3, monstre1_3_niv3, monstre2_1_niv3, monstre3_1_niv3, monstre3_2_niv3, Boss_niv3]

    affiche(Joueur,liste_m,liste_o)
    tour_monstres(liste_m, liste_o)
    #affichage_victoire_defaite(joueur, liste_m)
    pygame.display.flip()


    continuer = True
    while continuer :
        for event in pygame.event.get(): # on prend le premier événement de la pile
            if event.type==QUIT: # clic sur la croix "fermeture de fenetre"
                continuer = False

            elif event.type == MOUSEBUTTONDOWN :
                (x, y) = event.pos
                #jeu(Joueur, liste_m, liste_o)
#             if event.type==MOUSEBUTTONDOWN :
#                  (x,y)=event.pos
#                  l=y//45
#                  c=x//45
#                  Joueur.pstn=(c*45,l*45)
#         fenetre.blit(joueur,(Joueur.pstn))

finally :
    pygame.quit()
