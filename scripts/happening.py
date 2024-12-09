import pygame

from scripts.entite import Joueur

class Happening_list:
    def __init__(self):
        self.modif = 1
        self.joueur = Joueur
    def lent(self, joueur):
        joueur.vit = 2
class Happenning:
    def __init__(self,jeu):
        self.jeu = jeu
        self.skin = pygame.image.load('img/joueur.png')
        self.skin.set_colorkey((237,28,36))
        self.pos =[]
        self.activable =[True,True,True]
        self.active = [False,False,False]

    def Collision_happening(self,hitbox_joueur):
        for i in range (0,3):
            a = self.pos[i]
            zone = pygame.Rect(a[0] + 1, a[1] + 1, 30, 30)
            if zone.colliderect(hitbox_joueur):
                self.active[i] = True

    def Rendu(self,surface):
        for i in range(0, 3):
            a = self.pos[i]
            if self.active[i] == False:
                surface.blit(self.skin, a)

    def action(self,joueur):
        for i in range(0, 3):
            if self.activable[i] and self.active[i]:
                t = i
        if t == 0:
            False#Happenning_list.lent(joueur)

