import pygame
import player

class Proyectil:
    def __init__(self):
        self.imagen_bala = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\PyL1\Juego\circulo_negro.png")
        self.imagen_bala = pygame.transform.scale(self.imagen_bala,(10,10))
        self.rect_bala = self.imagen_bala.get_rect()
        self.surface = self.imagen_bala
        self.rect = self.rect_bala
        self.speed = 10
        self.trayectoria = [0, 0]


    def crear_lista_proyectiles(self, cantidad):
        lista_proyectiles = []
        for i in range(cantidad):
            proyectil = Proyectil()
            lista_proyectiles.append(proyectil)
        return lista_proyectiles


    def calcular_trayectoria(self, player):
        rx = (player.rect[0] - self.rect[0]) / 100
        ry = (player.rect[1] - self.rect[1]) / 100
        self.trayectoria = [rx, ry]
        self.rect[0] = player.rect[0] + 50
        self.rect[1] = player.rect[1] + 50
        return self

    def update(self, lista_proyectiles, ventana_principal):
        for proyectil in lista_proyectiles:
            proyectil.rect[0] = proyectil.rect[0] + proyectil.trayectoria[0]
            proyectil.rect[1] = proyectil.rect[1] + proyectil.trayectoria[1]
            proyectil.rect[0] = proyectil.rect[0] + (proyectil.trayectoria[0] * 3)
            proyectil.rect[1] = proyectil.rect[1] + (proyectil.trayectoria[1] * 3)
            ventana_principal.blit(proyectil.surface, (proyectil.rect[0], proyectil.rect[1]))