# Donjon-Monster
    Projet : Cahier des Charges 
    
Membres du groupe : 
- Lilas Ontaneda 
- Vignon Manon 
- Krishnakumar Regina 

Titre du Projet : 
- Donjon Monster! 

Court descriptif du projet : 
C’est un jeu basé sur le jeu Wakfu. 
Un personnage manipulé par un joueur possède plusieurs pouvoirs qui lui sont automatiquement attribués (soin, attaque, défense) et plusieurs possibilités de déplacement sur une carte quadrillée. 
Le but étant de battre des monstres qui ont eux-mêmes différents pouvoirs et possibilités de déplacement sur la grille (en fonction de leur catégorie) en leur faisant perdre tous leurs points de vie. Le jeu se décompose en 3 niveaux accessibles seulement en cas de victoire du niveau précédent. Si le joueur perd un niveau, il peut le recommencer sans devoir repasser par les niveaux précédents. 
Le jeu est codé en tour par tour, pour chaque action le personnage peut se déplacer et/ou ensuite utiliser ses pouvoirs, pour cela il dispose de points de déplacement qui lui permettent de franchir autant de cases (hors diagonale) que de points dont il dispose, c’est le même système pour les sorts, chaque sort a un coût, le joueur peut en utiliser autant que sa jauge de points d’action le lui permet. De plus, les monstres comme le joueur disposent de points de vie, variables selon la catégorie du monstre. Si le joueur perd tous ses points de vie, il a perdu. Pour utiliser un sort, ou se déplacer sur la grille, le joueur devra cliquer sur la case où il souhaite aller ou sur le sort qu’il souhaite utiliser. A chaque début de partie, le joueur est automatiquement envoyé sur une case de la grille et peut voir où se situent les monstres avant que le combat ne commence. A chaque victoire, le joueur obtient une récompense (points d’action supplémentaires, points de vie ou points de déplacement) qu’il ne conserve pas en cas de défaite. 

Schéma annoté de l’interface graphique : /

Éléments à programmer : 

Classe Personnage: 
Attributs : 
- nom (str), pseudonyme du personnage 
- image1 (png), associe une image au personnage 
- image2 (png), associe une image au personnage dans laquelle il se fait attaquer 
- categorie (str), définit le statut du personnage (joueur, monstre1, monstre2, monstre3, boss) 
- pv (int), nombre de points de vie 
- pa (int), les points d’action servent à utiliser les sorts
- pd (int), le nombre de points de déplacement est égal au nombre de cases que peut franchir le personnage à chaque tour 
- sorts (dict), les clés représentent les types de sorts (attaque, soin, défense) et les valeurs représentent les sorts stockés dans des listes 
- position(tuple), coordonnées (x,y) du personnage 
Méthode : 
constructeur 
est_mort (personnage): 
Personnage -> bool 
Retourne True si le personnage n’a plus de pv, False sinon. 
deplacer(personnage) : 
personnage(Personnage) -> void 
- on teste le statut du personnage : 
→ joueur : 
illumine les cases sur lesquelles le joueur peut se déplacer en fonction de ses pd et de sa position initiale, 
Demande à l’utilisateur de cliquer sur la case qu’il veut atteindre 
Modifie la position du joueur en fonction de la requête de l’utilisateur 
Change l’attribut position en fonction de la nouvelle position 
→ monstre : 
Modifie la position du monstre en fonction de ses pd (le monstre ne doit pas se déplacer de la même façon à chaque tour mais doit toujours avoir comme stratégie de viser le joueur) 
Deux personnages ne peuvent se trouver sur la même case et un personnage ne peut se déplacer sur une case contenant un obstacle. 
Change l’attribut position en fonction de la nouvelle position 
action(personnage) : 
personnage → void 
- on teste le statut du personnage : 
→ joueur :
- le joueur choisit un sort 
- les cases à portée de tir s’illuminent 
- il peut choisir un adversaire 
- appel à la classe sort pour actionner le sort sélectionné 
→ monstre1 
→ monstre2 
-> monstre3 
-> Boss 
(les monstres auront des stratégies d’action différentes selon leur catégorie, par exemple un monstre de catégorie 2 pourra se voir attribuer un sort d’attaque et un sort de soin, et devra utiliser son sort de soin si son nombre de pv est inférieur à 50 sinon il attaquera) 

    Classe Sort : 
Attributs : 
- nom (str) 
- degats (int) : nombre de pv retirés par le sort 
- type (str) : attaque, soin, défense 
- cout (int) : nombre de pa utilisé par le sort
- description (str) : description du sort 

Fonctions/Méthodes:
        constructeur

        action_sort(self,perso , adv):
        """ self, Personnage, Personnage -> void
                     Préconditions : self.pv != 0
                     Rôle : En fonction du type du sort, lance le sort sur l'adversaire ou le joueur correspondant. """

        
        def est_zone(self, perso, liste_monstres):
        """ Personnage, list[Personnage], Sort -> list
            Préconditions : None
            Rôle : Détermine si un ou plusieurs monstres se trouve dans la zone d'action du sort et renvoit False si la liste de monstres est vide sinon la liste de               coordonnées des monstres dans la zone. """
            
        attaque / augmentation / defense / soin 

Variables Globales : 
liste_monstres1 : list(Personnage) : liste des monstres du niveau 1 
liste_monstres2 : list(Personnage) : liste des monstres du niveau 2 
liste_monstres3 : list(Personnage) : liste des monstres du niveau 3 
Joueur(Personnage): Personnage du Joueur 
liste_sort : list(Sort) liste des sorts possibles 
Graphe1 : Grille de jeu du niveau 1, 2 et 3
Barre1 : Barre de tâche (graphique) du niveau 1 
Barre2 : Barre de tâche (graphique) du niveau 2 
Barre3 : Barre de tâche (graphique) du niveau 3 
Fenêtre : fenêtre de l’interface Graphique 

Interface Graphique : 
Fonctions: 

barre_user(): 
Modifier graphiquement la barre de tâches entre chaque tour pour afficher les changements nécessaires (pa, pv) 

description_sort(liste_sorts): 
liste_sorts(list) -> void 
Rôle : Créer une fenêtre avec la description de chaque sort si l’utilisateur clique sur le bouton destiné à l’afficher. 

affichage_sort(sort, perso):
sort (Sort), adversaire(Personnage) -> void 
Rend visible les dégâts à l’aide d’une animation : change l’image du monstre touché par une autre où il est attaqué, cette fonction est utilisée lorsque le sort en paramètre n’est pas un sort de soin, lorsque le sort a des effets directs sur l’adversaire du personnage en paramètre. 



Gestionnaire d'evenements: 

    def tour_par_tour(joueur):
    """ Personnage -> void
        Préconditions : None
        Rôle : Appel chaque fonction du gestionnaire des tâches pour mettre à jour les évenements et fait jouer le personnage suivant. """
        
    def victoire(joueur, liste_adversaire):
    """ Personnage, list -> bool
        Préconditions : None
        Rôle : Si le joueur a des pv (est en vie, (pv > 0)) et que tout les monstres n'ont plus de pv (sont morts, (pv <= 0)) retourner TRUE, si tout les monstres ne         sont pas morts retourne "continue", sinon retourner FALSE. """

recompense(): 
Aucun paramètre 
Rôle : Le joueur choisit entre deux cadeaux avant de passer au niveau suivant. Modification de la fenêtre graphique, le joueur clique sur la récompense souhaitée. Modification des attributs du joueur en conséquence. 


Grande étapes du programme (partie principale) : 
- Initialisation des variables dans les classes 
- Initialisation de Pygame et création de la fenêtre graphique: 
- Disposition des personnages pour chaque niveau 
- Affichage de la barre d’utilisateur 
- Gestionnaire d'événement, faisant appel aux différentes fonctions de déplacement et de sort en fonction de l'événement. 

Fonctions optionnelles : 
- Choix de l’image pour l’utilisateur 

Répartition du travail : 
- Manon : Classe Personnage 
- Lilas : Classe Sort, Gestionnaire d'évenements
- Regina : Partie Graphique
