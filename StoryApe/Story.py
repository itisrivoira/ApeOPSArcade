from typing import Any

import pygame, sys, os

import time, random, json

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init() #inizializzo pygame
pygame.display.set_caption('Ape Ops Arcade')

#FIST CAP
WINDOW_SIZE1 = (1080,900)

screen = pygame.display.set_mode(WINDOW_SIZE1,0,32) #finestra di gioco
player_image = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
player_image=pygame.transform.scale(player_image,(65, 85)) #ridimensiono l'omino
bg_image = pygame.image.load(os.path.join("Immagini", "labbg.jpg")) #background

text1 = pygame.image.load(os.path.join("Immagini", "Begin.png"))
text1 = pygame.transform.scale(text1,(700, 150)) #ridimensionamento

text2 = pygame.image.load(os.path.join("Immagini", "Corrente.png"))
text2 = pygame.transform.scale(text2,(700, 150)) #ridimensionamento

text3 = pygame.image.load(os.path.join("Immagini", "Urla.png"))
text3 = pygame.transform.scale(text3,(700, 150)) #ridimensionamento

text4 = pygame.image.load(os.path.join("Immagini", "Occhiata.png"))
text4 = pygame.transform.scale(text4,(500, 150)) #ridimensionamento

#money_image = pygame.image.load(os.path.join("Immagini", "Money.gif"))
#money_image = pygame.transform.scale(money_image,(50,50))

#global variables
moving_right = False
moving_left = False
moving_up = False
moving_down = False
n_livello = 1   #numero livello

#font
font = pygame.font.SysFont("Comic Sans MS", 45)
font_icon = pygame.font.SysFont("Comic Sans MS", 20)

#color font
yellow_font = (255, 255, 0)
black_font = (0,0,0)

#numero Step
nStep = 0

#position
player_location=[120,350]
player_location2 = [490, 550]

#check player location
player_locx = 0
player_locy = 0

#obiettivo
n_obiettivo = 0
obiettivo_check = False

#sound track
# first
pygame.mixer.pre_init()
pygame.mixer.music.load(os.path.join("Audio", "FirstTrack.ogg"))  # Get the first track from the playlist
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song


#PS4 Controller Json
#Inizializzo il controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open(os.path.join("Json", "ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
#controllo analogico
analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }

def message_to_screen(msg, color, font):
    if nStep == 4:
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text, [350, 450])
    else:
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text, [200, 450])

def fade(width, height, nStep):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        if nStep == 1:
            message_to_screen("Click Mouse Button to continue...", yellow_font, font)
        elif nStep == 4:
            message_to_screen("Secondo Capitolo", yellow_font, font)

        pygame.time.delay(5)

def fade_obiettivo(width, height, n):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()

        if n <= 3:
            message_to_screen("Obiettivo: perlustra il laboratorio", yellow_font, font)

        if n == 4:
            message_to_screen("Obiettivo: esci dal laboratorio", yellow_font, font)

        pygame.time.delay(5)

def show_obiettivo(n):
    if n == 4:
        n_obiettivo = 4
        fade_obiettivo(1080,900, n_obiettivo)
    elif n <= 3:
        n_obiettivo = 3
        fade_obiettivo(1080,900, n_obiettivo)

n_image = 0 #salto livello (scena)

while True:
    if n_livello > 0:
        if n_image == 0:
            screen.blit(bg_image, (0, 0))
            screen.blit(player_image, player_location)
            screen.blit(text1, (250, 750))

        elif n_image == 1:
            screen.blit(bg_image, (0, 0))
            screen.blit(player_image, player_location)
            # corto circuito sounds
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "CortoCircuito.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song
            nStep = 1
            fade(1080, 900, nStep)

        elif n_image == 2:
            screen.blit(bg_image, (0, 0))
            screen.blit(player_image, player_location)
            screen.blit(text2, (250, 750))
            # scream sounds
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "Scream.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song
            # pygame.mixer.unpause()

        elif n_image == 3:
            screen.blit(bg_image, (0, 0))
            screen.blit(player_image, player_location)
            screen.blit(text3, (250, 750))

        elif n_image == 4:
            screen.blit(bg_image, (0, 0))
            screen.blit(player_image, player_location)
            n_obiettivo = 4
            if (player_location[0] > 900 and player_location[1] > 330) or (player_location[0] > 900 and player_location[1] <362):
                print("open door")
                pygame.mixer.fadeout(1)
                pygame.mixer.pause()
                pygame.mixer.music.load(os.path.join("Audio", "DoorOpening.ogg"))  # Get the first track from the playlist
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song
                nStep = 4
                fade(1080, 900, nStep)
                n_livello = 2

        elif n_image == 5:
            n_livello = 2
            # Cap 2
            WINDOW_SIZE2 = (688, 904)
            screen2 = pygame.display.set_mode(WINDOW_SIZE2, 0, 32)
            player_image2 = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
            player_image2 = pygame.transform.scale(player_image2, (25, 45))  # ridimensiono l'omino
            bg_image2 = pygame.image.load(os.path.join("Immagini", "BgLevel2.png"))
            #money_image = pygame.image.load(os.path.join("Immagini", "Money.gif"))
            #money_image = pygame.transform.scale(money_image, (50, 50))
            salvini_image = pygame.image.load(os.path.join("Immagini", "hornySalvini.png"))
            salvini_image = pygame.transform.scale(salvini_image, (25, 45))  # ridimensiono salvini
            draga_image = pygame.image.load(os.path.join("Immagini", "draga.png"))
            draga_image = pygame.transform.scale(draga_image, (75, 55))
            salvini_image = pygame.transform.scale(salvini_image, (25, 45))
            #text salvini
            dialog_enemy_1 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy1.png"))
            dialog_enemy_1 = pygame.transform.scale(dialog_enemy_1, (500, 150))  # ridimensionamento
            dialog_enemy_2 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy2.png"))
            dialog_enemy_2 = pygame.transform.scale(dialog_enemy_2, (500, 150))  # ridimensionamento
            dialog_enemy_3 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy3.png"))
            dialog_enemy_3 = pygame.transform.scale(dialog_enemy_3, (500, 150))  # ridimensionamento
            dialog_enemy_4 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy4.png"))
            dialog_enemy_4 = pygame.transform.scale(dialog_enemy_4, (500, 150))  # ridimensionamento
            dialog_enemy_5 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy5.png"))
            dialog_enemy_5 = pygame.transform.scale(dialog_enemy_5, (500, 150))  # ridimensionamento
            dialog_enemy_6 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy6.png"))
            dialog_enemy_6 = pygame.transform.scale(dialog_enemy_6, (500, 150))  # ridimensionamento
            dialog_enemy_7 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy7.png"))
            dialog_enemy_7 = pygame.transform.scale(dialog_enemy_7, (500, 150))  # ridimensionamento
            #---
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(text4, (90, 750))
            screen2.blit(draga_image, [340,80])
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "ThemeSound.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song

        elif n_image == 6:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(draga_image, [340, 80])
            screen2.blit(salvini_image, [370, 150])

        elif n_image == 7:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_1, (90, 750))

        elif n_image == 8:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_2, (90, 750))

        elif n_image == 9:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_3, (90, 750))

        elif n_image == 10:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_4, (90, 750))

        elif n_image == 11:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_5, (90, 750))

        elif n_image == 12:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_6, (90, 750))

        elif n_image == 13:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_7, (90, 750))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "StartFight.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song

        elif n_image == 14:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            print("HO VINTO!")

    # movements
    if n_livello == 1:
        if moving_right == True:
            player_location[0] += 4
            player_locx = player_location[0]
            print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        if moving_left == True:
            if player_location[0] < 60 and player_location[1] > 330:
                print("I can't go here")
            else:
                player_location[0] -= 4
                player_locx = player_location[0]
                print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        if moving_up == True:
            if player_location[1] < 334:
                print("I can't go here")
            else:
                player_location[1] -= 4
                player_locy = player_location[1]
                print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        if moving_down == True:
            if player_location[0] == 56 and player_location[1] > 346:
                print("I can't go here")
            else:
                player_location[1] += 4
                player_locy = player_location[1]
                print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

    elif n_livello == 2:
        #print("Livello: " + str(n_livello))
        if n_image != 5:
            if n_image < 7 or n_image > 13:
                if moving_right == True:
                    player_location2[0] += 3
                    player_locx = player_location2[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if n_image == 6:
                        if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                            n_image = 7

                if moving_left == True:
                    player_location2[0] -= 3
                    player_locx = player_location2[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if n_image == 6:
                        if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                            n_image = 7

                if moving_up == True:
                    player_location2[1] -= 3
                    player_locy = player_location2[1]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if n_image == 6:
                        if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                            n_image = 7

                if moving_down == True:
                    player_location2[1] += 3
                    player_locy = player_location2[1]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if n_image == 6:
                        if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                            n_image = 7
        else:
            print("Dialogo...")
    #gestione eventi

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if n_image == 6:
                n_image = 6
            else:
                n_image = n_image + 1

        if event.type == KEYDOWN:
            # movements keyboard
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = True
            if event.key == K_LEFT or event.key == K_a:
                moving_left = True

            if event.key == K_UP or event.key == K_w:
                moving_up = True
            if event.key == K_DOWN or event.key == K_s:
                moving_down = True

            if event.key == K_o:
                obiettivo_check = True
                show_obiettivo(n_obiettivo)


        if event.type == KEYUP:
            # movements keyboard
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = False
            if event.key == K_LEFT or event.key == K_a:
                moving_left = False

            if event.key == K_UP or event.key == K_w:
                moving_up = False
            if event.key == K_DOWN or event.key == K_s:
                moving_down = False

            if event.key == K_o:
                obiettivo_check = False

        #movements controller

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['left_arrow']:
                moving_left = True
            if event.button == button_keys['right_arrow']:
                moving_right = True
            if event.button == button_keys['down_arrow']:
                moving_down = True
            if event.button == button_keys['up_arrow']:
                moving_up = True

            if event.button == button_keys['x']:
                if n_image == 6:
                    n_image = 6
                else:
                    n_image = n_image + 1

        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['left_arrow']:
                moving_left = False
            if event.button == button_keys['right_arrow']:
                moving_right = False
            if event.button == button_keys['down_arrow']:
                moving_down = False
            if event.button == button_keys['up_arrow']:
                moving_up = False

                # HANDLES ANALOG INPUTS
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            # print(analog_keys)
            # Horizontal Analog
            if abs(analog_keys[0]) > .4:
                if analog_keys[0] < -.7:
                    moving_left = True
                else:
                    moving_left = False
                if analog_keys[0] > .7:
                    moving_right = True
                else:
                    moving_right = False
            # Vertical Analog
            if abs(analog_keys[1]) > .4:
                if analog_keys[1] < -.7:
                    moving_up = True
                else:
                    moving_up = False
                if analog_keys[1] > .7:
                    moving_down = True
                else:
                    moving_down = False
                # Triggers
            """
            if analog_keys[4] > 0:  # Left trigger
                color += 2
            if analog_keys[5] > 0:  # Right Trigger
                color -= 2
            """

    pygame.display.update()
    clock.tick(60)

#to do:

#inventario (I)
#mappa (m)
#gameplay stile pou --> golden apple
#raccolta monete --> entrata ristorante
#aggiunta effetti grafici
#comandi da controller --> already done
