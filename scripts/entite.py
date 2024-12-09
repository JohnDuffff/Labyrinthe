

import pygame

class Joueur:
    def __init__(self,jeu,e_type):
        self.jeu = jeu
        self.type = e_type
        self.skin = pygame.image.load('./img/joueur.png').convert()
        self.skin_vie = pygame.image.load('./img/vie.png')
        self.skin.set_colorkey((237, 28, 36)) #couleur fond image
        self.skin_vie.set_colorkey((237, 28, 36))
        self.vie_restante = 3
        self.pos = [16, 16]
        self.vit = 4

    def mouv(self, mouvement,hitbox,obstacles):

        #collision bordures exterieurs
        if self.pos[0]<= 16:
            self.pos[0] = 16
        elif self.pos[0] >= 1168:
            self.pos[0] = 1168
        elif self.pos[1]<= 16:
            self.pos[1] = 16
        elif self.pos[1] >= 688:
            self.pos[1] = 688
        #collision murs interieurs
        hit_box = hitbox

        for obstacle in obstacles:
            if hit_box.colliderect(obstacle):
                self.vit = 0.5
                if self.pos[1] < obstacle[1]:
                    self.pos[1] = obstacle[1]-32
                elif self.pos[1] > obstacle[1]:
                    self.pos[1] = obstacle[1]+16
                elif self.pos[0] < obstacle[0]:
                    self.pos[0] = obstacle[0]-32
                elif self.pos[0] > obstacle[0]:
                    self.pos[0] = obstacle[0]+16
            else :
                self.vit = 4

        #deplacement
        self.pos[0] += mouvement[0] * self.vit
        self.pos[1] += mouvement[1] * self.vit


        #aligner le joueur avec la grille
        if mouvement[0] == 0:
            self.pos[0] = self.pos[0]//16 * 16
        if mouvement[1] == 0:
            self.pos[1] = self.pos[1]//16 * 16


    def Collision_joueur(self):
        # defini la zone de colision du joueur
        return pygame.Rect(self.pos[0]+1, self.pos[1]+1, 30, 30)

    def Nb_vie(self):
        self.vie_restante -=1

    def Rendu(self,surface):
        #affiche le joueur
        surface.blit(self.skin, self.pos)
        surface.blit(self.skin, (16, 738))
        for i in range (self.vie_restante):
            surface.blit(self.skin_vie, (64 + 40*i , 738))


class Cle:
    def __init__(self, jeu):
        self.jeu = jeu
        self.skin = pygame.image.load('img/cle.png').convert()
        self.skin.set_colorkey((237,28,36))
        self.pos = []
        self.obtenue = False

    def Collision_cle(self,hitbox_joueur):
        range = pygame.Rect(self.pos[0] + 1, self.pos[1] + 1, 30, 30)
        if range.colliderect(hitbox_joueur):
            self.obtenue = True

    def Rendu(self,surface):
        if self.obtenue:
            surface.blit(self.skin, (192,738))
        else:
            surface.blit(self.skin, self.pos)

class Ennemi :
    def __init__(self,jeu):
        self.jeu = jeu
        self.skin = pygame.image.load('img/ennemi.png')
        self.skin.set_colorkey((237,28,36))
        self.pos = [160,160] #[16,688]
        self.mouv = 50
        self.invincibilite = 0

    def Mouvement(self,hitbox,obstacles,mouv):
        hit_box = hitbox
        for obstacle in obstacles:
            if hit_box.colliderect(obstacle):
                if self.pos[1] < obstacle[1]:
                    self.pos[1] = obstacle[1]-32
                elif self.pos[1] > obstacle[1]:
                    self.pos[1] = obstacle[1]+16
                elif self.pos[0] < obstacle[0]:
                    self.pos[0] = obstacle[0]-32
                elif self.pos[0] > obstacle[0]:
                    self.pos[0] = obstacle[0]+16

        if self.mouv == 0:
            self.mouv = 50
            if mouv[1]:
                self.pos[mouv[0]] += 8
            else:
                self.pos[mouv[0]] -= 8
        else:
            self.mouv -= 1



    def Collision_ennemi(self):
        return pygame.Rect(self.pos[0]+1, self.pos[1]+1, 30, 30)

    def Degat(self, hitbox_joueur, hitbox_ennemi):
        if hitbox_ennemi.colliderect(hitbox_joueur) :
            if self.invincibilite == 0:
                self.invincibilite = 50
                return 1
            else:
                self.invincibilite -= 1

        else:
            self.invincibilite = 0
            return 0

    def Rendu_Ennemi(self,surface):
        surface.blit(self.skin,self.pos)
