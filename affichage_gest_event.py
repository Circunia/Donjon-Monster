import pygame
from pygame.locals import *
pygame.init()
largeur = 1300
hauteur = 700

x = 320
y = 320

#zone = [[(x, y-45)], [(x-45,y)], [(x, y+45)],[(x+45,y)]]


try :
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.draw.rect(fenetre, (255,255,255), (0, 0, 1300, 700))


    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (225,206,154), (50+90*i, 50+90*j, 45, 45))
            n = str(50+90*i) +" , " + str (50+90*j)
            font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
            texte = font.render(n, 1, (0,0,0))
            fenetre.blit(texte, (50+90*i, 50+90*j))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (225,206,154), (95+90*i, 95+90*j, 45, 45))
            n = str(95+90*i) +" , " + str (95+90*j)
            font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
            texte = font.render(n, 1, (0,0,0))
            fenetre.blit(texte, (95+90*i, 95+90*j))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (250,240,197), (95+90*i, 50+90*j, 45, 45))
            n = str(95+90*i) +" , " + str (50+90*j)
            font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
            texte = font.render(n, 1, (0,0,0))
            fenetre.blit(texte, (95+90*i, 50+90*j+20))

    for i in range (7):
        for j in range (7):
            pygame.draw.rect(fenetre, (250,240,197), (50+90*i, 95+90*j, 45, 45))
            n = str(50+90*i) +" , " + str (95+90*j)
            font = pygame.font.SysFont("Aller", 17, bold = False, italic = False)
            texte = font.render(n, 1, (0,0,0))
            fenetre.blit(texte, (50+90*i, 95+90*j +20))



    #crée un cadre avec deux carrée où est possé une question à deux réponses
    #creations des rectangles
    surface_victoire = pygame.draw.rect(fenetre, (145, 123, 198), (140, 185, 1000, 280)) # pop up niveau suivant (victoire)
    surface_defaite = pygame.draw.rect(fenetre, (203, 67, 67), (140, 185, 1000, 280)) # pop up dead (défaite)

    pygame.draw.rect(fenetre, (0, 0, 0), (140, 185, 1000, 280), 2) # cadre
    surface_reponse1 = pygame.draw.rect(fenetre, (130, 80, 100), (275, 365, 200, 50)) # réponse 1
    surface_reponse2 = pygame.draw.rect(fenetre, (130, 80, 100), (770, 365, 200, 50)) # réponse 2
    pygame.draw.rect(fenetre, (130, 80, 100), (275, 365, 200, 50), 2) # cadre réponse 1
    pygame.draw.rect(fenetre, (130, 80, 100), (770, 365, 200, 50), 2) # cadre réponse 2

    #police d'ecriture
    font = pygame.font.SysFont("arial", 30)
    font1_big = pygame.font.Font("neuropolitical.ttf", 50)
    font1_small = pygame.font.Font("neuropolitical.ttf", 30)
    font2 = pygame.font.Font("Bloodthirsty.ttf", 50)

    texte_reponse1 = pygame.font.Font.render(font, "Oui", True, (0,0,0))
    texte_reponse2 = pygame.font.Font.render(font, "Non", True, (0,0,0))

    #if victoire():
    var = True
    if var:
        texte_victoire = pygame.font.Font.render( font1_big, "VICTOIRE", True, (0,0,0))
        texte_question1 = pygame.font.Font.render(font1_small, "Souhaitez-vous passer au niveau suivant ?", True, (0,0,0))
        fenetre.blit(texte_victoire, (475, 200))
        fenetre.blit(texte_question1, (220, 270))
        fenetre.blit(texte_reponse1, (350, 370))
        fenetre.blit(texte_reponse2, (845, 370))

    var = False
    #if victoire() == False:
    if var:
        texte_victoire = pygame.font.Font.render( font2, "DEFAITE", True, (0,0,0))
        texte_question2 = pygame.font.Font.render(font2, "Souhaitez-vous recommencer le niveau ?", True, (0,0,0))
        fenetre.blit(texte_question2, )
        fenetre.blit(texte_question2, )
        fenetre.blit(texte_reponse1, )
        fenetre.blit(texte_reponse2, surface_reponse2)


    # pos_question1 = surface_victoire.get_rect()
    # surface_victoire.blit(question1, pos_question1)


    # img_question1 = font.render(question1 , True, RED)




#    if event.type==MOUSEBUTTONDOWN :
#            (x, y) = event.pos
#            #if x <= 250 and y <= 350 : position du carré 1
#                if x >= 275 and y >=365 :
#                    pygame.font()
#                    pygame.display.flip()
#
#    if event.type==MOUSEBUTTONDOWN :
#            (x, y) = event.pos
#            #if x <= 250 and y <= 350 :  position du carré 2
#                if x >= 770 and y >=365 :


    pygame.display.flip()

#    for case in zone:
#        pygame.draw.rect(fenetre, (100,140,130), (case[0][0],case[0][1], 45, 45))
#    pygame.draw.rect(fenetre, (200,240,230), (x,y, 45, 45))

    #pygame.display.flip()
    continuer = True
    while continuer :
        for event in pygame.event.get():
            if event.type == QUIT :
                continuer = False

finally :
    pygame.quit()
