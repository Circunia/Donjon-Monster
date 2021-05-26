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
    pygame.draw.rect(fenetre, (203, 67, 67), (140, 185, 1000, 300)) # pop up dead (défaite)
    #pygame.draw.rect(fenetre, (145, 123, 198), (140, 185, 1000, 300)) # pop up niveau suivant (victoire)

    pygame.draw.rect(fenetre, (0, 0, 0), (140, 185, 1000, 300), 2) # cadre
    pygame.draw.rect(fenetre, (130, 80, 100), (275, 365, 200, 80)) # réponse 1
    pygame.draw.rect(fenetre, (130, 80, 100), (770, 365, 200, 80)) # réponse 2
    pygame.draw.rect(fenetre, (130, 80, 100), (275, 365, 200, 80), 2) # cadre réponse 1
    pygame.draw.rect(fenetre, (130, 80, 100), (770, 365, 200, 80), 2) # cadre réponse 2

    #pygame.font.init()  non nécessaire ?
    SysFont = pygame.font.get_default_font()
    question1 = pygame.font.SysFont("Souhaitez-vous continuer ?", 100)
    # reponse1 = pygame.font.SysFont("Oui", 30)
    # reponse2 = pygame.font.SysFont("Non", 30)
    img_question1 = font.render(question1 , True, RED)

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

    pygame.display.flip()
    continuer = True
    while continuer :
        for event in pygame.event.get():
            if event.type == QUIT :
                continuer = False

finally :
    pygame.quit()
