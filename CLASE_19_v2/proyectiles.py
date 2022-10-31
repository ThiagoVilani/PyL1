import pygame

class Proyectil():
    def __init__(self, x, y):
        self.image = pygame.image.load(r"C:\Users\vilan\Desktop\images\black_circle.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
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
        
    
class Cargador():
    def __init__(self):
        self.lista_proyectiles = []
    
    def crear_lista_proyectiles(self, player_x, player_y):
        lista_proyectiles = []
        for i in range(10):
            proyectil = Proyectil(player_x, player_y)
            lista_proyectiles.append(proyectil)
        return lista_proyectiles

    def update(self, screen):
        for proyectil in self.lista_proyectiles:
            proyectil.pos_x = proyectil.pos_x + proyectil.trayectoria[0]
            proyectil.pos_y = proyectil.pos_y + proyectil.trayectoria[1]
            #proyectil.pos_x = proyectil.pos_x + (proyectil.trayectoria[0] * 3)
            #proyectil.pos_y = proyectil.pos_y + (proyectil.trayectoria[1] * 3)
            screen.blit(proyectil.image, (proyectil.pos_x, proyectil.pos_y))
            
            pygame.draw.rect(screen, (255, 90, 34), (proyectil.pos_x, proyectil.pos_y, 50,50))
            # print(proyectil.rect.x, proyectil.rect.y)
            #print(proyectil.pos_x, proyectil.pos_y)
    
