import pygame
from constantes import *
import tablero

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA+100))
pygame.display.set_caption('The Simpsons Memotest')

running = True
tick = pygame.USEREVENT
pygame.time.set_timer(tick,1000)
clock_fps = pygame.time.Clock()
tablero_juego = tablero.Tablero()
pos_mouse = None
lista_tarjetas_visibles = []
indices_tarjetas_visibles = []

while running:
    tiempo_origen = pygame.time.get_ticks()
    clock_fps.tick(60)
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos_mouse = event.pos
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                print("Ya paso un segundo") 
    pos_mouse, lista_tarjetas_visibles, indices_tarjetas_visibles = tablero_juego.update(pos_mouse, tiempo_origen, lista_tarjetas_visibles, indices_tarjetas_visibles)
    pantalla_juego.fill((255, 255, 255))
    tablero_juego.render(pantalla_juego)
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()
