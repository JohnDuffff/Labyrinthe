import pygame
import random



def path():
#(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14)
    mur_enleve_V = []
    mur_enleve_H = []
    cle_pos = []
    happening_pos = []
    a = 1 #random.randint(1,3)
    if a ==1:
        mur_enleve_V = [(0,2),(0,10),(0,12),(1,2),(1,10),(1,12),(2,8),(2,10),(2,13),(3,8),(3,10),(3,13),(4,14),(5,14),(6,14),(7,2),(7,5),(7,12),(7,13),(8,2),(8,5),(8,11),(8,13),(9,2),(9,13),(10,2),(10,13),(11,2),(11,11),(12,2),(12,9),(13,0),(13,9),(14,0),(14,7),(14,10),(15,0),(15,4),(15,10),(16,0),(16,4),(16,10),(17,0),(17,4),(17,10),(18,0),(18,8),(19,0),(19,8),(20,0),(20,3),(20,4),(20,8),(21,0),(21,3),(21,11),(22,0),(22,3),(22,14),(22,0),(22,3),(22,14),(23,0),(23,3),(23,14)]
        mur_enleve_H = [(0,0),(0,1),(0,10),(0,11),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,12),(4,8),(4,9),(4,13),(7,2),(7,3),(7,4),(7,12),(7,13),(8,11),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(11,11),(11,12),(12,9),(12,10),(13,0),(13,1),(14,7),(14,8),(14,9),(15,4),(15,5),(15,6),(17,0),(17,1),(17,2),(17,3),(18,4),(18,5),(18,6),(18,7),(18,8),(18,9),(20,3),(21,8),(21,9),(21,10),(22,11),(22,12),(22,13),(23,14),(24,0),(24,1),(24,2),(25,14)]
        cle_pos = [16+21*48,16+4*48]
        happening_pos = [[16+3*48,16+10*48],[16+21*48,16+3*48],[16+12*48,16+2*48]]
    elif a == 2:
        mur_enleve_V = [(0,3),(1,3),(2,3),(2,11),(3,3),(3,11),(4,5),(4,9),(5,5),(5,9),(6,5),(6,9),(7,5),(7,9),(8,1),(8,9),(9,1),(9,13),(10,3),(10,13),(11,3),(11,13),(12,5),(12,13),(13,5),(13,13),(14,5),(14,13),(15,1),(15,3),(15,5),(15,8),(16,1),(16,5),(17,1),(17,5),(18,1),(18,5),(19,1),(19,4),(19,9),(19,12),(20,0),(20,4),(20,9),(20,12),(21,0),(21,4),(21,9),(21,12),(22,0),(22,2),(22,12),(23,12),(24,14)]
        mur_enleve_H = []
        cle_pos = [16+2*48,16+13*48]
    elif a == 3:
        mur_enleve_V = []
        mur_enleve_H = []
    return mur_enleve_V, mur_enleve_H, cle_pos, happening_pos


class Bordure :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [[0,0],[0,48],[1200,16],[0,720]]

    def Rendu_Bordure(self,surface):
        for i in range (0,1216,16):
            surface.blit(self.skin,(self.pos[0][0]+i, self.pos[0][1]))
            surface.blit(self.skin, (self.pos[3][0] + i, self.pos[3][1]))
        for i in range (0,666,16):
            surface.blit(self.skin, (self.pos[1][0], self.pos[1][1] + i))
            surface.blit(self.skin, (self.pos[2][0], self.pos[2][1] + i))


class Mur_Vert :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [48, 16]
        self.list_pos = []


    def yaMur(self):
        mat_Mur_v=[]
        for i in range(24):
            list = []
            for j in range(15):
                list.append(random.randint(0,9))
            mat_Mur_v.append(list)
        return mat_Mur_v


    def Rendu_Mur_vert(self,surface,path,mat_mur_v):
        path_v = path
        mat_mur_v = mat_mur_v
        for i in range(0,24,1):
            for j in range(15):
                if mat_mur_v[i][j] > 2:
                    if (i, j) not in path_v:

                        self.pos = [48 + i * 48, 16 + j * 48]
                        surface.blit(self.skin, self.pos), surface.blit(self.skin, (self.pos[0], self.pos[1] + 16))
                        self.list_pos.append(self.pos)



    def collision(self,obstacles):
        for pos in self.list_pos:
            obstacles.append(pygame.Rect(pos[0], pos[1], 16, 32))



class Mur_Hor :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [16, 48]
        self.list_pos = []


    def yaMur(self):
        mat_Mur_h=[]
        for i in range(25):
            list = []
            for j in range(14):
                list.append(random.randint(0,9))
            mat_Mur_h.append(list)

        return mat_Mur_h

    def Rendu_Mur_hor(self,surface,path,mat_mur_h):
        path_h = path
        ya_Mur = mat_mur_h
        for i in range(25):
            for j in range(14):
                if ya_Mur[i][j] > 3 :
                    if (i, j) not in path_h:
                        self.pos = [16 + i * 48, 48 + j * 48]
                        surface.blit(self.skin, self.pos),surface.blit(self.skin,(self.pos[0]+16,self.pos[1]))
                        self.list_pos.append(self.pos)

    def collision(self, obstacles):
        for pos in self.list_pos:
            obstacles.append(pygame.Rect(pos[0], pos[1], 32, 16))

class Mur :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [48,48]
        self.list_pos = []

    def Rendu_Mur(self,surface):
        for i in range(24):
            for j in range(14):
                self.pos = [48 + i * 48, 48 + j * 48]
                surface.blit(self.skin, self.pos)
                self.list_pos.append(self.pos)

    def collision(self, obstacles):
        for pos in self.list_pos:
            obstacles.append(pygame.Rect(pos[0], pos[1], 16, 16))

