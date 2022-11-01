from auxiliar import Auxiliar
import random

class Enemy():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images\inhabitants\aligator\walk.png", 3, 6, True)
        self.frame = 0
        self.speed_walk = random.randint(5, 10)
        self.animation = self.walk_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()


    def update(self):
        #Actualizacion de frames
        if(self.frame < len(self.animation) - 4):
            self.frame += 1 
        else: 
            self.frame = 0

        self.pos_x += self.speed_walk

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)