import pygame
import math
import random
from constantes import *
import tarjeta
import pygame


'''
ANCHO_PANTALLA = 500
ALTO_PANTALLA = 550
ALTO_TEXTO = 50
CANTIDAD_TARJETAS_H = 2
CANTIDAD_TARJETAS_V = 2
'''
def init():
    '''
    Crea una lista de tarjetas
    Recibe como parametro la cantidad de tarjetas
    Retorna un dict tablero
    '''
    dic_tablero = {}
    lista_tarjetas = []
    i = 1
    for x in range(0,CANTIDAD_TARJETAS_H * ANCHO_TARJETA, ANCHO_TARJETA):
        for y in range(0,CANTIDAD_TARJETAS_V * ALTO_TARJETA,ALTO_TARJETA):
            if(i > CANTIDAD_TARJETAS_UNICAS):
                tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
            else:
                tarjeta_test = tarjeta.init("0{0}.png".format(i),r"00.png",x,y)
            lista_tarjetas.append(tarjeta_test)
            i = i + 1
    dic_tablero["lista_tarjetas"] = lista_tarjetas
    dic_tablero["tiempo_click"] = 0
    return dic_tablero

def mezclar(dic_tablero):
    lista_tarjetas = dic_tablero["lista_tarjetas"]
    lista_posiciones = []
    for tarjeta in lista_tarjetas:
        lista_posiciones.append(tarjeta["rect"])
    random.shuffle(lista_posiciones)
    for tarjeta, posicion in zip(lista_tarjetas, lista_posiciones):
        tarjeta["rect"] = posicion
    
def colicion(dic_tablero, pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    indice_tarjeta = None
    if pos_xy != None:
        print("colision en colision")
        for i in range(len(dic_tablero["lista_tarjetas"])):
            if dic_tablero["lista_tarjetas"][i]["rect"].collidepoint(pos_xy):
                indice_tarjeta = i
                dic_tablero["tiempo_click"] = pygame.time.get_ticks()
    return indice_tarjeta    

def update(dic_tablero, pos_mouse, tiempo_origen, lista_tarjetas_visibles, indices_tarjetas_visibles):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, 
    en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''    
    
    
    tarjeta_a_descubrir = colicion(dic_tablero, pos_mouse)
    if tarjeta_a_descubrir != None:
        dic_tablero["lista_tarjetas"][tarjeta_a_descubrir]["visible"] = True
        pos_mouse = None
        lista_tarjetas_visibles.append(dic_tablero["lista_tarjetas"][tarjeta_a_descubrir])
        indices_tarjetas_visibles.append(tarjeta_a_descubrir)
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    if len(lista_tarjetas_visibles) > 1:
        if (lista_tarjetas_visibles[0]["path_imagen"] == lista_tarjetas_visibles[1]["path_imagen"]):
            print("las imagenes coinciden")
            dic_tablero["lista_tarjetas"][indices_tarjetas_visibles[0]]["descubierto"] = True
            dic_tablero["lista_tarjetas"][indices_tarjetas_visibles[1]]["descubierto"] = True
            lista_tarjetas_visibles = []
            indices_tarjetas_visibles = []
            dic_tablero["tiempo_click"] = 0
        else:
            if 0 < dic_tablero["tiempo_click"]:
                tiempito = tiempo_origen - dic_tablero["tiempo_click"] 
                if tiempito > 3000:
                    print("ahora deberian cambiarse a hide")
                    dic_tablero["tiempo_click"] = 0
                    for tarjeta in dic_tablero["lista_tarjetas"]:
                        tarjeta["visible"] = False
                    lista_tarjetas_visibles = []
                    indices_tarjetas_visibles = []        
    win(dic_tablero)        
    return pos_mouse, lista_tarjetas_visibles, indices_tarjetas_visibles
    
        
        

def render(d_tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = d_tablero["lista_tarjetas"]
    for tarjeta in lista_tarjetas:
        if (tarjeta["descubierto"] == True) or (tarjeta["visible"] == True):
            pantalla_juego.blit(tarjeta["surface"],tarjeta["rect"])
        else:
            if (tarjeta["descubierto"] == False) and (tarjeta["visible"] == False):
                pantalla_juego.blit(tarjeta["surface_hide"], tarjeta["rect"])

        

def coincidencia(lista_tarjetas):
    tarjetas_visibles = []
    indices_coincidentes = []
    for i in range(len(lista_tarjetas)):
        if lista_tarjetas[i]["visible"] == True:
            indices_coincidentes.append(i)
            tarjetas_visibles.append(lista_tarjetas[i])
    if tarjetas_visibles[0]["path_imagen"] == tarjetas_visibles[1]["path_imagen"]:
        return indices_coincidentes

def win(dic_tablero):
    contador_descubiertas = 0
    lista_tarjetas = dic_tablero["lista_tarjetas"]
    for tarjeta in lista_tarjetas:
        if tarjeta["descubierto"] == True:
            contador_descubiertas += 1
    if contador_descubiertas == len(lista_tarjetas):
        print("Ganaste")