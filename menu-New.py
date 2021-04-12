import pygame
from pygame.locals import *
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import os
import time
import sys
import math
import random
import cv2
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()
pygame.mixer.pre_init()
pygame.init()
random.seed()

font = pygame.font.SysFont(None, 45)
bg_image = pygame.image.load("images/bgwhite.jpg")
pg_win = pygame.image.load("images/protagWin.png")
enemy_hit = pygame.image.load("images/brigadiereRuspa_hit.png")
pg_image = pygame.image.load("images/hornyProtag.png") #protagonista
pg_punch = pygame.image.load("images/medicPunch.png")
pg_kick = pygame.image.load("images/medicKick.png")
#pg_dodge = pygame.image.load("images/medicPunch.png")
#pg_block = pygame.image.load("images/medicPunch.png")
enemy_image = pygame.image.load("images/hornySalvini.png") #nemico
menufight_image = pygame.image.load("menuAssets/menu_ingame_fight.png") #menu fighting
iconpg_image = pygame.image.load("images/medic_Icon.png") #icon image pg
iconen_image = pygame.image.load("images/salvini_Icon.png") #icon image enemy
#pg hp
fullhppg_image = pygame.image.load("images/hp_heart.png") #icon image fullhp
halfhppg_image = pygame.image.load("images/hp_heart_half.png") #icon image halfhp
grayhppg_image = pygame.image.load("images/hp_heart_gray.png") #icon image grayhp
#enemy hp
fullhpen_image = pygame.image.load("images/hp_heart.png") #icon image fullhp
halfhpen_image = pygame.image.load("images/hp_heart_half.png") #icon image halfhp
grayhpen_image = pygame.image.load("images/hp_heart_gray.png") #icon image grayhp



def redWindow():
    win = pygame.display.set_mode((W, H))
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))


def mainWindow():
    win = pygame.display.set_mode((1280, 720))
    win.fill(WHITE)
    pygame.display.update()


def quitGame():
    pygame.quit()
    quit()


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def reset():

    global currentEN_HP, currentPG_HP, hp_bar_en, hp_bar_pg, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, turnNMB

    turnNMB = 0
    dodgeCheck_EN = False
    dodgeCheck_PG = False
    blockCheck_EN = False
    blockCheck_PG = False
    turnCheck = True
    hp_bar_pg = [ fullhppg_image, fullhppg_image, fullhppg_image ]
    hp_bar_en = [ fullhpen_image, fullhpen_image, fullhppg_image ]
    currentPG_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
    currentEN_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
    game_intro()


config = {'DEBUG': False, 'sound_effects': True, 'background_music': True, 'show_score': True, 'high_scores': [0, 0, 0, 0, 0, 0, 0, 0, 0]}
hp_bar_pg = [ fullhppg_image, fullhppg_image, fullhppg_image ]
hp_bar_en = [ fullhpen_image, fullhpen_image, fullhppg_image ]
currentPG_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
currentEN_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]

W, H = 800, 447
W2, H2 = 1280, 720
#win2 = pygame.display.set_mode((W, H))
win = pygame.display.set_mode((W, H), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()
pygame.time.set_timer(USEREVENT + 1, random.randrange(2300, 3500))
speed = 60

WHITE = 255, 255, 255
BLACK = 0, 0, 0
MATTE_BLACK = 20, 20, 20
GREEN = 40, 175, 99
RED = 255, 0, 0
YELLOW = 250, 237, 39
DARK_GREEN = 0, 128, 0
LIGHT_BLUE = 25, 35, 255
GREY = 204, 204, 204
BLUE = 0, 0, 225
tmp = None
music_pause = False
pause = 0
fall_speed = 0
showMusicToggle = True
showSoundEffectToggle = True
videoCheck = False
transparent = (0, 0, 0, 0)
turnCheck = True
dodgeCheck_PG = False
blockCheck_PG = False
dodgeCheck_EN = False
blockCheck_EN = False
turnNMB = 0

pygame.mixer.music.load( "./Sound/ncsound.ogg" )  # Get the first track from the playlist
pygame.mixer.music.play(-1) 


def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [x, y])


def commandsList():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    pygame.display.update()
    show = True
    
    pygame.time.wait(150)
    while show:
        click = False
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4 and (pressed_keys[K_LALT] or pressed_keys[K_RALT]) or event.key == K_q))
            if event.type == QUIT or alt_f4:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                options_menu()
            elif event.type == MOUSEBUTTONDOWN:
                click = True
        
        #LEFT KEY
        cmdButton('left.png', 30, 25, 132, 70)
        cmdButton('leftarrowkey.png', 178, 50, 125, 31)
        
        #RIGHT KEY
        cmdButton('right.png', 30, 105, 151, 70)
        cmdButton('rightarrowkey.png', 173, 130, 133, 31)
        
        #UP KEY
        cmdButton('up.png', 30, 185, 97, 70)
        cmdButton('uparrowkey.png', 180, 210, 118, 31)
        
        #DOWN KEY
        cmdButton('down.png', 30, 265, 154, 70)
        cmdButton('downarrowkey.png', 175, 290, 136, 31)
        
        #RETURN KEY
        cmdButton('return.png', 350, 25, 190, 70)
        cmdButton('esckey.png', 540, 50, 90, 31)
        
        #RAGEQUIT KEY
        cmdButton('close.png', 350, 105, 269, 70)
        cmdButton('alt_f4key.png', 619, 130, 92, 31)
        
        #RETURN TO MENU
        menuButton('button_back_black.png', 550, 355, 124, 56, action = options_menu)
        
        pygame.display.update()


def menuToggle(x, y, w, h, click = False, SIMG = True, activeImage = None, inactiveImage = None):
    
    activeImage = pygame.image.load(os.path.join('menuAssets', 'toggle_on.png'))
    inactiveImage = pygame.image.load(os.path.join('menuAssets', 'toggle_off.png'))
    mouse = pygame.mouse.get_pos()
    clickedBtn = pygame.mouse.get_pressed()
    val = False
    btn = inactiveImage
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if clickedBtn[0] == 1:
            if not SIMG:
                win.blit(activeImage, (x, y))
                SIMG = False
            else:
                win.blit(inactiveImage, (x, y))
                SIMG = True

    return x + w > mouse[0] > x and y + h > mouse[1] > y and click and pygame.time.get_ticks() > 100


def options_menu():
    global music_pause, showMusicToggle, showSoundEffectToggle
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    pygame.display.update()
    show = True
    showBtn = False
    counter = 0
    mouse_x, mouse_y = 0, 0
    showMusic = pygame.image.load(os.path.join('menuAssets', 'option_music_toggle.png'))
    showSoundEffect = pygame.image.load(os.path.join('menuAssets', 'option_effects_toggle.png'))
    toggleOff = pygame.image.load(os.path.join('menuAssets', 'toggle_off.png'))
    toggleOn = pygame.image.load(os.path.join('menuAssets', 'toggle_on.png'))

    pygame.time.wait(150)
    while show:
        counter += 1
        click = False
        mouse = pygame.mouse.get_pos()
        clickedBtn = pygame.mouse.get_pressed()
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if showBtn == False:
                win.blit(showMusic, (125, 125))
                win.blit(showSoundEffect, (125, 250))
                win.blit(toggleOn, (550, 115))
                win.blit(toggleOn, (550, 240))
                showBtn = True
            
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4 and (pressed_keys[K_LALT] or pressed_keys[K_RALT]) or event.key == K_q))
            if event.type == QUIT or alt_f4:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                game_intro()
            elif event.type == MOUSEBUTTONDOWN:
                click = True
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if (mouse_x >= 550) and (mouse_x <= 550 + 138) and (mouse_y >= 115) and (mouse_y <= 115 + 54):
                        if showMusicToggle == True:
                            showMusicToggle = False
                            music_pause = True
                        else:
                            showMusicToggle = True
                            music_pause = False

                        if music_pause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    
                    elif (mouse_x >= 550) and (mouse_x <= 550 + 138) and (mouse_y >= 240) and (mouse_y <= 240 + 54):
                        if showSoundEffectToggle == True:
                            showSoundEffectToggle = False
                        else:
                            showSoundEffectToggle = True

            menuButton('button_commands_black.png', 180, 355, 200, 56, action = commandsList)
            menuButton('button_back_black.png', 500, 355, 124, 56, action = game_intro)
        
        if counter == 5:
            counter = 0
            if showMusicToggle == True:
                win.blit(toggleOn, (550, 115))
            else:
                win.blit(toggleOff, (550, 115))

            if showSoundEffectToggle == True:
                win.blit(toggleOn, (550, 240))
            else:
                win.blit(toggleOff, (550, 240))
    
        pygame.display.update()
    showBtn = False


def menuButton(img, x, y, w, h, click = False, action = None):
    
    global videoCheck
    btn = pygame.image.load(os.path.join('menuAssets', img))
    mouse = pygame.mouse.get_pos()
    clickedBtn = pygame.mouse.get_pressed()
    val = False
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if clickedBtn[0] == 1 and action != None:
            action()
        if click and pygame.time.get_ticks() > 100:
            val = True

    win.blit(btn, (x, y))
    return val


def cmdButton(img, x, y, w, h, click = False, action = None):
    btn = pygame.image.load(os.path.join('menuAssets/cmdAssets', img))
    mouse = pygame.mouse.get_pos()
    clickedBtn = pygame.mouse.get_pressed()
    val = False
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if clickedBtn[0] == 1 and action != None:
            action()
        if click and pygame.time.get_ticks() > 100:
            val = True

    win.blit(btn, (x, y))
    return val


def gameButton(x, y, w, h, action, turn = True, click = False):
    
    global turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, turnNMB
    mouse = pygame.mouse.get_pos()
    clickedBtn = pygame.mouse.get_pressed()
    val = False
    if turn == True: 
        if x + w > mouse[0] > x and y + h > mouse[1] > y:   
            if clickedBtn[0] == 1 and action != None:
                if action == event_Dodge:
                    action()
                    dodgeCheck_PG = True
                    print(dodgeCheck_PG)
                elif action == event_Block:
                    action()
                    blockCheck_PG = True
                    print(blockCheck_PG)
                else:
                    action()
                turnCheck = False
                turnNMB = 1
            if click and pygame.time.get_ticks() > 100:
                val = True
    
    return val


def endScreen():

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        
        redWindow()
        death = pygame.image.load(os.path.join('menuAssets', 'died.png'))
        restart = pygame.image.load(os.path.join('menuAssets', 'restart.png'))
        win.blit(death, (W/4, H/3 - 50))
        win.blit(restart, (W/4 - 10, H / 2))
        pygame.display.update()

    global currentEN_HP, currentPG_HP, hp_bar_en, hp_bar_pg, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, turnNMB

    turnNMB = 0
    dodgeCheck_EN = False
    dodgeCheck_PG = False
    blockCheck_EN = False
    blockCheck_PG = False
    turnCheck = True
    hp_bar_pg = [ fullhppg_image, fullhppg_image, fullhppg_image ]
    hp_bar_en = [ fullhpen_image, fullhpen_image, fullhppg_image ]
    currentPG_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
    currentEN_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
    game_intro()


def video():
    global videoCheck
    video = cv2.VideoCapture('./video/storyline.mp4') 
    while (video.isOpened()):
        ret, frame = video.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    
    videoCheck = True 
    video.release()
    cv2.destroyAllWindows()
    pygame.time.wait(1000)
    game_loop()


def pg_HP():
    global hp_bar_pg, currentPG_HP
    x_pos = 150
    for i in range(len(currentPG_HP)):
        win.blit(currentPG_HP[i], (x_pos, 40))
        x_pos += 65


def en_HP():
    global hp_bar_en, currentEN_HP
    x_pos = 920
    for i in range(len(currentEN_HP)):
        win.blit(currentEN_HP[i], (x_pos, 40))
        x_pos += 65


def event_Punch():    
    global pg_image, enemy_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG
    x = 100
    pg_image.fill(transparent)
    enemy_image.fill(transparent)
    game_layout()
    
    if turnCheck == True:
        if dodgeCheck_EN == False:    
            win.blit(enemy_hit, (900, 110))
            win.blit(pg_punch, (770, 85))
            message_to_screen("LEGASOV USES PUNCH", BLACK, 490, 40)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    currentEN_HP[i] = grayhpen_image
                    hp_bar_en.pop(i)
        elif dodgeCheck_EN == True:
            message_to_screen("RUSPA USES DODGE", BLACK, 490, 40) 
            message_to_screen("LEGASOV USES PUNCH", BLACK, 505, 70)
            win.blit(pg_punch, (180, 110))
    else:
        if dodgeCheck_PG == False:    
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy_hit, (180, 110))
            message_to_screen("RUSPA USES PUNCH", BLACK, 500, 40)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    currentPG_HP[i] = grayhpen_image
                    hp_bar_pg.pop(i)
        elif dodgeCheck_PG == True:
            message_to_screen("LEGASOV USES DODGE", BLACK, 490, 40)
            message_to_screen("RUSPA USES PUNCH", BLACK, 505, 70)
            win.blit(enemy_hit, (180, 110))
    
    dodgeCheck_PG = False   
    dodgeCheck_EN = False    
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy_image = pygame.image.load("images/hornySalvini.png")


def event_Kick():
    global pg_image, enemy_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG
    x = 100
    pg_image.fill(transparent)
    enemy_image.fill(transparent)
    game_layout()

    
    if turnCheck == True:
        if dodgeCheck_EN == False:    
            win.blit(enemy_hit, (900, 110))
            win.blit(pg_kick, (770, 85))
            message_to_screen("LEGASOV USES KICK", BLACK, 490, 40)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    currentEN_HP[i] = grayhpen_image
                    hp_bar_en.pop(i)
        elif dodgeCheck_EN == True:
            message_to_screen("RUSPA USES DODGE", BLACK, 490, 40) 
            message_to_screen("LEGASOV USES KICK", BLACK, 505, 70)
            win.blit(pg_kick, (180, 110))
    else:
        if dodgeCheck_PG == False:    
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy_hit, (180, 110))
            message_to_screen("RUSPA USES KICK", BLACK, 500, 40)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    currentPG_HP[i] = grayhpen_image
                    hp_bar_pg.pop(i)
        elif dodgeCheck_PG == True:
            message_to_screen("LEGASOV USES DODGE", BLACK, 490, 40)
            message_to_screen("RUSPA USES KICK", BLACK, 505, 70)
            win.blit(enemy_hit, (180, 110))
    
    dodgeCheck_EN = False
    dodgeCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)    
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy_image = pygame.image.load("images/hornySalvini.png")


def event_Dodge():
    global dodgeCheck_PG, dodgeCheck_EN
    pass
    #if dodgeCheck_PG == True:



def event_Block():
    global blockCheck_PG, blockCheck_EN
    pass
    # if blockCheck_PG == True:
    #     for i in range(len(currentPG_HP) + 1):
    #         if i == (len(hp_bar_pg)):
    #             currentPG_HP = currentPG_HP
        
    #     pg_HP()
    #     en_HP()
    #     pygame.display.flip()
    #     pygame.time.wait(750)
    #     message_to_screen(" ", transparent, 185, 40)    
    #     pg_image = pygame.image.load("images/hornyProtag.png")
    #     enemy_image = pygame.image.load("images/hornySalvini.png")
    
    # if blockCheck_EN = True:


def event_Enemy():
    global turnCheck, dodgeCheck_EN, blockCheck_EN
    
    move = random.randint(0, 3)
    if move == 0:
        print("RUSPA PUNCH")
        event_Punch()
    
    if move == 1:
        print("RUSPA KICK")
        event_Kick()
    
    if move == 2:
        print("RUSPA DODGE")
        event_Dodge()
        dodgeCheck_EN = True
    
    if move == 3:
        print("RUSPA BLOCK")
        event_Block()
        blockCheck_EN = True

    turnCheck = True
    pygame.time.wait(350)


def player_win():
    global pg_image, enemy_image

    mainWindow()
    pg_image.fill(transparent)
    enemy_image.fill(transparent)
    game_layout()
    
    win.blit(enemy_hit, (900, 110))
    win.blit(pg_win,(100,85))
    pygame.display.flip()
    pygame.time.wait(750)

    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy_image = pygame.image.load("images/hornySalvini.png")


def game_layout(): 
        win.blit(bg_image, (0, 0))
        win.blit(pg_image,(100,85))  #pg
        win.blit(enemy_image,(900,110))  #enemy
        win.blit(menufight_image, (100, 475))    #menufight
        win.blit(iconpg_image, (10, 10)) #iconpg
        win.blit(iconen_image, (1175, 10))   #iconenemy
        pg_HP()
        en_HP()
        message_to_screen("KOWALSKI LEGASOV", BLACK, 85, 10)
        message_to_screen("BRIGADIERE RUSPA", BLACK, 845, 10)
        pygame.display.update()


def game_intro():
    global videoCheck
    music_pause = False
    intro = True
    
    pygame.time.wait(150)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        redWindow()

        title = pygame.image.load(os.path.join('menuAssets', 'title.png'))
        win.blit(title, (25, 0))

        if videoCheck == False:
            menuButton("play_button.png", W/4 + 20, 215, 382, 80, action = video)
        else:
            menuButton("play_button.png", W/4 + 20, 215, 382, 80, action = game_loop)
        
        menuButton("options_button.png", W/3 - 10, 345, 301, 47, action = options_menu)
        
        pygame.display.update()


def game_loop():

    clock = pygame.time.Clock()

    global videoCheck, turnCheck, turnNMB
    runGame = True
    mainWindow()
    while runGame:
        game_layout()

        if hp_bar_en == []:
            player_win()
            pygame.time.wait(1150)
            endScreen()

        if hp_bar_pg == []:
            pygame.time.wait(1150)
            endScreen()

        if turnCheck == True:
            gameButton(162, 534, 257, 59, event_Punch, turnCheck)
            gameButton(445, 534, 257, 59, event_Kick, turnCheck)
            gameButton(162, 616, 257, 59, event_Dodge, turnCheck)
            gameButton(445, 616, 257, 59, event_Block, turnCheck)
        else:
            turnNMB = 0
            pygame.time.wait(400)
            event_Enemy()

        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                runGame = False
                videoCheck = False
                turnCheck = True
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            reset()
    
    clock.tick(25)

game_intro()