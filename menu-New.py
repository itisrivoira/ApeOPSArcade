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

#misc
font = pygame.font.SysFont(None, 45)
bg_image = pygame.image.load("images/bgwhite.jpg")

#personaggi
pg_win = pygame.image.load("images/protagWin.png")
pg_image = pygame.image.load("images/hornyProtag.png")
pg_punch = pygame.image.load("images/medicPunch.png")
pg_kick = pygame.image.load("images/medicKick.png")
pg_fire = pygame.image.load("images/protagFire.png")
pg_slash = pygame.image.load("images/protagSlash.png")
iconpg_image = pygame.image.load("images/medic_Icon.png") #icon image pg

enemy_image = pygame.image.load("images/hornySalvini.png")
enemy_hit = pygame.image.load("images/brigadiereRuspa_hit.png")
iconen_image = pygame.image.load("images/salvini_Icon.png") #icon image enemy

#enemy 2
enemy2_image = pygame.image.load("images/chefNibba.png")
enemy2_fire = pygame.image.load("images/chefNibba_Fire.png")
enemy2_hit = pygame.image.load("images/chefNibba_hit.png")
iconEN2_img = pygame.image.load("images/chefNibba_icon.png")

#enemy 3 BOSS
enemy3_image = pygame.image.load("images/apeStand.png")
enemy3_slash = pygame.image.load("images/apeSlash.png")
enemy3_fire = pygame.image.load("images/apeFlameAtk.png")
enemy3_hit = pygame.image.load("images/apeHit.png")
iconEN3_img = pygame.image.load("images/apeIcon.png")

#fighting menu
menufight_image3 = pygame.image.load("menuAssets/menu_ingame_fight3.png")
menufight_image2 = pygame.image.load("menuAssets/menu_ingame_fight2.png")
menufight_image = pygame.image.load("menuAssets/menu_ingame_fight.png") #menu fighting

#pg hp
fullhppg_image = pygame.image.load("images/hp_heart.png") #icon image fullhp
halfhppg_image = pygame.image.load("images/hp_heart_half.png") #icon image halfhp
grayhppg_image = pygame.image.load("images/hp_heart_gray.png") #icon image grayhp

#enemy hp
fullhpen_image = pygame.image.load("images/hp_heart.png") #icon image fullhp
halfhpen_image = pygame.image.load("images/hp_heart_half.png") #icon image halfhp
grayhpen_image = pygame.image.load("images/hp_heart_gray.png") #icon image grayhp

#bgs
bg_lvl1 = pygame.image.load("images/bg_lvl1.png")
bg_lvl2 = pygame.image.load("images/bg_lvl2.png")
bg_lvl3 = pygame.image.load("images/bg_lvl3.png")


#window bgs
def redWindow():
    win = pygame.display.set_mode((W, H))
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))


def mainWindow(img_BG):
    win = pygame.display.set_mode((1280, 720))
    win.blit(img_BG, (0, 0))

def quitGame():
    pygame.quit()
    quit()


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

#reset
def reset():

    global currentEN_HP, currentPG_HP, hp_bar_en, hp_bar_pg, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, turnNMB, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf, levelCount

    if levelCount == 1:
        if hp_bar_en == []:
            levelCount = 2
        elif hp_bar_pg == []:
            levelCount = 1
    elif levelCount == 2:
        if hp_bar_en == []:
            levelCount = 3
        elif hp_bar_pg == []:
            levelCount = 1
    elif levelCount == 3:
        if hp_bar_en == []:
            levelCount = 1
        elif hp_bar_pg == []:
            levelCount = 1

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
    hpENcheck = [True, True, True]
    hpPGcheck = [True, True, True]
    hpENhalf = [False, False, False]
    hpPGhalf = [False, False, False]

#-------------- VARIABILI ---------------- 
config = {'DEBUG': False, 'sound_effects': True, 'background_music': True, 'show_score': True, 'high_scores': [0, 0, 0, 0, 0, 0, 0, 0, 0]}
hp_bar_pg = [ fullhppg_image, fullhppg_image, fullhppg_image ]
hp_bar_en = [ fullhpen_image, fullhpen_image, fullhppg_image ]
currentPG_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
currentEN_HP = [ fullhpen_image, fullhpen_image, fullhppg_image ]
hpENcheck = [True, True, True]
hpPGcheck = [True, True, True]
# True = Full HP Heart || False = Gray HP Heart
hpENhalf = [False, False, False]
hpPGhalf = [False, False, False]
# False = Full / Gray heart || True = Half Heart



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
levelCount = 1

pygame.mixer.music.load( "./Sound/ncsound.ogg" )  # Get the first track from the playlist
pygame.mixer.music.play(-1) 

#msg to screen
def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [x, y])

#lista comandi
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

#function toggle button for sounds
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

#entire option menu
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

#function menu button
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

#function command button
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

#function ingame button
def gameButton(x, y, w, h, action, turn = True, click = False):
    
    global turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, turnNMB, levelCount
    mouse = pygame.mouse.get_pos()
    clickedBtn = pygame.mouse.get_pressed()
    val = False
    if turn == True: 
        if x + w > mouse[0] > x and y + h > mouse[1] > y:   
            if clickedBtn[0] == 1 and action != None:
                
                if levelCount == 1:    
                    if action == event_Dodge:
                        dodgeCheck_PG = True
                        print(dodgeCheck_PG)
                        action()
                    elif action == event_Block:
                        blockCheck_PG = True
                        print(blockCheck_PG)
                        action()
                    else:
                        action()
                
                elif levelCount == 2:
                    if action == event_Dodge2:
                        dodgeCheck_PG = True
                        print(dodgeCheck_PG)
                        action()
                    elif action == event_Block2:
                        blockCheck_PG = True
                        print(blockCheck_PG)
                        action()
                    else:
                        action()
                
                elif levelCount == 3:
                    if action == event_Dodge3:
                        dodgeCheck_PG = True
                        print(dodgeCheck_PG)
                        action()
                    elif action == event_Block3:
                        blockCheck_PG = True
                        print(blockCheck_PG)
                        action()
                    else:
                        action()                                            
                turnCheck = False
                turnNMB = 1
            if click and pygame.time.get_ticks() > 100:
                val = True
    
    return val

#win or lose screen with reset
def endScreen():

    global currentEN_HP, currentPG_HP, hp_bar_en, hp_bar_pg, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, turnNMB, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf, levelCount

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if levelCount == 1:
                    pygame.time.wait(150)
                    if hp_bar_en == []:
                        levelCount += 1
                    elif hp_bar_pg == []:
                        levelCount = 1
                        run = False
                
                elif levelCount == 2:
                    pygame.time.wait(150)                    
                    if hp_bar_en == []:
                        levelCount += 1
                    elif hp_bar_pg == []:
                        levelCount = 1
                        run = False
                
                elif levelCount == 3:
                    pygame.time.wait(150)                    
                    if hp_bar_en == []:
                        levelCount += 1
                    elif hp_bar_pg == []:
                        levelCount = 1
                        run = False
                else:
                    pygame.time.wait(150)
                    levelCount = 1
                    run = False
        
        if hp_bar_pg == []:
            pygame.time.wait(150)
            redWindow()
            death = pygame.image.load(os.path.join('menuAssets', 'died.png'))
            restart = pygame.image.load(os.path.join('menuAssets', 'restart.png'))
            win.blit(death, (W/4, H/3 - 50))
            win.blit(restart, (W/4 - 10, H / 2))
            pygame.display.update()
        elif hp_bar_en == []:
            pygame.time.wait(150)
            redWindow()
            winPG = pygame.image.load(os.path.join('menuAssets', 'youWon.png'))
            restart = pygame.image.load(os.path.join('menuAssets', 'restart.png'))
            win.blit(winPG, (W/4 - 25, H/3 - 50))
            win.blit(restart, (W/4 - 10, H / 2))
            pygame.display.update() 

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
    hpENcheck = [True, True, True]
    hpPGcheck = [True, True, True]
    hpENhalf = [False, False, False]
    hpPGhalf = [False, False, False]

#video
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

#HP del personaggio
def pg_HP():
    global hp_bar_pg, currentPG_HP
    x_pos = 150
    for i in range(len(currentPG_HP)):
        win.blit(currentPG_HP[i], (x_pos, 40))
        x_pos += 65

#HP del nemico
def en_HP():
    global hp_bar_en, currentEN_HP
    x_pos = 920
    for i in range(len(currentEN_HP)):
        win.blit(currentEN_HP[i], (x_pos, 40))
        x_pos += 65

#evento punch livello 1
def event_Punch():    
    global pg_image, enemy_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf
    global levelCount
    if levelCount == 2:
        return    
    
    x = 100
    pg_image.fill(transparent)
    enemy_image.fill(transparent)
    game_layout()
    
    if turnCheck == True:
        #Turno Protagonista
        if dodgeCheck_EN == False and blockCheck_EN == False:    
            win.blit(enemy_hit, (900, 110))
            win.blit(pg_punch, (770, 85))
            message_to_screen("LEGASOV USES PUNCH", BLACK, 490, 40)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    if hpENcheck[i] == True:   
                        currentEN_HP[i] = grayhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                    elif hpENhalf[i] == True:
                        currentEN_HP[i] = grayhpen_image
                        currentEN_HP[i - 1] = halfhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                        if i >= 1:    
                            hpENhalf[i - 1] = True
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                        en_HP()

        else:
            if dodgeCheck_EN == True:
                blockCheck_EN = False
                message_to_screen("RUSPA USES DODGE", BLACK, 490, 40) 
                message_to_screen("LEGASOV USES PUNCH", BLACK, 505, 70)
                win.blit(pg_punch, (770, 110))
        
            elif blockCheck_EN == True:
                dodgeCheck_EN = False
                message_to_screen("RUSPA USES BLOCK", BLACK, 490, 40) 
                message_to_screen("LEGASOV USES PUNCH", BLACK, 505, 70)
                win.blit(pg_punch, (770, 110))
                win.blit(enemy_hit, (900, 110))
                
                for i in range(len(hp_bar_en)):
                    if i == (len(hp_bar_en) - 1):
                        if hpENcheck[i] == True:   
                            currentEN_HP[i] = halfhpen_image
                            hpENcheck[i] = False
                            hpENhalf[i] = True
                        elif hpENhalf[i] == True:
                            currentEN_HP[i] = grayhpen_image
                            hp_bar_en.pop(i)
                            hpENcheck[i] = False
                            hpENhalf[i] = False   
    else:
        #Turno Nemico
        if dodgeCheck_PG == False and blockCheck_PG == False:    
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy_hit, (180, 110))
            message_to_screen("RUSPA USES PUNCH", BLACK, 500, 40)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    if hpPGcheck[i] == True:   
                        currentPG_HP[i] = grayhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                    elif hpPGhalf[i] == True:
                        currentPG_HP[i] = grayhpen_image
                        currentPG_HP[i - 1] = halfhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                        if i >= 1:    
                            hpPGhalf[i - 1] = True
        
        else:
            if dodgeCheck_PG == True:
                blockCheck_PG = False
                message_to_screen("LEGASOV USES DODGE", BLACK, 490, 40)
                message_to_screen("RUSPA USES PUNCH", BLACK, 505, 70)
                win.blit(enemy_hit, (180, 110))
        
            elif blockCheck_PG == True:
                dodgeCheck_PG = True
                message_to_screen("LEGASOV USES BLOCK", BLACK, 490, 40)
                message_to_screen("RUSPA USES PUNCH", BLACK, 505, 70)
                win.blit(pg_image, (100, 85)) 
                win.blit(enemy_hit, (180, 110))
                
                for i in range(len(hp_bar_pg)):
                    if i == (len(hp_bar_pg) - 1):
                        if hpPGcheck[i] == True:   
                            currentPG_HP[i] = halfhpen_image
                            hpPGcheck[i] = False
                            hpPGhalf[i] = True
                        elif hpPGhalf[i] == True:
                            currentPG_HP[i] = grayhpen_image
                            hp_bar_pg.pop(i)
                            hpPGcheck[i] = False
                            hpPGhalf[i] = False 

    dodgeCheck_PG = False   
    dodgeCheck_EN = False    
    blockCheck_EN = False
    blockCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy_image = pygame.image.load("images/hornySalvini.png")

#evento kick livello 1
def event_Kick():
    global pg_image, enemy_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf
    global levelCount
    if levelCount == 2:
        return
    
    x = 100
    pg_image.fill(transparent)
    enemy_image.fill(transparent)
    game_layout()

    
    if turnCheck == True:
        #Turno Protagonista 
        if dodgeCheck_EN == False and blockCheck_EN == False:    
            #NO DAMAGE REDUCTION OR DODGE
            win.blit(enemy_hit, (900, 110))
            win.blit(pg_kick, (770, 85))
            message_to_screen("LEGASOV USES KICK", BLACK, 490, 40)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    if hpENcheck[i] == True:   
                        currentEN_HP[i] = grayhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                    elif hpENhalf[i] == True:
                        currentEN_HP[i] = grayhpen_image
                        currentEN_HP[i - 1] = halfhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                        if i >= 1:    
                            hpENhalf[i - 1] = True
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                        en_HP()                    
        
        else:
            if dodgeCheck_EN == True:
                #DODGED -- SCHIVATO
                blockCheck_EN = False
                message_to_screen("RUSPA USES DODGE", BLACK, 490, 40) 
                message_to_screen("LEGASOV USES KICK", BLACK, 505, 70)
                win.blit(pg_kick, (770, 110))
        
            elif blockCheck_EN == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_EN = False
                message_to_screen("RUSPA USES BLOCK", BLACK, 490, 40) 
                message_to_screen("LEGASOV USES KICK", BLACK, 505, 70)
                win.blit(pg_kick, (770, 110))
                win.blit(enemy_hit, (900, 110))
                for i in range(len(hp_bar_en)):
                    if i == (len(hp_bar_en) - 1):
                        if hpENcheck[i] == True:   
                            currentEN_HP[i] = halfhpen_image
                            hpENcheck[i] = False
                            hpENhalf[i] = True
                        elif hpENhalf[i] == True:
                            currentEN_HP[i] = grayhpen_image
                            hp_bar_en.pop(i)
                            hpENcheck[i] = False
                            hpENhalf[i] = False
    else:
        #Turno Nemico
        if dodgeCheck_PG == False and blockCheck_PG == False:    
            #NO DAMAGE REDUCTION OR DODGE
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy_hit, (180, 110))
            message_to_screen("RUSPA USES KICK", BLACK, 500, 40)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    if hpPGcheck[i] == True:   
                        currentPG_HP[i] = grayhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                    elif hpPGhalf[i] == True:
                        currentPG_HP[i] = grayhpen_image
                        currentPG_HP[i - 1] = halfhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                        if i >= 1:    
                            hpPGhalf[i - 1] = True
        
        else:
            if dodgeCheck_PG == True:
                #DODGED -- SCHIVATO
                blockCheck_PG = False
                message_to_screen("LEGASOV USES DODGE", BLACK, 490, 40)
                message_to_screen("RUSPA USES KICK", BLACK, 505, 70)
                win.blit(enemy_hit, (180, 110))
        
            elif blockCheck_PG == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 490, 40)
                message_to_screen("RUSPA USES KICK", BLACK, 505, 70)
                win.blit(pg_image, (100, 85)) 
                win.blit(enemy_hit, (180, 110))
                
                for i in range(len(hp_bar_pg)):
                    if i == (len(hp_bar_pg) - 1):
                        if hpPGcheck[i] == True:   
                            currentPG_HP[i] = halfhpen_image
                            hpPGcheck[i] = False
                            hpPGhalf[i] = True
                        elif hpPGhalf[i] == True:
                            currentPG_HP[i] = grayhpen_image
                            hp_bar_pg.pop(i)
                            hpPGcheck[i] = False
                            hpPGhalf[i] = False   


    dodgeCheck_EN = False
    dodgeCheck_PG = False
    blockCheck_EN = False
    blockCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)    
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy_image = pygame.image.load("images/hornySalvini.png")

#evento dodge livello 1
def event_Dodge():
    global dodgeCheck_PG, dodgeCheck_EN
    global levelCount
    if levelCount == 2:
        return
    pass

#evento block livello 1
def event_Block():
    global blockCheck_PG, blockCheck_EN
    global levelCount
    if levelCount == 2:
        return
    pass

#evento nemico livello 1
def event_Enemy():
    global turnCheck, dodgeCheck_EN, blockCheck_EN
    global levelCount
    if levelCount == 2:
        return
    
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


#evento new weapon livello 2
def event_Fire():    
    global pg_image, enemy2_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf
    x = 100
    if levelCount == 3:
        return
    
    pg_image.fill(transparent)
    enemy2_image.fill(transparent)
    game_layout2()
    
    if turnCheck == True:
        #Turno Protagonista
        if dodgeCheck_EN == False and blockCheck_EN == False:    
            win.blit(enemy2_hit, (900, 110))
            win.blit(pg_fire, (210, 70))
            message_to_screen("LEGASOV USES FIREOUT", BLACK, 470, 60)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                    elif hpENcheck[i] == True:   
                        currentEN_HP[i] = grayhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                    elif hpENhalf[i] == True:
                        currentEN_HP[i] = grayhpen_image
                        currentEN_HP[i - 1] = halfhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                        if i >= 1:    
                            hpENhalf[i - 1] = True
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                        en_HP()

        else:
            if dodgeCheck_EN == True:
                blockCheck_EN = False
                message_to_screen("MATTARELLA USES DODGE", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES FIREOUT", BLACK, 485, 90)
                win.blit(pg_fire, (210, 70))
        
            elif blockCheck_EN == True:
                dodgeCheck_EN = False
                message_to_screen("MATTARELLA USES BLOCK", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES FIREOUT", BLACK, 485, 90)
                win.blit(enemy2_hit, (900, 110))
                win.blit(pg_fire, (210, 70))
                
                for i in range(len(hp_bar_en)):
                    if i == (len(hp_bar_en) - 1):
                        if hpENcheck[i] == True:   
                            currentEN_HP[i] = halfhpen_image
                            hpENcheck[i] = False
                            hpENhalf[i] = True
                        elif hpENhalf[i] == True:
                            currentEN_HP[i] = grayhpen_image
                            hp_bar_en.pop(i)
                            hpENcheck[i] = False
                            hpENhalf[i] = False   
    else:
        #Turno Nemico
        if dodgeCheck_PG == False and blockCheck_PG == False:    
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy2_fire, (250, 110))
            message_to_screen("MATTARELLA USES INCENDIO", BLACK, 450, 60)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    if hpPGcheck[i] == True:   
                        currentPG_HP[i] = grayhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                    elif hpPGhalf[i] == True:
                        currentPG_HP[i] = grayhpen_image
                        currentPG_HP[i - 1] = halfhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                        if i >= 1:    
                            hpPGhalf[i - 1] = True
        
        else:
            if dodgeCheck_PG == True:
                blockCheck_PG = False
                message_to_screen("LEGASOV USES DODGE", BLACK, 460, 60)
                message_to_screen("MATTARELLA USES INCENDIO", BLACK, 450, 90)
                win.blit(enemy2_fire, (250, 110))
        
            elif blockCheck_PG == True:
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("MATTARELLA USES INCENDIO", BLACK, 450, 90)
                win.blit(pg_image, (100, 85)) 
                win.blit(enemy2_fire, (250, 110))
                
                for i in range(len(hp_bar_pg)):
                    if i == (len(hp_bar_pg) - 1):
                        if hpPGcheck[i] == True:   
                            currentPG_HP[i] = halfhpen_image
                            hpPGcheck[i] = False
                            hpPGhalf[i] = True
                        elif hpPGhalf[i] == True:
                            currentPG_HP[i] = grayhpen_image
                            hp_bar_pg.pop(i)
                            hpPGcheck[i] = False
                            hpPGhalf[i] = False 

    dodgeCheck_PG = False   
    dodgeCheck_EN = False    
    blockCheck_EN = False
    blockCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy2_image = pygame.image.load("images/chefNibba.png")

#evento kick livello 2
def event_Kick2():
    global pg_image, enemy2_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf
    x = 100
    if levelCount == 3:
        return    
    pg_image.fill(transparent)
    enemy2_image.fill(transparent)
    game_layout2()
    
    if turnCheck == True:
        #Turno Protagonista 
        if dodgeCheck_EN == False and blockCheck_EN == False:    
            #NO DAMAGE REDUCTION OR DODGE
            win.blit(enemy2_hit, (900, 110))
            win.blit(pg_kick, (770, 85))
            message_to_screen("LEGASOV USES KICK", BLACK, 470, 60)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                    elif hpENcheck[i] == True:   
                        currentEN_HP[i] = grayhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                    elif hpENhalf[i] == True:
                        currentEN_HP[i] = grayhpen_image
                        currentEN_HP[i - 1] = halfhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                        if i >= 1:    
                            hpENhalf[i - 1] = True
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                        en_HP()

        else:
            if dodgeCheck_EN == True:
                #DODGED -- SCHIVATO
                blockCheck_EN = False
                message_to_screen("MATTARELLA USES DODGE", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES KICK", BLACK, 470, 90)
                win.blit(pg_kick, (770, 110))
        
            elif blockCheck_EN == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_EN = False
                message_to_screen("MATTARELLA USES BLOCK", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES KICK", BLACK, 470, 90)
                win.blit(enemy2_hit, (900, 110))
                win.blit(pg_kick, (770, 110))
                
                for i in range(len(hp_bar_en)):
                    if i == (len(hp_bar_en) - 1):
                        if hpENcheck[i] == True:   
                            currentEN_HP[i] = halfhpen_image
                            hpENcheck[i] = False
                            hpENhalf[i] = True
                        elif hpENhalf[i] == True:
                            currentEN_HP[i] = grayhpen_image
                            hp_bar_en.pop(i)
                            hpENcheck[i] = False
                            hpENhalf[i] = False
    else:
        #Turno Nemico
        if dodgeCheck_PG == False and blockCheck_PG == False:    
            #NO DAMAGE REDUCTION OR DODGE
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy2_hit, (180, 110))
            message_to_screen("MATTARELLA USES KICK", BLACK, 450, 60)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    if hpPGcheck[i] == True:   
                        currentPG_HP[i] = grayhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                    elif hpPGhalf[i] == True:
                        currentPG_HP[i] = grayhpen_image
                        currentPG_HP[i - 1] = halfhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                        if i >= 1:    
                            hpPGhalf[i - 1] = True
        
        else:
            if dodgeCheck_PG == True:
                #DODGED -- SCHIVATO
                blockCheck_PG = False
                message_to_screen("LEGASOV USES DODGE", BLACK, 460, 60)
                message_to_screen("MATTARELLA USES KICK", BLACK, 450, 90)
                win.blit(enemy2_hit, (200, 110))
        
            elif blockCheck_PG == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("MATTARELLA USES KICK", BLACK, 450, 90)
                win.blit(pg_image, (100, 85)) 
                win.blit(enemy2_hit, (200, 110))
                
                for i in range(len(hp_bar_pg)):
                    if i == (len(hp_bar_pg) - 1):
                        if hpPGcheck[i] == True:   
                            currentPG_HP[i] = halfhpen_image
                            hpPGcheck[i] = False
                            hpPGhalf[i] = True
                        elif hpPGhalf[i] == True:
                            currentPG_HP[i] = grayhpen_image
                            hp_bar_pg.pop(i)
                            hpPGcheck[i] = False
                            hpPGhalf[i] = False   

    dodgeCheck_EN = False
    dodgeCheck_PG = False
    blockCheck_EN = False
    blockCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)    
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy2_image = pygame.image.load("images/chefNibba.png")

#evento dodge livello 2
def event_Dodge2():
    global dodgeCheck_PG, dodgeCheck_EN
    if levelCount == 3:
        return    
    pass

#evento block livello 2
def event_Block2():
    global blockCheck_PG, blockCheck_EN
    if levelCount == 3:
        return    
    pass

#evento nemico livello 2
def event_Enemy2():
    global turnCheck, dodgeCheck_EN, blockCheck_EN
    if levelCount == 3:
        return
    
    move = random.randint(0, 3)
    if move == 0:
        print("MATTARELLA PUNCH")
        event_Fire()
    
    if move == 1:
        print("MATTARELLA KICK")
        event_Kick2()
    
    if move == 2:
        print("MATTARELLA DODGE")
        event_Dodge2()
        dodgeCheck_EN = True
    
    if move == 3:
        print("MATTARELLA BLOCK")
        event_Block2()
        blockCheck_EN = True

    turnCheck = True
    pygame.time.wait(250)


#evento 1st atk lvl 3
def event_Fire2():    
    global pg_image, enemy3_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf
    x = 100
    pg_image.fill(transparent)
    enemy3_image.fill(transparent)
    game_layout3()
    
    if turnCheck == True:
        #Turno Protagonista
        if dodgeCheck_EN == False and blockCheck_EN == False:    
            win.blit(enemy3_hit, (900, 110))
            win.blit(pg_fire, (210, 70))
            message_to_screen("LEGASOV USES FIREOUT", BLACK, 470, 60)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                    elif hpENcheck[i] == True:   
                        currentEN_HP[i] = grayhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                    elif hpENhalf[i] == True:
                        currentEN_HP[i] = grayhpen_image
                        currentEN_HP[i - 1] = halfhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                        if i >= 1:    
                            hpENhalf[i - 1] = True
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                        en_HP()

        else:
            if dodgeCheck_EN == True:
                blockCheck_EN = False
                message_to_screen("APE USES DODGE", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES FIREOUT", BLACK, 485, 90)
                win.blit(pg_fire, (210, 70))
        
            elif blockCheck_EN == True:
                dodgeCheck_EN = False
                message_to_screen("APE USES BLOCK", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES FIREOUT", BLACK, 485, 90)
                win.blit(enemy3_hit, (900, 110))
                win.blit(pg_fire, (210, 70))
                
                for i in range(len(hp_bar_en)):
                    if i == (len(hp_bar_en) - 1):
                        if hpENcheck[i] == True:   
                            currentEN_HP[i] = halfhpen_image
                            hpENcheck[i] = False
                            hpENhalf[i] = True
                        elif hpENhalf[i] == True:
                            currentEN_HP[i] = grayhpen_image
                            hp_bar_en.pop(i)
                            hpENcheck[i] = False
                            hpENhalf[i] = False   
    else:
        #Turno Nemico
        if dodgeCheck_PG == False and blockCheck_PG == False:    
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy3_fire, (250, 110))
            message_to_screen("APE USES FLAME MANTLE", BLACK, 450, 60)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    if hpPGcheck[i] == True:   
                        currentPG_HP[i] = grayhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                    elif hpPGhalf[i] == True:
                        currentPG_HP[i] = grayhpen_image
                        currentPG_HP[i - 1] = halfhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                        if i >= 1:    
                            hpPGhalf[i - 1] = True
        
        else:
            if dodgeCheck_PG == True:
                blockCheck_PG = False
                message_to_screen("LEGASOV USES DODGE", BLACK, 460, 60)
                message_to_screen("APE USES FLAME MANTLE", BLACK, 450, 90)
                win.blit(enemy3_fire, (250, 110))
        
            elif blockCheck_PG == True:
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("APE USES FLAME MANTLE", BLACK, 450, 90)
                win.blit(pg_image, (100, 85)) 
                win.blit(enemy3_fire, (250, 110))
                
                for i in range(len(hp_bar_pg)):
                    if i == (len(hp_bar_pg) - 1):
                        if hpPGcheck[i] == True:   
                            currentPG_HP[i] = halfhpen_image
                            hpPGcheck[i] = False
                            hpPGhalf[i] = True
                        elif hpPGhalf[i] == True:
                            currentPG_HP[i] = grayhpen_image
                            hp_bar_pg.pop(i)
                            hpPGcheck[i] = False
                            hpPGhalf[i] = False 

    dodgeCheck_PG = False   
    dodgeCheck_EN = False    
    blockCheck_EN = False
    blockCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy3_image = pygame.image.load("images/apeStand.png")


#evento kick / 2nd atk livello 3
def event_Slash():
    global pg_image, enemy3_image, hp_bar_en, hp_bar_pg, currentEN_HP, currentPG_HP, turnCheck, dodgeCheck_EN, dodgeCheck_PG, blockCheck_EN, blockCheck_PG, hpENcheck, hpPGcheck, hpENhalf, hpPGhalf
    x = 100
    pg_image.fill(transparent)
    enemy3_image.fill(transparent)
    game_layout3()
    
    if turnCheck == True:
        #Turno Protagonista 
        if dodgeCheck_EN == False and blockCheck_EN == False:    
            #NO DAMAGE REDUCTION OR DODGE
            win.blit(enemy3_hit, (900, 110))
            win.blit(pg_slash, (770, 85))
            message_to_screen("LEGASOV USES SLASH", BLACK, 470, 60)    
            
            for i in range(len(hp_bar_en)):
                if i == (len(hp_bar_en) - 1):
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                    elif hpENcheck[i] == True:   
                        currentEN_HP[i] = grayhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                    elif hpENhalf[i] == True:
                        currentEN_HP[i] = grayhpen_image
                        currentEN_HP[i - 1] = halfhpen_image
                        hp_bar_en.pop(i)
                        hpENcheck[i] = False
                        if i >= 1:    
                            hpENhalf[i - 1] = True
                    if currentEN_HP == [ grayhpen_image, grayhpen_image, halfhpen_image ]:
                        currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]
                        en_HP()

        else:
            if dodgeCheck_EN == True:
                #DODGED -- SCHIVATO
                blockCheck_EN = False
                message_to_screen("APE USES STELLAR DODGE", BLACK, 440, 60) 
                message_to_screen("LEGASOV USES SLASH", BLACK, 470, 90)
                win.blit(pg_slash, (770, 110))
        
            elif blockCheck_EN == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_EN = False
                message_to_screen("APE USES STELLAR BLOCK", BLACK, 440, 60) 
                message_to_screen("LEGASOV USES SLASH", BLACK, 470, 90)
                win.blit(enemy3_hit, (900, 110))
                win.blit(pg_slash, (770, 110))
                
                for i in range(len(hp_bar_en)):
                    if i == (len(hp_bar_en) - 1):
                        if hpENcheck[i] == True:   
                            currentEN_HP[i] = halfhpen_image
                            hpENcheck[i] = False
                            hpENhalf[i] = True
                        elif hpENhalf[i] == True:
                            currentEN_HP[i] = grayhpen_image
                            hp_bar_en.pop(i)
                            hpENcheck[i] = False
                            hpENhalf[i] = False
    else:
        #Turno Nemico
        if dodgeCheck_PG == False and blockCheck_PG == False:    
            #NO DAMAGE REDUCTION OR DODGE
            pg_image = pygame.image.load("images/hornyProtag.png")
            win.blit(pg_image, (100, 85))        
            win.blit(enemy3_slash, (180, 110))
            message_to_screen("APE USES STELLAR SLASH", BLACK, 450, 60)    
            
            for i in range(len(hp_bar_pg)):
                if i == (len(hp_bar_pg) - 1):
                    if hpPGcheck[i] == True:   
                        currentPG_HP[i] = grayhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                    elif hpPGhalf[i] == True:
                        currentPG_HP[i] = grayhpen_image
                        currentPG_HP[i - 1] = halfhpen_image
                        hp_bar_pg.pop(i)
                        hpPGcheck[i] = False
                        if i >= 1:    
                            hpPGhalf[i - 1] = True
        
        else:
            if dodgeCheck_PG == True:
                #DODGED -- SCHIVATO
                blockCheck_PG = False
                message_to_screen("LEGASOV USES DODGE", BLACK, 460, 60)
                message_to_screen("MATTARELLA USES KICK", BLACK, 450, 90)
                win.blit(enemy3_slash, (200, 110))
        
            elif blockCheck_PG == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("MATTARELLA USES KICK", BLACK, 450, 90)
                win.blit(pg_image, (100, 85)) 
                win.blit(enemy3_slash, (200, 110))
                
                for i in range(len(hp_bar_pg)):
                    if i == (len(hp_bar_pg) - 1):
                        if hpPGcheck[i] == True:   
                            currentPG_HP[i] = halfhpen_image
                            hpPGcheck[i] = False
                            hpPGhalf[i] = True
                        elif hpPGhalf[i] == True:
                            currentPG_HP[i] = grayhpen_image
                            hp_bar_pg.pop(i)
                            hpPGcheck[i] = False
                            hpPGhalf[i] = False   

    dodgeCheck_EN = False
    dodgeCheck_PG = False
    blockCheck_EN = False
    blockCheck_PG = False
    pg_HP()
    en_HP()
    pygame.display.flip()
    pygame.time.wait(750)
    message_to_screen(" ", transparent, 185, 40)    
    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy3_image = pygame.image.load("images/apeStand.png")


#evento dodge livello 3
def event_Dodge3():
    global dodgeCheck_PG, dodgeCheck_EN
    pass

#evento block livello 3
def event_Block3():
    global blockCheck_PG, blockCheck_EN
    pass


#evento nemico livello 3
def event_Enemy3():
    global turnCheck, dodgeCheck_EN, blockCheck_EN
    
    move = random.randint(0, 3)
    if move == 0:
        print("FLAME MANTLE")
        event_Fire2()
    
    if move == 1:
        print("STELLAR SLASH")
        event_Slash()
    
    if move == 2:
        print("STELLAR DODGE")
        event_Dodge3()
        dodgeCheck_EN = True
    
    if move == 3:
        print("STELLAR BLOCK")
        event_Block3()
        blockCheck_EN = True

    turnCheck = True
    pygame.time.wait(250)


#vittoria player png
def player_win():
    global pg_image, enemy_image, currentEN_HP

    mainWindow(bg_lvl1)
    pg_image.fill(transparent)
    enemy_image.fill(transparent)
    currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]

    game_layout()   
    win.blit(enemy_hit, (900, 110))
    win.blit(pg_win,(100,85))
    pygame.display.flip()
    pygame.time.wait(750)

    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy_image = pygame.image.load("images/hornySalvini.png")


#vittoria player png 2
def player_win2():
    global pg_image, enemy2_image, currentEN_HP

    mainWindow(bg_lvl2)
    pg_image.fill(transparent)
    enemy2_image.fill(transparent)
    currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]

    game_layout2()
    win.blit(enemy2_hit, (900, 110))
    win.blit(pg_win,(100,85))
    pygame.display.flip()
    pygame.time.wait(750)

    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy2_image = pygame.image.load("images/chefNibba.png")


#vittoria player png 3
def player_win3():
    global pg_image, enemy3_image, currentEN_HP

    mainWindow(bg_lvl3)
    pg_image.fill(transparent)
    enemy3_image.fill(transparent)
    currentEN_HP = [ grayhpen_image, grayhpen_image, grayhpen_image ]

    game_layout3()
    win.blit(enemy3_hit, (900, 110))
    win.blit(pg_win,(100,85))
    pygame.display.flip()
    pygame.time.wait(750)

    pg_image = pygame.image.load("images/hornyProtag.png")
    enemy3_image = pygame.image.load("images/apeStand.png")


#livello 1
def game_layout():
    global levelCount
    if levelCount == 2:
        return
    
    win.blit(bg_lvl1, (0, 0))
    win.blit(pg_image,(100,85))  #pg
    win.blit(enemy_image,(900,110))  #enemy
    win.blit(menufight_image, (100, 475))    #menufight
    win.blit(iconpg_image, (10, 10)) #iconpg
    win.blit(iconen_image, (1175, 10))   #iconenemy
    pg_HP()
    en_HP()
    message_to_screen("KOWALSKI LEGASOV", BLACK, 85, 10)
    message_to_screen("LIVELLO 1", BLACK, 555, 10)
    message_to_screen("BRIGADIERE RUSPA", BLACK, 845, 10)
    pygame.display.update()


#livello 2
def game_layout2():
    global levelCount
    if levelCount > 2:
        return

    win.blit(bg_lvl2, (0, 0))
    win.blit(pg_image,(100,85))  #pg
    win.blit(enemy2_image,(900,110))  #enemy2
    win.blit(menufight_image2, (100, 475))    #menufight2
    win.blit(iconpg_image, (10, 10)) #iconpg
    win.blit(iconEN2_img, (1175, 10))   #iconenemy2
    pg_HP()
    en_HP()
    message_to_screen("KOWALSKI LEGASOV", BLACK, 85, 10)
    message_to_screen("LIVELLO 2", BLACK, 525, 10)
    message_to_screen("BRIGADIERE MATTARELLA", BLACK, 765, 10)
    pygame.display.update()


#livello 3
def game_layout3():
    global levelCount

    win.blit(bg_lvl3, (0, 0))
    win.blit(pg_image,(100,85))  #pg
    win.blit(enemy3_image,(900,110))  #enemy2
    win.blit(menufight_image3, (100, 475))    #menufight2
    win.blit(iconpg_image, (10, 10)) #iconpg
    win.blit(iconEN3_img, (1175, 10))   #iconenemy2
    pg_HP()
    en_HP()
    message_to_screen("KOWALSKI LEGASOV", BLACK, 85, 10)
    message_to_screen("LIVELLO 3", BLACK, 525, 10)
    message_to_screen("IL GORILLA STELLARE", BLACK, 765, 10)
    pygame.display.update()


#menu iniziale
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

#loop gioco
def game_loop():

    clock = pygame.time.Clock()

    global videoCheck, turnCheck, turnNMB, levelCount, hp_bar_en, hp_bar_pg
    runGame = True
    reset()
    while runGame:
        if levelCount == 1:
            mainWindow(bg_lvl1)
            game_layout()
            pygame.time.wait(150)

            if hp_bar_en == []:
                player_win()
                pygame.time.wait(1150)
                endScreen()
                turnCheck = True
                levelCount = 2

            if hp_bar_pg == []:
                pygame.time.wait(1150)
                endScreen()
                reset()
                game_intro()
                levelCount = 1

            if turnCheck == True:
                gameButton(162, 534, 257, 59, event_Punch, turnCheck)
                gameButton(445, 534, 257, 59, event_Kick, turnCheck)
                gameButton(162, 616, 257, 59, event_Dodge, turnCheck)
                gameButton(445, 616, 257, 59, event_Block, turnCheck)
            else:
                turnNMB = 0
                pygame.time.wait(400)
                event_Enemy()
        
        elif levelCount == 2:           
            mainWindow(bg_lvl2)
            game_layout2()
            pygame.time.wait(150)
            
            if hp_bar_en == []:
                player_win2()
                pygame.time.wait(1150)
                endScreen()
                turnCheck = True
                levelCount = 3

            if hp_bar_pg == []:
                pygame.time.wait(1150)
                endScreen()
                reset()
                game_intro()
                levelCount = 1

            if turnCheck == True:
                gameButton(162, 534, 257, 59, event_Fire, turnCheck)
                gameButton(445, 534, 257, 59, event_Kick2, turnCheck)
                gameButton(162, 616, 257, 59, event_Dodge2, turnCheck)
                gameButton(445, 616, 257, 59, event_Block2, turnCheck)
            else:
                turnNMB = 0
                pygame.time.wait(400)
                event_Enemy2()
        
        elif levelCount == 3:        
            mainWindow(bg_lvl3)
            game_layout3()
            pygame.time.wait(150)
            
            if hp_bar_en == []:
                player_win3()
                pygame.time.wait(1150)
                endScreen()
                game_intro()

            if hp_bar_pg == []:
                pygame.time.wait(1150)
                endScreen()
                game_intro()

            if turnCheck == True:
                gameButton(162, 534, 257, 59, event_Fire2, turnCheck)
                gameButton(445, 534, 257, 59, event_Slash, turnCheck)
                gameButton(162, 616, 257, 59, event_Dodge3, turnCheck)
                gameButton(445, 616, 257, 59, event_Block3, turnCheck)
            else:
                turnNMB = 0
                pygame.time.wait(400)
                event_Enemy3()


        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                runGame = False
                videoCheck = False
                turnCheck = True
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            pygame.time.wait(450)
            reset()
            game_intro()
    
    clock.tick(25)

game_intro()