import pygame
from auxiliar import Auxiliar

class Platform():
    def __init__(self, x, y):
        self.lista_plataforma = []
        self.frame = 0
        self.pos_x = x
        self.pos_y = y
        self.image = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images/tile/sheet1.png",8,8)#[type]
        self.image = pygame.transform.scale(self.image[1],(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.rect_floor = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 5)

    def update(self):
        pass

    def draw(self, screen, debug):
        screen.blit(self.image, self.rect)
        if debug:
            pygame.draw.rect(screen, (20, 200, 200), self.rect)
            pygame.draw.rect(screen, (255, 20, 20), self.rect_floor)
        


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Plataforms_list():
    def __init__(self) -> None:
        self.plataforms_list = []

    def crear_lista_plataforma(self, x, y, cantidad_bloques):
        for i in range(cantidad_bloques):
            self.plataforms_list.append(Platform(x, y))
            x += 50
    
    def draw(self, screen, debug):
        for i in range(len(self.plataforms_list)):
            self.plataforms_list[i].draw(screen, debug)
        
        