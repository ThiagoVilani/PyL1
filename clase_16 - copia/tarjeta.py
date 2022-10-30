import pygame
import math
import random
from constantes import *

class Tarjeta:
    def __init__(self, nombre_imagen, nombre_imagen_hide, x, y):
        self.visible = False
        self.descubierto = False
        self.path_imagen = PATH_RECURSOS+nombre_imagen
        self.surface = pygame.transform.scale(pygame.image.load(self.path_imagen), (ANCHO_TARJETA, ALTO_TARJETA))
        self.surface_hide = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA, ALTO_TARJETA))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

