from auxiliar import Auxiliar
import proyectil

class Enemy:
    def __init__(self, x, y, speed_walk, speed_run):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\OneDrive\Escritorio\PyL1\CLASE_19_inicio_juego - copia\images\inhabitants\aligator\walk.png",3,6, False, 3)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\OneDrive\Escritorio\PyL1\CLASE_19_inicio_juego - copia\images\inhabitants\aligator\walk.png",3,6,True,3)
        self.stay = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\OneDrive\Escritorio\PyL1\CLASE_19_inicio_juego - copia\images\inhabitants\aligator\idle.png",15,9)
        self.appear = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\OneDrive\Escritorio\PyL1\CLASE_19_inicio_juego - copia\images\inhabitants\aligator\appear.png", 3,9, True, 3)
        self.frame = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.movimiento = ""
        self.lista_proyectiles = []


    def movimiento(pos_x):
        pass

    def update(self, tiempo):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

        if tiempo%2 == 0:
            pass

        if self.move_x == 399:
            self.animation = self.appear
            if self.image == self.animation[-1]:
                self.move_x += 10
                
        if self.move_x > 400 and self.move_x < 410:
            self.movimiento = "adelante"
        if self.move_x > 900:
            self.movimiento = "atras"
        
        if self.movimiento == "adelante":
            self.move_x += self.speed_walk
            self.animation = self.walk_l
        elif self.movimiento == "atras":
            self.move_x -= self.speed_walk
            self.animation = self.walk_r

        self.rect.x = self.move_x
        self.rect.y = self.move_y
        

    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)