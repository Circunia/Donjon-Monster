from random import randint

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
        return zone_p #retourne une liste de cases (avec leurs coordonnées) sur lesquelles le joueur peut se déplacer
                      # en fonction de ses pd
        
        
    def deplacer(self, liste_m, liste_o):
        """self(Personnage), list, list -> void
           Préconditions : le personnage pris en paramètre doit être en vie.
           Rôle : Change la position du personnage en fonction de ses pd et de la requête
                  de l'utilisateur si le personnage est le joueur."""
        if self.cat == "Joueur" :
            zone = self.zone_possible(liste_m, liste_o)
                self.pstn =   # appel à une fonction qui retourne les coordoonnées de la case sur laquelle l'utilisateur a cliqué
        elif self.cat == "Monstre1":
            position_joueur = conversion_cc(Joueur.pstn, liste_case)
            position_monstre = conversion_cc(self.pstn, liste_case)
            chemin_m = chemin(grille, position_monstre, position_joueur, liste_case)
            while self.pd > and len(chemin_m) > 0 :
                self.pstn = chemin_m.pop(0)
                self.pd = self.pd - 1
        elif self.cat == "Monstre2":
            position_joueur = conversion_cc(Joueur.pstn, liste_case)
            position_monstre = conversion_cc(self.pstn, liste_case)
            chemin_m = chemin(grille, position_monstre, position_joueur, liste_case)
            while self.pd > and len(chemin_m) > 0 :
                self.pstn = chemin_m.pop(0)
                self.pd = self.pd - 1
        elif self.cat == "Monstre3":
            zone_p = self.zone_possible(liste_m, liste_o)
            for i in range(self.pd):
                n = randint(0, len(zone_p))
                self.pstn = (zone_p[n][0], zone_p[n][1])
                self.pd = self.pd - 1
            
        else : 
            zone_p = self.zone_possible(liste_m, liste_o)
            for i in range(self.pd):
                n = randint(0, len(zone_p))
                self.pstn = (zone_p[n][0], zone_p[n][1])
                self.pd = self.pd - 1
            
    
    def action (self) :
        """self(Personnage) -> void
           Préconditions :
           Rôle : fait agir les sorts en fonction du type de personnage"""
        if self.cat == "Joueur" :
            while self.pa > 0 and #fonction qui détermine si le joueur a fini son tour ou non
            sort_j = #appel à la fonction qui sélectionne le sort sur lequel le joueur a cliqué
            monstre = #appel à la fonction qui sélectionne le monstre sur lequel le joueur 
            sort_j.action_sorts(self, monstre)
        elif self.cat == "Monstre1":
            if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
            
        elif self.cat == "Monstre2":
            if self.pv < : #seuil à déterminer
                if self.pa >= self.sorts["soin"][0].cout:
                    self.sorts["soin"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
            elif not Joueur.pstn in : #liste de coordonnées des cases sur lesquelles agit le sort (Lilas)
                if self.pa >= self.sorts["soin"][0].cout:
                    self.sorts["soin"][0].action_sorts(self, Joueur)
            else :
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout:
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
                    
        elif self.cat == "Monstre3" :
            if self.pv < : #seuil à déterminer
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
            if self.pv < : #seuil à déterminer
                if self.pa >= self.sorts["soin"][0].cout :
                    self.sorts["soin"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout :
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
            elif Joueur.pstn in : #liste de coordonnées des cases sur lesquelles agit le sort (Lilas)
                n = randint(0,1)
                if n == 0 :
                    if self.pa >= self.sorts["defense"][0].cout :
                        self.sorts["defense"][0].action_sorts(self, Joueur)
                else :
                    if self.pa >= self.sorts["attaque"][0].cout :
                        self.sorts["attaque"][0].action_sorts(self, Joueur)
            else :
                if self.pa >= self.sorts["attaque"][0].cout :
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
                if self.pa >= self.sorts["attaque"][0].cout :
                    self.sorts["attaque"][0].action_sorts(self, Joueur)
                    
            
        
    
        
        
        
