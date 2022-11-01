from auxiliar import Auxiliar
from proyectil import Proyectil
import random
import pygame

class Enemy:
    def __init__(self, x, y):
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images\inhabitants\aligator\walk.png", 3, 6)
        self.frame = 0
        self.pos_x = x
        self.pos_y = y
        self.speed_walk = random.randint(5, 10)
        self.animation = self.walk_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.creation_time = 0
        
        
    def update(self):
        self.creation_time += 1
        #Actualizacion de frames
        if(self.frame < len(self.animation) - 4):
            self.frame += 1 
        else: 
            self.frame = 0

        self.pos_x -= self.speed_walk
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
        #if self.creation_time == 20:
        #    self.disparar()
        #print(self.creation_time, "creacion")
        
    
    def draw(self, screen):
        self.image = self.animation[self.frame]
        print(self.rect.x)
        screen.blit(self.image,self.rect)


    def disparar(self):
        proyectil = Proyectil(self.pos_x, self.pos_y)
        return proyectil

        

class Horde:
    def __init__(self):
        self.enemy_list = []


    def crear_horda(self, cantidad):
        for i in range(cantidad):
            enemigo = Enemy(random.randint(1080, 1200), 250)
            self.enemy_list.append(enemigo)


    def update(self, screen):
        for enemy in self.enemy_list:
            print(enemy.pos_x, "posicion x")
            enemy.update()
            #enemy.pos_x -= enemy.speed_walk
            enemy.draw(screen)
        return 