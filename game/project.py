#Libraries

import pygame
import sys
import random
import pygame.time as taim
import pygame.locals as gg
import pygame.event as ev

pygame.init()

#refresh
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255,40,0)


title_image = pygame.image.load("titulo.jpg")
game_over_image = pygame.image.load("Fin_juego.jpg")

#fondo = pygame.image.load("cielo.jpg")
playy = pygame.image.load("player.png")


#pantalla

tamano_ancho = 500
tamano_largo = 500


surface = pygame.display.set_mode((tamano_ancho,tamano_largo))
pygame.display.set_caption('proyecto final')  #  nombre



#  statements
izquierdista = False
derechista = False

game_init = False
game_end = False

game_plataform = []
game_plataform_speed = 5
game_plataform_delay = 6000
game_plataform_last = 0
game_plataform_droop = -9
game_droop = False
game_start = 0
game_timer = 0


# Ready player one
jugador = {"x": tamano_ancho / 2, "y": 0,"largo": 20,"ancho": 20,"vy": 5}

#===========================================================================================================

def jugador_draw():
    #pygame.image.load("player.png").convert_alpha() , (jugador["x"],jugador["y"],jugador["ancho"],jugador["largo"])
    pygame.draw.rect(surface,(RED), (jugador["x"],jugador["y"],jugador["ancho"],jugador["largo"]))


def movimiento():
    global game_plataform_droop, game_droop

    left_plataform = True
    right_plataform = True


    if surface.get_at((int(jugador["x"]), int(jugador["y"] + jugador["largo"]))) == (0,0,0, 255):
         left_plataform = False #0, 0, 0, 255

    if surface.get_at((int(jugador["x"] + jugador["ancho"]), int(jugador["y"] + jugador["largo"]))) == (0, 0, 0, 255):
        right_plataform = False

    if left_plataform is False and right_plataform is False and (jugador["y"] + jugador["largo"]) + \
            jugador["vy"] < tamano_largo:
        jugador["y"] += jugador["vy"]

    if game_droop is False:
        game_droop = True
        game_plataform_droop += 1

    else:

        plataform_n = False
        player_off = 0
        game_droop = False

        while plataform_n is False:

            if surface.get_at((int(jugador["x"]), int((jugador["y"]) + int(jugador["largo"])) - player_off)) == (
                    0, 0, 0, 255):
                jugador ["y"] -= player_off
                plataform_n = True


            elif (jugador["y"] + jugador["largo"]) - player_off > 0:
             player_off += 1

            else:

             game_over_F()
             break
#
    if derechista is True:
        if jugador["x"] > 0 and jugador["x"] - 5 > 0:
            jugador["x"] -= 5
        elif jugador["x"] > 0 and jugador["x"] - 5 < 0:
            jugador["x"] = 0
#izquierdista
    if izquierdista is True:
        if jugador["x"] + jugador["ancho"] < tamano_ancho and (jugador["x"] + jugador["ancho"]) + 5 < tamano_ancho:
            jugador["x"] += 5

        elif jugador["x"] + jugador["ancho"] < tamano_ancho and (jugador["x"] + jugador["ancho"]) + 5 > tamano_ancho:
            jugador["x"] = tamano_ancho - jugador["ancho"]

def plataform_spaw():
    global game_plataform_last, game_plataform_delay

    plataform_y = tamano_largo
    gapPosition = random.randint(0,tamano_ancho - 80) #pos

    game_plataform.append({"pos": [0, plataform_y], "gap": gapPosition})
    game_plataform_last = taim.get_ticks()

    if game_plataform_delay > 800:
        game_plataform_delay -= 200

def plataform_mov():
    for idx, plataform in enumerate(game_plataform):

        plataform["pos"][1] -= game_plataform_speed

        if plataform["pos"][1] < -10:
            game_plataform.pop(idx)


def plataform_shape():

    for plataform in game_plataform:
        pygame.draw.rect(surface, (GREEN), (plataform["pos"][0], plataform["pos"][1], tamano_ancho, 20))
        pygame.draw.rect(surface, (0, 0, 0), (plataform["gap"], plataform["pos"][1], 40, 20))

def game_over_F():
    global game_init,game_end

    game_plataform_speed = 0
    game_init = False
    game_end = True

def restart():
    global game_plataform, jugador, game_start, game_plataform_droop, game_plataform_delay

    game_plataform =[]
    jugador["x"] = tamano_ancho / 2
    jugador["y"] = 0
    game_start = taim.get_ticks()
    game_plataform_droop = -1
    game_plataform_delay = 2000

def quit():
    pygame.quit()
    sys.exit()

#==================================================================================================================


while True:

    surface.fill((0, 0, 0))
    # surface.blit(fondo, (0, 10))
    for event in ev.get():
        print(event) #print de los eventos

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                izquierdista = True
            if event.key == pygame.K_RIGHT:
                derechista = True
            if event.key == pygame.K_ESCAPE:
                quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                    izquierdista = False
            if event.key == pygame.K_RIGHT:
                    derechista = False

            if event.key == pygame.K_SPACE:
                   if game_init == False:
                     restart()
                     game_init = True

        if event.type == gg.QUIT:
            quit()

    if game_init is True: #juego exe


       # surface.blit(fondo, (0,10))

        game_timer = taim.get_ticks() - game_start
        #jugador_draw()
        plataform_mov()
        plataform_shape()
        movimiento()
        jugador_draw()

    elif game_end is True:  # el juego termina

        surface.blit(game_over_image, (0, 180))

    else:
        # Welcome Screen
        surface.blit(title_image, (0, 130))


    if taim.get_ticks() - game_plataform_last > game_plataform_delay:
            plataform_spaw()


    clock.tick(60) #60 fps
    pygame.display.update()