import random
import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemy, Horde
from platforms import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()


imagen_fondo = pygame.image.load(r"C:\Users\vilan\Desktop\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

#Bases Temporales
tick = pygame.USEREVENT
pygame.time.set_timer(tick, 90)
tick_2 = pygame.USEREVENT +1
pygame.time.set_timer(tick_2, 2000)
tick_3 = pygame.USEREVENT +2
pygame.time.set_timer(tick_3, 40)

#Creacion de Objetos y Variables
player_1 = Player(x=0,y=400,speed_walk=4,speed_run=8,gravity=8,jump_power=25,frame_rate_ms=80,move_rate_ms=40,jump_height=150)
horde = Horde()
lista_plataforma = Plataforms_list()
lista_plataforma.crear_lista_plataforma(200, 400, 5)
game_over = False
debug = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game_over:
            pygame.quit()
            sys.exit()
        if event.type == tick:
            game_over = horde.update(player_1)     
        if event.type == tick_2 and len(horde.enemy_list) < 2:
            enemy = Enemy((ANCHO_VENTANA + 50), random.randint(600, 700))
            horde.enemy_list.append(enemy)

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    horde.draw(screen, debug)
    lista_plataforma.draw(screen, debug)
    player_1.events(delta_ms,keys)
    player_1.update(delta_ms, lista_plataforma.plataforms_list)
    player_1.draw(screen, debug)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






