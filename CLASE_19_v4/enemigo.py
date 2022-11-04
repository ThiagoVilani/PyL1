from auxiliar import Auxiliar
import random
import pygame
from constantes import *

class Enemy():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\OneDrive\Escritorio\images\inhabitants\dust\walk_left.png", 8, 1)
        self.frame = 0
        self.speed_walk = random.randint(5, 10)
        self.animation = self.walk_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    def update(self):
        #Actualizacion de frames
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

        self.pos_x -= self.speed_walk

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y



    def draw(self, screen):
        pygame.draw.rect(screen, (200, 29, 249), self.rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        

class Horde():
    def __init__(self):
        self.enemy_list = []
    
    def update(self, player):
        for enemy in self.enemy_list:
            enemy.update()
            if enemy.pos_x < -50:
                enemy.pos_x = ANCHO_VENTANA + 50
            if  enemy.rect.colliderect(player.rect):
                return True
    
    def draw(self, screen):
        for enemy in self.enemy_list:
            enemy.draw(screen)
        