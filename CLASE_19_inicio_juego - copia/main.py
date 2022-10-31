#from curses import KEY_DOWN
import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from proyectil import Proyectil

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(r"C:\Users\vilan\Desktop\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(0,0,4,8,8,16)
enemy_1 = Enemy(399, 250, 10, 20)
tick = pygame.USEREVENT
pygame.time.set_timer(tick, 90)
contador_tiempo = 0

while True:
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
            contador_tiempo += 1
            enemy_1.update(contador_tiempo)
            

    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    #enemy_1.update()
    print(enemy_1.rect)
    print(enemy_1.move_x, enemy_1.move_y)
    #proyectil.update(player_1.lista_proyectiles, screen)
    player_1.update()
    player_1.draw(screen)
    enemy_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(25)



    






