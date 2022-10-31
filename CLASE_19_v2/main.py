#from curses import KEY_DOWN
import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from proyectiles import Proyectil, Cargador

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(r"C:\Users\vilan\Desktop\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(0,0,4,8,8,16)
enemy = Enemy(199, 230, 5)
cargador = Cargador()
#cargador.crear_lista_proyectiles(player_1.move_x, player_1.move_y)
tick = pygame.USEREVENT
pygame.time.set_timer(tick, 30)
tick_2 = pygame.USEREVENT + 1
pygame.time.set_timer(tick_2, 2000)

while True:
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
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
            enemy.update()
        if event.type == tick:
            if len(cargador.lista_proyectiles) < 10:
                proyectil = Proyectil(enemy.pos_x, enemy.pos_y)
                cargador.lista_proyectiles.append(proyectil.calcular_trayectoria(player_1.move_x, player_1.move_y))
        if event.type == tick_2:
             #cargador.update(screen)
             print("paso un segundo")

#    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    
    #enemy.update()
    
    if 0 < len(cargador.lista_proyectiles):
        cargador.update(screen)
    player_1.update()
    player_1.draw(screen)
    enemy.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    






