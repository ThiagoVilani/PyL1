import pygame

class Proyectil():
    def __init__(self, x, y):
        self.image = pygame.image.load(r"C:\Users\vilan\Desktop\images\red_circle.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.speed = 10
        self.trayectoria = [0, 0]

    def calcular_trayectoria(self, player_x, player_y):
        rx = (player_x - self.pos_x) / 100
        ry = (player_y - self.pos_y) / 100
        self.trayectoria = [rx, ry]
        #self.pos_x = player_x + 5
        #self.pos_y = player_y + 5
        return self
    

def update_proyectiles(lista_proyectiles, screen):
    for proyectil in lista_proyectiles:
        proyectil.pos_x += proyectil.trayectoria[0]
        proyectil.pos_y += proyectil.trayectoria[1]
        screen.blit(proyectil, (proyectil.pos_x, proyectil.pos_y))
