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
        
    def deplacer(self, liste_m, liste_o):
        """self(Personnage) -> void
           Préconditions : le personnage pris en paramètre doit être en vie.
           Rôle : Change la position du personnage en fonction de ses pd et de la requête
                  de l'utilisateur si le personnage est le joueur."""
        if self.cat == "Joueur" :
            xj = self.pstn[0]
            yj = self.pstn[1]
            zone_p = []
            l_case = 25
            zone_p.append((xj, yj))
            for i in range (0, self.pd + 1):
                for j in range (0, self.pd + 1):
                    case1 = (xj + (i * case), yj + (j * case))
                    case2 = (xj - (i * case), yj - (j * case))
                    if case1[0] >= 50 and case1[0] <= 400 and case1[1] >= 50 and case1[1] <= 400 :
                        for monstre in liste_m :
                            if case1[0] != monstre.pstn[0] and case1[1] != monstre.pstn[1] :
                                for obstacle in liste_o :
                                    if case1[0] != obstacle[0] and case1[1] != obstacle[1] :
                                        zone_p.append(case1)
                    if case2[0] >= 50 and case2[0] <= 400 and case2[1] >= 50 and case2[1] <= 400 :
                        for monstre in liste_m :            
                            if case2[0] != monstre.pstn[0] and case2[1] != monstre.pstn[1] :
                                for obstacle in liste_o :
                                    if case2[0] != obstacle[0] and case2[1] != obstacle[1] :
                                        zone_p.append(case2)
            return zone_p #retourne une liste de cases (avec leurs coordonnées) sur lesquelles le joueur peut se déplacer
                          # en fonction de ses pd
            while self.pd > 0 and #appel à une fonction qui permet à l'utilisatuer de cliquer sur un bouton si il a fini son action :
                self.pstn =   # appel à une fonction qui retourne les coordoonnées de la case sur laquelle l'utilisateur a cliqué
                self.pd = self.pd - 1
            
                                      
        elif self.cat == "Monstre1":
            
            
            
        elif self.cat == "Monstre2":
        elif self.cat == "Monstre3":
        else :
    
    def chemin_min (self, joueur) :
        x = self.pstn[0]
        y = self.pstn[1]
        xj = joueur.pstn[0]
        yj = joueur.pstn[1]
        case = 25
        if y == yj and x + case == xj :
            self.pstn = (x,y)
        elif y == yj and x - case == xj :
            self.pstn = (x,y)
        elif x == xj and y + case == yj :
            self.pstn = (x,y)
        elif x == xj and y - case == yj :
            self.pstn = (x,y)
        else :
            if self.pd > 0 :
                
        
        
        
