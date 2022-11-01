import random
import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemy, Horde

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()


imagen_fondo = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
tick = pygame.USEREVENT
pygame.time.set_timer(tick, 90)
tick_2 = pygame.USEREVENT +1
pygame.time.set_timer(tick_2, 2000)
tick_3 = pygame.USEREVENT +2
pygame.time.set_timer(tick_3, 40)
player_1 = Player(0,0,4,8,8,16)
horde = Horde()
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or game_over:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.control("WALK_L")
            if event.key == pygame.K_RIGHT:
                player_1.control("WALK_R")
            if event.key == pygame.K_DOWN:
                player_1.control("DOWN")
            if event.key == pygame.K_UP:
                player_1.control("UP")            
            if event.key == pygame.K_SPACE:
                player_1.control("JUMP_R")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_1.control("STAY")
        if event.type == tick:
            game_over = horde.update(player_1)
        if event.type == tick_3:
            player_1.update()       
        if event.type == tick_2 and len(horde.enemy_list) < 2:
            enemy = Enemy((ANCHO_VENTANA + 50), random.randint(330, 430))
            horde.enemy_list.append(enemy)

    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    horde.draw(screen)
    
    player_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






