from re import X
from auxiliar import Auxiliar

class Enemy():
    def __init__(self, x, y, speed_walk):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images\inhabitants\aligator\walk.png", 3, 6, True)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images\inhabitants\aligator\walk.png", 3, 6, False)
        self.frame = 0
        self.pos_x = x
        self.pos_y = y
        self.direccion = "derecha"
        self.speed_walk = speed_walk
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.cargardor = "objeto cargador, aca se acumulan los proyectiles"

    def update(self):
        #Actualizacion de frames
        if(self.frame < len(self.animation) - 4):
            self.frame += 1 
        else: 
            self.frame = 0

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        
        if self.pos_x < 200:
            self.direccion = "right"
        elif 700 < self.pos_x:
            self.direccion = "left"
        
        if self.direccion == "right":
            self.pos_x += self.speed_walk
            self.animation = self.walk_r
        elif self.direccion == "left":
            self.pos_x -= self.speed_walk
            self.animation = self.walk_l
            self.rect.x = self.pos_x + 155

       #self.rect.x = self.pos_x
       #self.rect.y = self.pos_y
        #print(self.pos_x)

    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
