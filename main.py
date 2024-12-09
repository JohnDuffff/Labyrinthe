import sys
import pygame
import time
import random

from scripts.entite import Joueur, Cle, Ennemi
from scripts.mur import Mur_Vert, Mur_Hor, Mur, Bordure, path
from scripts.happening import Happenning

class Jeu:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Labyrinthe')

        #   self.screen = pygame.display.set_mode((1216, 772))  # (32+25*32+24*16,32+36+15*32+14*16)

        # Configuration de la fenêtre
        info_ecran = pygame.display.Info()
        self.window_width = info_ecran.current_w
        self.window_height = info_ecran.current_h - 30  # Réserve de l'espace pour la barre de titre
        pygame.display.set_caption("maze")
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        
        # Couleurs
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.grey = (50, 50, 50)
        
        # infos fenetre
        info_ecran = pygame.display.Info()
        self.window_width = info_ecran.current_w
        self.window_height = info_ecran.current_h

        # creation clocks
        self.clock = pygame.time.Clock()
        self.speed = 200  # speed du joueur en pixels par seconde
        self.time_initial = 150  # time initial en secondes
        self.time = self.time_initial

        # Police d'affichage pour le chronomètre
        self.font = pygame.font.Font(None, 36)  # Police par défaut

        # creation chemin
        self.chemin = path()

        self.cle = Cle(self)
        self.cle.pos = self.chemin[2]

        self.happening = Happenning(self)
        self.happening.pos = self.chemin[3]

        self.movement = [False, False, False, False]
        self.joueur = Joueur(self, 'sorciere')

        self.ennemi = Ennemi(self)

        self.skin = pygame.image.load('img/mur.png').convert()

        # creation matrice mur verticaux
        self.mur_vert = Mur_Vert(self, self.skin)
        self.list_murV = self.mur_vert.yaMur()

        # creation matrice mur horizontaux
        self.mur_hor = Mur_Hor(self, self.skin)
        self.list_murH = self.mur_hor.yaMur()

        self.mur = Mur(self, self.skin)
        self.bordure = Bordure(self,self.skin)

        # initialisation liste coordonnées des murs/colisions
        self.obstacles = []

    def run(self):
        pygame.mixer.music.load('sound/OIIAOIIA-CAT.wav')
        pygame.mixer.music.set_volume(0.5)

        # positionement murs
        self.mur.Rendu_Mur(self.screen)
        self.mur_vert.Rendu_Mur_vert(self.screen, self.chemin[0], self.list_murV)
        self.mur_hor.Rendu_Mur_hor(self.screen, self.chemin[1], self.list_murH)

        # remplissage liste coordonnées murs
        self.mur.collision(self.obstacles)
        self.mur_hor.collision(self.obstacles)
        self.mur_vert.collision(self.obstacles)

        while True:
            # fond d'écran
            self.screen.fill((55, 50, 123))

            delta_time = self.clock.tick(60) / 1000  # time écoulé en secondes
            
            # Met à jour le time restant
            self.time = self.time_initial - (pygame.time.get_ticks() // 1000)
            
            #calcul déplacements

            self.hitbox = self.joueur.Collision_joueur()

            self.joueur.mouv([self.movement[3] - self.movement[2], self.movement[1] - self.movement[0]],self.hitbox,self.obstacles)

            self.cle.Collision_cle(self.hitbox)

            self.happening.Collision_happening(self.hitbox)

            self.hitbox_ennemi = self.ennemi.Collision_ennemi()
            a = random.randint(0, 1)
            b = random.randint(0, 1)
            for i in range(6):
                self.ennemi.Mouvement(self.hitbox_ennemi,self.obstacles,[a,b])
            if self.ennemi.Degat(self.hitbox,self.hitbox_ennemi):
                self.joueur.Nb_vie()

            #actualisation visuelle position joueur
            self.joueur.Rendu(self.screen)
            self.cle.Rendu(self.screen)
            self.ennemi.Rendu_Ennemi(self.screen)
            self.happening.Rendu(self.screen)

            # actualisation visuelle murs
            self.bordure.Rendu_Bordure(self.screen)
            self.mur.Rendu_Mur(self.screen)
            self.mur_vert.Rendu_Mur_vert(self.screen, self.chemin[0],self.list_murV)
            self.mur_hor.Rendu_Mur_hor(self.screen, self.chemin[1], self.list_murH)


            if self.joueur.vie_restante <= 0:
                print('Perdu, la HOOOOONTE')
                pygame.quit()
                sys.exit()

            if self.joueur.pos == [1172,688] and self.cle.obtenue :
                print('gagné ... bref ...')
                pygame.mixer.music.play(-1)
                time.sleep(4)
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        self.movement[2] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        self.movement[2] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[3] = False
            
            """Affiche le chronomètre sur l'écran."""
            chronometer_surface = pygame.Surface((190, 50))  # Dimensions de la mini-fenêtre
            chronometer_surface.fill(self.black)  # Fond black pour la sous-surface

            # Rendre le texte du chronomètre en blanc
            texte_chrono = self.font.render(f"time : {self.time} s", True, self.white)
            chronometer_surface.blit(texte_chrono, (10, 10))

            # Afficher la mini-fenêtre dans le coin supérieur droit de la fenêtre principale
            self.screen.blit(chronometer_surface, (self.window_width - 150, 736))

            pygame.display.update()
            self.clock.tick(60)

Jeu().run()