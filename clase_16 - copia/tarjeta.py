import pygame
import math
import random
from constantes import *

def init(nombre_imagen, nombre_imagen_hide, x, y):
    '''
    Crea una nueva tarjeta
    Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
    Retorna la tarjeta creada
    '''
    nueva_tarjeta = {}
    nueva_tarjeta["visible"] = False
    nueva_tarjeta["descubierto"]=False
    nueva_tarjeta["path_imagen"] = PATH_RECURSOS+nombre_imagen
    nueva_tarjeta["surface"] = pygame.transform.scale(pygame.image.load(nueva_tarjeta["path_imagen"]), (ANCHO_TARJETA, ALTO_TARJETA))
    nueva_tarjeta["surface_hide"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA, ALTO_TARJETA))
    nueva_tarjeta["rect"] = nueva_tarjeta["surface"].get_rect()
    nueva_tarjeta["rect"].x = x
    nueva_tarjeta["rect"].y = y
    return nueva_tarjeta

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

#t = Tarjeta(r"00.png", r"00.png", 10, 20)
#print(t.descubierto, "hola")
#
#t2 = init(r"00.png", r"00.png", 10, 20)
#print(t2["surface"])
