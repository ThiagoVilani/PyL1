import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemy, Horde
import proyectil

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
tick = pygame.USEREVENT +0
pygame.time.set_timer(tick, 2000)
tick_2 = pygame.USEREVENT +1
pygame.time.set_timer(tick_2, 90)


imagen_fondo = pygame.image.load(r"C:\Users\vilan\Desktop\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(0,0,4,8,8,16)
horde = Horde()
lista_proyectiles = []

while True:
    total_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.control("WALK_L")
            if event.key == pygame.K_RIGHT:
                player_1.control("WALK_R")
            if event.key == pygame.K_SPACE:
                player_1.control("JUMP_R")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                player_1.control("STAY")
        if event.type == tick:
            if len(horde.enemy_list) < 10:
                enemigo = Enemy(1000, 250)
                horde.enemy_list.append(enemigo)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    for i in range(len(horde.enemy_list)):
        lista_proyectiles = horde.enemy_list[i].disparar()
    player_1.update()
    player_1.draw(screen)
    #proyectil.update_proyectiles(lista_proyectiles, screen)
    
    # enemigos update

    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






