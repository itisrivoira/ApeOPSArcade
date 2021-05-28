from typing import Any
import pygame, sys, os
from pygame import gfxdraw
import time, random, json
clock = pygame.time.Clock()
from pygame.locals import *
import cv2
from os import environ

pygame.init() #inizializzo pygame
pygame.display.set_caption('Ape Ops Arcade')

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

    # if levelCount == 1:
    #     if hp_bar_en == []:
    #         levelCount = 2
    #     elif hp_bar_pg == []:
    #         levelCount = 1
    # elif levelCount == 2:
    #     if hp_bar_en == []:
    #         levelCount = 3
    #     elif hp_bar_pg == []:
    #         levelCount = 1
    # elif levelCount == 3:
    #     if hp_bar_en == []:
    #         levelCount = 1
    #     elif hp_bar_pg == []:
    #         levelCount = 1

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
                pass #game_intro()
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
            menuButton('button_back_black.png', 500, 355, 124, 56, action = None )#game_intro)
        
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
    #game_loop()

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
                message_to_screen("MATTARELLO USES DODGE", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES FIREOUT", BLACK, 485, 90)
                win.blit(pg_fire, (210, 70))
        
            elif blockCheck_EN == True:
                dodgeCheck_EN = False
                message_to_screen("MATTARELLO USES BLOCK", BLACK, 450, 60) 
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
            message_to_screen("MATTARELLO USES INCENDIO", BLACK, 450, 60)    
            
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
                message_to_screen("MATTARELLO USES INCENDIO", BLACK, 450, 90)
                win.blit(enemy2_fire, (250, 110))
        
            elif blockCheck_PG == True:
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("MATTARELLO USES INCENDIO", BLACK, 450, 90)
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
                message_to_screen("MATTARELLO USES DODGE", BLACK, 450, 60) 
                message_to_screen("LEGASOV USES KICK", BLACK, 470, 90)
                win.blit(pg_kick, (770, 110))
        
            elif blockCheck_EN == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_EN = False
                message_to_screen("MATTARELLO USES BLOCK", BLACK, 450, 60) 
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
            message_to_screen("MATTARELLO USES KICK", BLACK, 450, 60)    
            
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
                message_to_screen("MATTARELLO USES KICK", BLACK, 450, 90)
                win.blit(enemy2_hit, (200, 110))
        
            elif blockCheck_PG == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("MATTARELLO USES KICK", BLACK, 450, 90)
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
        print("MATTARELLO PUNCH")
        event_Fire()
    
    if move == 1:
        print("MATTARELLO KICK")
        event_Kick2()
    
    if move == 2:
        print("MATTARELLO DODGE")
        event_Dodge2()
        dodgeCheck_EN = True
    
    if move == 3:
        print("MATTARELLO BLOCK")
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
                message_to_screen("MATTARELLO USES KICK", BLACK, 450, 90)
                win.blit(enemy3_slash, (200, 110))
        
            elif blockCheck_PG == True:
                #BLOCKED -- BLOCCATO
                dodgeCheck_PG = False
                message_to_screen("LEGASOV USES BLOCK", BLACK, 460, 60)
                message_to_screen("MATTARELLO USES KICK", BLACK, 450, 90)
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
    message_to_screen("BRIGADIERE MATTARELLO", BLACK, 765, 10)
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


dialog_enemy_24 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy24.png"))
dialog_enemy_24 = pygame.transform.scale(dialog_enemy_24, (500, 150))  # ridimensionamento
dialog_enemy_25 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy25.png"))
dialog_enemy_25 = pygame.transform.scale(dialog_enemy_25, (500, 150))  # ridimensionamento
dialog_enemy_26 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy26.png"))
dialog_enemy_26 = pygame.transform.scale(dialog_enemy_26, (500, 150))  # ridimensionamento
dialog_enemy_27 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy27.png"))
dialog_enemy_27 = pygame.transform.scale(dialog_enemy_27, (500, 150))  # ridimensionamento
dialog_enemy_28 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy28.png"))
dialog_enemy_28 = pygame.transform.scale(dialog_enemy_28, (500, 150))  # ridimensionamento
dialog_enemy_29 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy29.png"))
dialog_enemy_29 = pygame.transform.scale(dialog_enemy_29, (500, 150))  # ridimensionamento
dialog_enemy_30 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy30.png"))
dialog_enemy_30 = pygame.transform.scale(dialog_enemy_30, (500, 150))  # ridimensionamento
dialog_enemy_31 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy31.png"))
dialog_enemy_31 = pygame.transform.scale(dialog_enemy_31, (500, 150))  # ridimensionamento
dialog_enemy_32 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy32.png"))
dialog_enemy_32 = pygame.transform.scale(dialog_enemy_32, (500, 150))  # ridimensionamento
dialog_enemy_33 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy33.png"))
dialog_enemy_33 = pygame.transform.scale(dialog_enemy_33, (500, 150))  # ridimensionamento
dialog_enemy_34 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy34.png"))
dialog_enemy_34 = pygame.transform.scale(dialog_enemy_34, (500, 150))  # ridimensionamento
dialog_enemy_35 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy35.png"))
dialog_enemy_35 = pygame.transform.scale(dialog_enemy_35, (500, 150))  # ridimensionamento
dialog_enemy_36 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy36.png"))
dialog_enemy_36 = pygame.transform.scale(dialog_enemy_36, (500, 150))  # ridimensionamento
dialog_enemy_37 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy37.png"))
dialog_enemy_37 = pygame.transform.scale(dialog_enemy_37, (500, 150))  # ridimensionamento
dialog_enemy_38 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy38.png"))
dialog_enemy_38 = pygame.transform.scale(dialog_enemy_38, (500, 150))  # ridimensionamento
dialog_enemy_39 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy39.png"))
dialog_enemy_39 = pygame.transform.scale(dialog_enemy_39, (500, 150))  # ridimensionamento
dialog_enemy_40 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy40.png"))
dialog_enemy_40 = pygame.transform.scale(dialog_enemy_40, (500, 150))  # ridimensionamento
dialog_enemy_41 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy41.png"))
dialog_enemy_41 = pygame.transform.scale(dialog_enemy_41, (500, 150))  # ridimensionamento
dialog_enemy_42 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy42.png"))
dialog_enemy_42 = pygame.transform.scale(dialog_enemy_42, (500, 150))  # ridimensionamento
dialog_enemy_43 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy43.png"))
dialog_enemy_43 = pygame.transform.scale(dialog_enemy_43, (500, 150))  # ridimensionamento
dialog_enemy_44 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy44.png"))
dialog_enemy_44 = pygame.transform.scale(dialog_enemy_44, (500, 150))  # ridimensionamento
dialog_enemy_45 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy45.png"))
dialog_enemy_45 = pygame.transform.scale(dialog_enemy_45, (500, 150))  # ridimensionamento


#global variables
moving_right = False
moving_left = False
moving_up = False
moving_down = False
n_livello = 1   #numero livello

#font2
font2 = pygame.font.SysFont("Comic Sans MS", 45)
font_icon = pygame.font.SysFont("Comic Sans MS", 20)

#color font2
yellow_font = (255, 255, 0)
black_font = (0,0,0)

#numero Step
nStep = 0

#position
player_location=[712,360]
player_location2 = [490, 550]
player_location3 = [308, 575]
player_location4 = [175, 500]
player_location5 = [264, 10]
player_location6 = [500, 220]
player_location7 = [9, 268]
player_location8 = [470, 300]

#check player location
player_locx = 0
player_locy = 0

#obiettivo
n_obiettivo = 0
obiettivo_check = False

#sound track
# first
pygame.mixer.pre_init()
pygame.mixer.music.load(os.path.join("Audio", "FirstTrack_1.ogg"))  # Get the first track from the playlist
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

def message_to_screen2(msg, color, font2):
    if nStep == 4:
        screen_text = font2.render(msg, True, color)
        screen.blit(screen_text, [350, 450])
    else:
        screen_text = font2.render(msg, True, color)
        screen.blit(screen_text, [200, 450])

def fade(width, height, nStep):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        if nStep == 1:
            message_to_screen2("Click Mouse Button to continue...", yellow_font, font2)
        elif nStep == 4:
            message_to_screen2("Secondo Capitolo", yellow_font, font2)

        pygame.time.delay(5)

def fade_obiettivo(width, height, n):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()

        if n <= 3:
            message_to_screen2("Obiettivo: perlustra il laboratorio", yellow_font, font2)

        if n == 4:
            message_to_screen2("Obiettivo: esci dal laboratorio", yellow_font, font2)

        pygame.time.delay(5)

def show_obiettivo(n):
    if n == 4:
        n_obiettivo = 4
        fade_obiettivo(1080,900, n_obiettivo)
    elif n <= 3:
        n_obiettivo = 3
        fade_obiettivo(1080,900, n_obiettivo)

def play_apple_sound(x):
    if x == "yes":
        pygame.mixer.fadeout(1)
        pygame.mixer.pause()
        pygame.mixer.music.load(os.path.join("Audio", "GetAppleSound.ogg"))  # Get the first track from the playlist
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song


def fade_decollo(width, height, screen, color):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        screen_text = font.render("Decollo", True, color)
        screen.blit(screen_text, [240, 300])


def fade_atterraggio(width, height, screen, color):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        screen_text = font.render("Atterraggio", True, color)
        screen.blit(screen_text, [165, 300])


show_apple1 = "yes";  show_apple2 = "yes"; show_apple3 = "yes"; show_apple4 = "yes";
n_apple = 0
n_apple1 = 0; n_apple2 = 0; n_apple3 = 0; n_apple4 = 0;
check_apple_sound = "none"
return_map_chef = 0
check_posx_salvini1 = 0
check_posx_salvini2 = 0
check_posx_chef1 = 0
check_posx_chef2 = 0
check_pos_spaceship = 0


n_image = 0 #salto scena
n_livello = 1 #salto livello
runGame = False

def SALVINI_FIGHT():
    global runGame, levelCount, turnCheck, turnNMB
    while runGame:
        if levelCount == 1:
            mainWindow(bg_lvl1)
            game_layout()
            pygame.time.wait(150)

            if hp_bar_en == []:
                #player_win()
                #pygame.time.wait(1500)
                #endScreen()
                turnCheck = True
                levelCount = 2
                runGame = False
                n_image = 15
                #return

            if hp_bar_pg == []:
                pygame.time.wait(1500)
                pygame.quit()
                sys.exit()
                # endScreen()
                # reset()
                # #game_intro()
                # levelCount = 1

            if turnCheck == True:
                gameButton(162, 534, 257, 59, event_Punch, turnCheck)
                gameButton(445, 534, 257, 59, event_Kick, turnCheck)
                gameButton(162, 616, 257, 59, event_Dodge, turnCheck)
                gameButton(445, 616, 257, 59, event_Block, turnCheck)
            else:
                turnNMB = 0
                pygame.time.wait(400)
            event_Enemy()


def CHEF_FIGHT():
    global runGame, levelCount, turnCheck, turnNMB
    if levelCount == 2:           
        mainWindow(bg_lvl2)
        game_layout2()
        pygame.time.wait(150)
        
        if hp_bar_en == []:
            #player_win()
            #pygame.time.wait(1500)
            #endScreen()
            turnCheck = True
            levelCount = 2
            runGame = False
            WINDOW_R1()
            n_image = 15

        if hp_bar_pg == []:
            pygame.time.wait(1500)
            pygame.quit()
            sys.exit()

        if turnCheck == True:
            gameButton(162, 534, 257, 59, event_Fire, turnCheck)
            gameButton(445, 534, 257, 59, event_Kick2, turnCheck)
            gameButton(162, 616, 257, 59, event_Dodge2, turnCheck)
            gameButton(445, 616, 257, 59, event_Block2, turnCheck)
        else:
            turnNMB = 0
            pygame.time.wait(400)
            event_Enemy2()


def APE_FIGHT():
    pass


def WINDOW_R1():
    global WINDOW_SIZE2, screen2, player_image2, bg_image2, salvini_image, draga_image, dialog_enemy_1, dialog_enemy_2, dialog_enemy_3, dialog_enemy_4
    global dialog_enemy_5, dialog_enemy_6, dialog_enemy_7, dialog_enemy_8, dialog_enemy_9, dialog_enemy_10
    WINDOW_SIZE2 = (688, 904)
    screen2 = pygame.display.set_mode(WINDOW_SIZE2, 0, 32)
    player_image2 = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
    player_image2 = pygame.transform.scale(player_image2, (25, 35))  # ridimensiono l'omino
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
    dialog_enemy_8 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy8.png"))
    dialog_enemy_8 = pygame.transform.scale(dialog_enemy_8, (500, 150))  # ridimensionamento
    dialog_enemy_9 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy9.png"))
    dialog_enemy_9 = pygame.transform.scale(dialog_enemy_9, (500, 150))  # ridimensionamento
    dialog_enemy_10 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy10.png"))
    dialog_enemy_10 = pygame.transform.scale(dialog_enemy_10, (500, 150))  # ridimensionamento
    #---
    screen2.blit(bg_image2, (0, 0))
    screen2.blit(player_image2, player_location2)
    #screen2.blit(money_image, (50, 50))
    screen2.blit(salvini_image, [370, 150])
    screen2.blit(text4, (90, 750))
    screen2.blit(draga_image, [340,80])
    pygame.mixer.fadeout(1)
    pygame.mixer.pause()
    pygame.mixer.music.load(os.path.join("Audio", "Poke.ogg"))  # Get the first track from the playlist
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song


def WINDOW_R2():
    global WINDOW_SIZE3, screen3, player_image3, bg_image3, dialog_enemy_11, dialog_enemy_12, dialog_enemy_13, dialog_enemy_14
    global dialog_enemy_15, dialog_enemy_16
    # Cap 3
    WINDOW_SIZE3 = (688, 620)
    screen3 = pygame.display.set_mode(WINDOW_SIZE3, 0, 32)
    player_image3 = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
    player_image3 = pygame.transform.scale(player_image3, (25, 35))  # ridimensiono l'omino
    bg_image3 = pygame.image.load(os.path.join("Immagini", "BgLevel3.png"))
    chef = pygame.image.load(os.path.join("Immagini", "chef.png"))
    chef = pygame.transform.scale(chef, (25, 35))  # ridimensiono lo chef
    #DialogoChef
    dialog_enemy_11 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy11.png"))
    dialog_enemy_11 = pygame.transform.scale(dialog_enemy_11, (500, 150))  # ridimensionamento
    dialog_enemy_12 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy12.png"))
    dialog_enemy_12 = pygame.transform.scale(dialog_enemy_12, (500, 150))  # ridimensionamento
    dialog_enemy_13 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy13.png"))
    dialog_enemy_13 = pygame.transform.scale(dialog_enemy_13, (500, 150))  # ridimensionamento
    dialog_enemy_14 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy14.png"))
    dialog_enemy_14 = pygame.transform.scale(dialog_enemy_14, (500, 150))  # ridimensionamento
    dialog_enemy_15 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy15.png"))
    dialog_enemy_15 = pygame.transform.scale(dialog_enemy_15, (500, 150))  # ridimensionamento
    dialog_enemy_16 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy16.png"))
    dialog_enemy_16 = pygame.transform.scale(dialog_enemy_16, (500, 150))  # ridimensionamento

    screen3.blit(bg_image3, (0, 0))
    screen3.blit(player_image3, player_location3)
    screen3.blit(chef, (420,110))   


while True:
    runGame = False
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
            player_image2 = pygame.transform.scale(player_image2, (25, 35))  # ridimensiono l'omino
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
            dialog_enemy_8 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy8.png"))
            dialog_enemy_8 = pygame.transform.scale(dialog_enemy_8, (500, 150))  # ridimensionamento
            dialog_enemy_9 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy9.png"))
            dialog_enemy_9 = pygame.transform.scale(dialog_enemy_9, (500, 150))  # ridimensionamento
            dialog_enemy_10 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy10.png"))
            dialog_enemy_10 = pygame.transform.scale(dialog_enemy_10, (500, 150))  # ridimensionamento
            #---
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            #screen2.blit(money_image, (50, 50))
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(text4, (90, 750))
            screen2.blit(draga_image, [340,80])
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "Poke.ogg"))  # Get the first track from the playlist
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

        # SALVINI FIGHT
        elif n_image == 14:
            runGame = True
            while runGame:
                if levelCount == 1:
                    mainWindow(bg_lvl1)
                    game_layout()
                    pygame.time.wait(150)

                    if hp_bar_en == []:
                        # player_win()
                        # pygame.time.wait(1500)
                        # endScreen()
                        turnCheck = True
                        levelCount = 2
                        runGame = False
                        n_image = 15
                        WINDOW_SIZE2 = (688, 904)
                        screen2 = pygame.display.set_mode(WINDOW_SIZE2, 0, 32)            
                        screen2.blit(bg_image2, (0, 0))
                        #return

                    if hp_bar_pg == []:
                        pygame.time.wait(1500)
                        pygame.quit()
                        sys.exit()
                        # endScreen()
                        # reset()
                        # #game_intro()
                        # levelCount = 1

                    if turnCheck == True:
                        gameButton(162, 534, 257, 59, event_Punch, turnCheck)
                        gameButton(445, 534, 257, 59, event_Kick, turnCheck)
                        gameButton(162, 616, 257, 59, event_Dodge, turnCheck)
                        gameButton(445, 616, 257, 59, event_Block, turnCheck)
                    else:
                        turnNMB = 0
                        pygame.time.wait(400)
                        event_Enemy()
            #SALVINI_FIGHT()

        elif n_image == 15:
            pygame.time.wait(350)
            # WINDOW_SIZE2 = (688, 904)
            # screen2 = pygame.display.set_mode(WINDOW_SIZE2, 0, 32)            
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            screen2.blit(salvini_image, [370, 150])
            screen2.blit(draga_image, [340, 80])
            screen2.blit(dialog_enemy_9, (90, 750))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "TpSound.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song


        elif n_image == 16:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            screen2.blit(dialog_enemy_8, (90, 750))


        elif n_image == 17:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)
            screen2.blit(dialog_enemy_10, (90, 750))

        elif n_image == 18:
            screen2.blit(bg_image2, (0, 0))
            screen2.blit(player_image2, player_location2)

        elif n_image == 19:
            # Cap 3
            WINDOW_SIZE3 = (688, 620)
            screen3 = pygame.display.set_mode(WINDOW_SIZE3, 0, 32)
            player_image3 = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
            player_image3 = pygame.transform.scale(player_image3, (25, 35))  # ridimensiono l'omino
            bg_image3 = pygame.image.load(os.path.join("Immagini", "BgLevel3.png"))
            chef = pygame.image.load(os.path.join("Immagini", "chef.png"))
            chef = pygame.transform.scale(chef, (25, 35))  # ridimensiono lo chef
            #DialogoChef
            dialog_enemy_11 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy11.png"))
            dialog_enemy_11 = pygame.transform.scale(dialog_enemy_11, (500, 150))  # ridimensionamento
            dialog_enemy_12 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy12.png"))
            dialog_enemy_12 = pygame.transform.scale(dialog_enemy_12, (500, 150))  # ridimensionamento
            dialog_enemy_13 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy13.png"))
            dialog_enemy_13 = pygame.transform.scale(dialog_enemy_13, (500, 150))  # ridimensionamento
            dialog_enemy_14 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy14.png"))
            dialog_enemy_14 = pygame.transform.scale(dialog_enemy_14, (500, 150))  # ridimensionamento
            dialog_enemy_15 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy15.png"))
            dialog_enemy_15 = pygame.transform.scale(dialog_enemy_15, (500, 150))  # ridimensionamento
            dialog_enemy_16 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy16.png"))
            dialog_enemy_16 = pygame.transform.scale(dialog_enemy_16, (500, 150))  # ridimensionamento

            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420,110))

        elif n_image == 20:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_11, (10, 450))

        elif n_image == 21:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_12, (10, 450))

        elif n_image == 22:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_13, (10, 450))

        elif n_image == 23:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_14, (10, 450))

        elif n_image == 24:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_15, (10, 450))

        elif n_image == 25:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_16, (10, 450))

        elif n_image == 26:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location3)
            screen3.blit(chef, (420, 110))

        elif n_image == 27:
            WINDOW_SIZE4 = (576, 544)
            screen_Apple1 = pygame.display.set_mode(WINDOW_SIZE4, 0, 32)
            bgApple1 = pygame.image.load(os.path.join("Immagini", "BgApple1.png"))
            Apple1 = pygame.image.load(os.path.join("Immagini", "Apple.png"))
            Apple1 = pygame.transform.scale(Apple1, (23, 19))
            Apple2 = pygame.image.load(os.path.join("Immagini", "Apple.png"))
            Apple2 = pygame.transform.scale(Apple2, (23, 19))

            screen_Apple1.blit(bgApple1, (0, 0))
            screen_Apple1.blit(player_image3, player_location4)
            if show_apple1 == "yes":
                screen_Apple1.blit(Apple1, (175, 400))
            if show_apple2 == "yes":
                screen_Apple1.blit(Apple2, (200, 350))

        elif n_image == 28:
            WINDOW_SIZEBack = (688, 620)
            screen3 = pygame.display.set_mode(WINDOW_SIZEBack, 0, 32)
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location5)
            screen3.blit(chef, (420, 110))

        elif n_image == 29:
            WINDOW_SIZE5 = (576, 544)
            screen_Apple2 = pygame.display.set_mode(WINDOW_SIZE5, 0, 32)
            bgApple2 = pygame.image.load(os.path.join("Immagini", "BgApple2New.png"))
            Apple3 = pygame.image.load(os.path.join("Immagini", "Apple.png"))
            Apple3 = pygame.transform.scale(Apple3, (23, 19))
            Apple4 = pygame.image.load(os.path.join("Immagini", "Apple.png"))
            Apple4 = pygame.transform.scale(Apple3, (23, 19))
            Shadow = pygame.image.load(os.path.join("Immagini", "Shadow.png"))
            Shadow = pygame.transform.scale(Shadow, (25, 35))

            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))

            if show_apple3 == "yes":
                screen_Apple2.blit(Apple3, (300, 240))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))

        elif n_image == 30:
            dialog_Shadow_1 = pygame.image.load(os.path.join("Immagini", "DialogoShadow1.png"))
            dialog_Shadow_1 = pygame.transform.scale(dialog_Shadow_1, (400, 125))  # ridimensionamento
            dialog_Shadow_2 = pygame.image.load(os.path.join("Immagini", "DialogoShadow2.png"))
            dialog_Shadow_2 = pygame.transform.scale(dialog_Shadow_2, (400, 125))  # ridimensionamento
            dialog_Shadow_3 = pygame.image.load(os.path.join("Immagini", "DialogoShadow3.png"))
            dialog_Shadow_3 = pygame.transform.scale(dialog_Shadow_3, (400, 125))  # ridimensionamento
            dialog_Shadow_4 = pygame.image.load(os.path.join("Immagini", "DialogoShadow4.png"))
            dialog_Shadow_4 = pygame.transform.scale(dialog_Shadow_4, (400, 125))  # ridimensionamento
            dialog_Shadow_5 = pygame.image.load(os.path.join("Immagini", "DialogoShadow5.png"))
            dialog_Shadow_5 = pygame.transform.scale(dialog_Shadow_5, (400, 125))  # ridimensionamento
            dialog_Shadow_6 = pygame.image.load(os.path.join("Immagini", "DialogoShadow6.png"))
            dialog_Shadow_6 = pygame.transform.scale(dialog_Shadow_6, (400, 125))  # ridimensionamento
            dialog_Shadow_7 = pygame.image.load(os.path.join("Immagini", "DialogoShadow7.png"))
            dialog_Shadow_7 = pygame.transform.scale(dialog_Shadow_7, (400, 125))  # ridimensionamento
            dialog_Shadow_8 = pygame.image.load(os.path.join("Immagini", "DialogoShadow8.png"))
            dialog_Shadow_8 = pygame.transform.scale(dialog_Shadow_8, (400, 125))  # ridimensionamento
            GotItem = pygame.image.load(os.path.join("Immagini", "GotItem.png"))
            GotItem = pygame.transform.scale(GotItem, (400, 125))  # ridimensionamento

            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_1,(90, 30))

        elif n_image == 31:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_2, (90, 30))

        elif n_image == 32:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_3, (90, 30))

        elif n_image == 33:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_3, (90, 30))

        elif n_image == 34:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_4, (90, 30))

        elif n_image == 35:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_5, (90, 30))

        elif n_image == 36:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_6, (90, 30))

        elif n_image == 37:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_7, (90, 30))

        elif n_image == 38:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(dialog_Shadow_8, (90, 30))
                pygame.mixer.fadeout(1)
                pygame.mixer.pause()
                pygame.mixer.music.load(os.path.join("Audio", "GotItem.ogg"))  # Get the first track from the playlist
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song


        elif n_image == 39:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))
                screen_Apple2.blit(GotItem, (90, 30))

        elif n_image == 40:
            screen_Apple2.blit(bgApple2, (0, 0))
            screen_Apple2.blit(player_image3, player_location6)
            screen_Apple2.blit(Shadow, (270, 390))
            if show_apple4 == "yes":
                screen_Apple2.blit(Apple4, (305, 430))

        elif n_image == 41:
            WINDOW_SIZEBack1 = (688, 620)
            screen3 = pygame.display.set_mode(WINDOW_SIZEBack1, 0, 32)
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))

        elif n_image == 42:
            # DialogoChef
            dialog_enemy_17 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy17.png"))
            dialog_enemy_17 = pygame.transform.scale(dialog_enemy_17, (500, 150))  # ridimensionamento
            dialog_enemy_18 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy18.png"))
            dialog_enemy_18 = pygame.transform.scale(dialog_enemy_18, (500, 150))  # ridimensionamento
            dialog_enemy_19 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy19.png"))
            dialog_enemy_19 = pygame.transform.scale(dialog_enemy_19, (500, 150))  # ridimensionamento
            dialog_enemy_20 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy20.png"))
            dialog_enemy_20 = pygame.transform.scale(dialog_enemy_20, (500, 150))  # ridimensionamento
            dialog_enemy_21 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy21.png"))
            dialog_enemy_21 = pygame.transform.scale(dialog_enemy_21, (500, 150))  # ridimensionamento
            dialog_enemy_22 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy22.png"))
            dialog_enemy_22 = pygame.transform.scale(dialog_enemy_22, (500, 150))  # ridimensionamento
            dialog_enemy_23 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy23.png"))
            dialog_enemy_23 = pygame.transform.scale(dialog_enemy_23, (500, 150))  # ridimensionamento

            WINDOW_SIZEBack2 = (688, 620)
            screen3 = pygame.display.set_mode(WINDOW_SIZEBack2, 0, 32)
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_18, (10, 450))

        elif n_image == 43:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_19, (10, 450))

        elif n_image == 44:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_20, (10, 450))

        elif n_image == 45:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_21, (10, 450))

        elif n_image == 46:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_22, (10, 450))

        elif n_image == 47:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_23, (10, 450))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "StartFight.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song

        #CHEF FIGHT
        elif n_image == 48:
            reset()
            runGame = True
            levelCount = 2
            while runGame:
                n_image = 49                
                if levelCount == 2:           
                    mainWindow(bg_lvl2)
                    game_layout2()
                    pygame.time.wait(150)
                    
                    if hp_bar_en == []:
                        #player_win()
                        #pygame.time.wait(1500)
                        #endScreen()
                        turnCheck = True
                        levelCount = 3
                        runGame = False
                        WINDOW_SIZEBack2 = (688, 620)
                        screen3 = pygame.display.set_mode(WINDOW_SIZEBack2, 0, 32)
                        screen3.blit(bg_image3, (0, 0))                        
                        #WINDOW_R2()
                        n_image = 49

                    if hp_bar_pg == []:
                        pygame.time.wait(1500)
                        pygame.quit()
                        sys.exit()

                    if turnCheck == True:
                        gameButton(162, 534, 257, 59, event_Fire, turnCheck)
                        gameButton(445, 534, 257, 59, event_Kick2, turnCheck)
                        gameButton(162, 616, 257, 59, event_Dodge2, turnCheck)
                        gameButton(445, 616, 257, 59, event_Block2, turnCheck)
                    else:
                        turnNMB = 0
                        pygame.time.wait(400)
                        event_Enemy2()
            
            pygame.time.wait(500)
            n_image = 49
            print(n_image) # = 49
            pygame.time.wait(500)

        elif n_image == 49:
            #DialogoChef
            n_image = 49
            WINDOW_SIZE3 = (688, 620)
            screen3 = pygame.display.set_mode(WINDOW_SIZE3, 0, 32)
            dialog_enemy_24 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy24.png"))
            dialog_enemy_24 = pygame.transform.scale(dialog_enemy_24, (500, 150))  # ridimensionamento
            dialog_enemy_25 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy25.png"))
            dialog_enemy_25 = pygame.transform.scale(dialog_enemy_25, (500, 150))  # ridimensionamento
            dialog_enemy_26 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy26.png"))
            dialog_enemy_26 = pygame.transform.scale(dialog_enemy_26, (500, 150))  # ridimensionamento
            dialog_enemy_27 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy27.png"))
            dialog_enemy_27 = pygame.transform.scale(dialog_enemy_27, (500, 150))  # ridimensionamento
            dialog_enemy_28 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy28.png"))
            dialog_enemy_28 = pygame.transform.scale(dialog_enemy_28, (500, 150))  # ridimensionamento
            dialog_enemy_29 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy29.png"))
            dialog_enemy_29 = pygame.transform.scale(dialog_enemy_29, (500, 150))  # ridimensionamento
            dialog_enemy_30 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy30.png"))
            dialog_enemy_30 = pygame.transform.scale(dialog_enemy_30, (500, 150))  # ridimensionamento
            dialog_enemy_31 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy31.png"))
            dialog_enemy_31 = pygame.transform.scale(dialog_enemy_31, (500, 150))  # ridimensionamento
            dialog_enemy_32 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy32.png"))
            dialog_enemy_32 = pygame.transform.scale(dialog_enemy_32, (500, 150))  # ridimensionamento
            dialog_enemy_33 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy33.png"))
            dialog_enemy_33 = pygame.transform.scale(dialog_enemy_33, (500, 150))  # ridimensionamento
            dialog_enemy_34 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy34.png"))
            dialog_enemy_34 = pygame.transform.scale(dialog_enemy_34, (500, 150))  # ridimensionamento
            dialog_enemy_35 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy35.png"))
            dialog_enemy_35 = pygame.transform.scale(dialog_enemy_35, (500, 150))  # ridimensionamento
            dialog_enemy_36 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy36.png"))
            dialog_enemy_36 = pygame.transform.scale(dialog_enemy_36, (500, 150))  # ridimensionamento
            dialog_enemy_37 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy37.png"))
            dialog_enemy_37 = pygame.transform.scale(dialog_enemy_37, (500, 150))  # ridimensionamento
            dialog_enemy_38 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy38.png"))
            dialog_enemy_38 = pygame.transform.scale(dialog_enemy_38, (500, 150))  # ridimensionamento
            dialog_enemy_39 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy39.png"))
            dialog_enemy_39 = pygame.transform.scale(dialog_enemy_39, (500, 150))  # ridimensionamento
            dialog_enemy_40 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy40.png"))
            dialog_enemy_40 = pygame.transform.scale(dialog_enemy_40, (500, 150))  # ridimensionamento
            dialog_enemy_41 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy41.png"))
            dialog_enemy_41 = pygame.transform.scale(dialog_enemy_41, (500, 150))  # ridimensionamento
            dialog_enemy_42 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy42.png"))
            dialog_enemy_42 = pygame.transform.scale(dialog_enemy_42, (500, 150))  # ridimensionamento
            dialog_enemy_43 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy43.png"))
            dialog_enemy_43 = pygame.transform.scale(dialog_enemy_43, (500, 150))  # ridimensionamento
            dialog_enemy_44 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy44.png"))
            dialog_enemy_44 = pygame.transform.scale(dialog_enemy_44, (500, 150))  # ridimensionamento
            dialog_enemy_45 = pygame.image.load(os.path.join("Immagini", "DialogoEnemy45.png"))
            dialog_enemy_45 = pygame.transform.scale(dialog_enemy_45, (500, 150))  # ridimensionamento

            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_24, (10, 450))
            pygame.time.wait(500)
            n_image = 50

        elif n_image == 50:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_25, (10, 450))

        elif n_image == 51:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_26, (10, 450))

        elif n_image == 52:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_27, (10, 450))

        elif n_image == 53:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_28, (10, 450))

        elif n_image == 54:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_29, (10, 450))

        elif n_image == 55:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_30, (10, 450))

        elif n_image == 56:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_31, (10, 450))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "PunchSound.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song

        elif n_image == 57:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_32, (10, 450))

        elif n_image == 58:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_33, (10, 450))

        elif n_image == 59:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_34, (10, 450))

        elif n_image == 60:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_35, (10, 450))

        elif n_image == 61:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_36, (10, 450))

        elif n_image == 62:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_37, (10, 450))

        elif n_image == 63:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_38, (10, 450))

        elif n_image == 64:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_39, (10, 450))

        elif n_image == 65:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_40, (10, 450))

        elif n_image == 66:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_41, (10, 450))

        elif n_image == 67:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_42, (10, 450))

        elif n_image == 68:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_43, (10, 450))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "EatingSound.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song

        elif n_image == 69:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_44, (10, 450))

        elif n_image == 70:
            screen3.blit(bg_image3, (0, 0))
            screen3.blit(player_image3, player_location7)
            screen3.blit(chef, (420, 110))
            screen3.blit(dialog_enemy_45, (10, 450))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "TpSound.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song
            n_livello = 4

        elif n_image == 71:
            WINDOW_SIZEB6 = (640, 640)
            screen4 = pygame.display.set_mode(WINDOW_SIZEB6, 0, 32)
            spaceshipK = pygame.image.load(os.path.join("Immagini/ImmaginiSpaceWar", "ship.png"))
            spaceshipK = pygame.transform.scale(spaceshipK, (25, 35))  # ridimensionamento
            player_image4 = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
            player_image4 = pygame.transform.scale(player_image4, (25, 35))  # ridimensiono l'omino
            bg_image4 = pygame.image.load(os.path.join("Immagini", "BgAereoSpace.png"))
            dialogo_space1 = pygame.image.load(os.path.join("Immagini", "DialogoSpace1.png"))
            dialogo_space1 = pygame.transform.scale(dialogo_space1, (500, 150))  # ridimensionamento
            dialogo_space2 = pygame.image.load(os.path.join("Immagini", "DialogoSpace2.png"))
            dialogo_space2 = pygame.transform.scale(dialogo_space2, (500, 150))  # ridimensionamento
            dialogo_space3 = pygame.image.load(os.path.join("Immagini", "DialogoSpace3.png"))
            dialogo_space3 = pygame.transform.scale(dialogo_space3, (500, 150))  # ridimensionamento
            dialogo_space4 = pygame.image.load(os.path.join("Immagini", "DialogoSpace4.png"))
            dialogo_space4 = pygame.transform.scale(dialogo_space4, (500, 150))  # ridimensionamento

            screen4.blit(bg_image4, (0, 0))
            screen4.blit(player_image4, player_location8)
            screen4.blit(player_image4, player_location8)
            screen4.blit(spaceshipK, (410, 70))
            screen4.blit(dialogo_space1, (10, 450))

        elif n_image == 72:
            screen4.blit(bg_image4, (0, 0))
            screen4.blit(player_image4, player_location8)
            screen4.blit(player_image4, player_location8)
            screen4.blit(spaceshipK, (410, 70))

        elif n_image == 73:
            screen4.blit(bg_image4, (0, 0))
            screen4.blit(player_image4, player_location8)
            screen4.blit(player_image4, player_location8)
            screen4.blit(spaceshipK, (410, 70))

        elif n_image == 74:
            screen4.blit(bg_image4, (0, 0))
            screen4.blit(player_image4, player_location8)
            screen4.blit(player_image4, player_location8)
            screen4.blit(spaceshipK, (410, 70))

        #decollo map
        elif n_image == 75:
            screen4.blit(bg_image4, (0, 0))
            screen4.blit(player_image4, player_location8)
            screen4.blit(player_image4, player_location8)
            screen4.blit(spaceshipK, (410, 70))
            screen4.blit(dialogo_space2, (10, 450))
            pygame.mixer.fadeout(1)
            pygame.mixer.pause()
            pygame.mixer.music.load(os.path.join("Audio", "TakeOffS.ogg"))  # Get the first track from the playlist
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)  # Setting the volume of the song

        # decollo map
        elif n_image == 76:
            fade_decollo(640, 640, screen4, yellow_font)

        elif n_image == 77:
            WINDOW_SIZES1 = (1280, 720)
            player_location9 = [565, 500]
            screen5 = pygame.display.set_mode(WINDOW_SIZES1, 0, 32)
            bg_nave = pygame.image.load(os.path.join("Immagini", "SpaceComando1.png"))
            player_image5 = pygame.image.load(os.path.join("Immagini", "Kovalski.png"))
            player_image5 = pygame.transform.scale(player_image4, (150, 175))  # ridimensiono l'omino
            screen5.blit(bg_nave, (0, 0))
            screen5.blit(player_image5, player_location9)

        elif n_image == 78:
            screen5.blit(bg_nave, (0, 0))
            screen5.blit(player_image5, player_location9)
            screen5.blit(dialogo_space3, (10, 500))

        elif n_image == 79:
            bg_nave2 = pygame.image.load(os.path.join("Immagini", "SpaceComando2.png"))
            screen5.blit(bg_nave2, (0, 0))
            screen5.blit(player_image5, player_location9)
            screen5.blit(dialogo_space4, (10, 500))

        elif n_image == 80:
            counter_destroy = 0
            pygame.init()  # inizializzo pygame
            pygame.display.set_caption('Ape Ops Arcade')
            WINDOW_SIZE5 = (600, 800)
            count = 0

            def draw_ready(text, fontready, text_col, x, y):
                img = fontready.render(text, True, text_col)
                screen.blit(img, (x, y))


            class Spaceship(pygame.sprite.Sprite):
                def __init__(self, x, y):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = ship
                    self.rect = self.image.get_rect()
                    self.rect.center = [x, y]
                    self.last_shot = pygame.time.get_ticks()
                    self.health = 120

                def update(self):

                    # movements
                    speed = 10

                    # cooldown
                    cooldown = 300

                    key = pygame.key.get_pressed()
                    if self.health > 0:
                        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.left > 0:
                            self.rect.x -= speed
                        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.right < 600:
                            self.rect.x += speed



                        if event.type == pygame.JOYBUTTONDOWN:
                            if event.button == button_keys['left_arrow'] and self.rect.left > 0:
                                self.rect.x -= speed
                            if event.button == button_keys['right_arrow'] and self.rect.right < 600:
                                self.rect.x += speed



                        time_now = pygame.time.get_ticks()

                        # shoot
                        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
                            bullet = Bullets(self.rect.centerx, self.rect.top)
                            bullet_group.add(bullet)
                            self.last_shot = time_now

                    # getter method
                    if self.health <= 0:
                        explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
                        explosion_group.add(explosion)

                def get_health(self):
                    return self.health


            class Bullets(pygame.sprite.Sprite):
                def __init__(self, x, y):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = bullet
                    self.rect = self.image.get_rect()
                    self.rect.center = [x, y]
                    self.count = 0

                def update(self):
                    self.rect.y -= 10
                    if self.rect.bottom < 100:
                        self.kill()

                    if pygame.sprite.spritecollide(self, enemy_group, True):
                        self.kill()
                        explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
                        explosion_group.add(explosion)
                        global count
                        count +=1

                def get_counter(self):
                    return self.count

            class Enemies(pygame.sprite.Sprite):
                def __init__(self, x, y):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load("Immagini/ImmaginiSpaceWar/Enemy" + str(random.randint(1, 3)) + ".png")
                    self.rect = self.image.get_rect()
                    self.rect.center = [x, y]
                    self.move_counter = 0
                    self.move_direction = 1

                def update(self):
                    self.rect.x += self.move_direction
                    self.move_counter += 1
                    if abs(self.move_counter) > 75:
                        self.move_direction *= -1
                        self.move_counter *= self.move_direction


            class Enemies_Bullets(pygame.sprite.Sprite):
                def __init__(self, x, y):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = bulletEn
                    self.rect = self.image.get_rect()
                    self.rect.center = [x, y]

                def update(self):
                    self.rect.y += 10
                    if self.rect.top > 800:
                        self.kill()

                    if pygame.sprite.spritecollide(self, space_ship_group, False):
                        spaceship.health -= 5
                        # return spaceship.health
                        print(spaceship.health)
                        explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
                        explosion_group.add(explosion)


            def create_enemies():
                for row in range(5):
                    for item in range(5):
                        enemy = Enemies(100 + item * 100, 100 + row * 70)
                        enemy_group.add(enemy)


            class Explosion(pygame.sprite.Sprite):
                def __init__(self, x, y, size):
                    pygame.sprite.Sprite.__init__(self)
                    self.images = []
                    for n in range(1, 6):
                        img = pygame.image.load("Immagini/ImmaginiSpaceWar/exp" + str(n) + ".png")
                        if size == 1:
                            img = pygame.transform.scale(img, (30, 30))
                        if size == 2:
                            img = pygame.transform.scale(img, (50, 50))
                        if size == 3:
                            img = pygame.transform.scale(img, (200, 200))
                        self.images.append(img)



                    self.index = 0
                    self.image = self.images[self.index]
                    self.rect = self.image.get_rect()
                    self.rect.center = [x, y]
                    self.counter = 0


                # aggiornare l'esplosione
                def update(self):
                    explosion_speed = 3
                    self.counter += 1

                    if self.counter >= explosion_speed and self.index < len(self.images) - 1:
                        self.counter = 0
                        print(self.counter)
                        self.index += 1
                        self.image = self.images[self.index]

                    if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                        self.kill()



            # hp
            bg_space = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "spacee.png")))
            hp_space1 = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "hp_space.png")))
            hp_space2 = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "hp_space.png")))
            hp_space3 = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "hp_space.png")))
            hp_half_hearth1 = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "hp_half_hearth.png")))

            # spaceship
            ship = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "ship.png")))

            # bullet
            bullet = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "bullet_ship.png")))
            bullet = pygame.transform.scale(bullet, (20, 20))
            screen = pygame.display.set_mode(WINDOW_SIZE5, 0, 32)  # finestra di gioco

            bulletEn = pygame.image.load((os.path.join("Immagini/ImmaginiSpaceWar", "bullet.png")))
            bulletEn = pygame.transform.scale(bulletEn, (20, 20))
            bulletEn = pygame.transform.flip(bulletEn, False, True)

            # fontsa
            fontready1 = pygame.font.SysFont('Costantia', 50)
            fontready2 = pygame.font.SysFont('Costantia', 40)

            # color fonts
            white = (255, 255, 255)

            # countdown start
            countdown_start = 3
            last_countdown_start = pygame.time.get_ticks()

            # spaceship
            spaceship = Spaceship(300, 700)

            # --Sprites--

            # spaceship sprites
            space_ship_group = pygame.sprite.Group()
            space_ship_group.add(spaceship)
            # bullets sprites
            bullet_group = pygame.sprite.Group()
            # enemy sprites
            enemy_group = pygame.sprite.Group()
            enemy_bullets_group = pygame.sprite.Group()
            # explosion sprites
            explosion_group = pygame.sprite.Group()

            # enemy
            enemy_colldown = 1000
            last_enemy_shot = pygame.time.get_ticks()
            create_enemies()

            exit = 0
            while True:
                if count == 25 and nhealth >0:
                    n_image = 81
                    break
                #print(count)

                if exit == 0:
                    screen.blit(bg_space, [0, 0])
                    nhealth = spaceship.get_health()

                    if nhealth == 120:
                        screen.blit(hp_space1, [10, 10])
                        screen.blit(hp_space2, [70, 10])
                        screen.blit(hp_space3, [130, 10])

                    elif nhealth > 80 and nhealth < 120:
                        screen.blit(hp_space1, [10, 10])
                        screen.blit(hp_space2, [70, 10])
                        screen.blit(hp_half_hearth1, [130, 10])

                    elif nhealth == 80:
                        screen.blit(hp_space1, [10, 10])
                        screen.blit(hp_space2, [70, 10])


                    elif nhealth > 40 and nhealth < 80:
                        screen.blit(hp_space1, [10, 10])
                        screen.blit(hp_half_hearth1, [70, 10])

                    elif nhealth == 40:
                        screen.blit(hp_space1, [10, 10])

                    elif nhealth > 0 and nhealth < 40:
                        screen.blit(hp_half_hearth1, [10, 10])

                    elif nhealth <= 0:
                        exit = 1

                    if countdown_start == 0:
                        # random bullets (enemies)
                        time_now = pygame.time.get_ticks()
                        if time_now - last_enemy_shot > enemy_colldown and len(enemy_bullets_group) < 5 and len(
                                enemy_group) > 0:
                            attack_enemy = random.choice(enemy_group.sprites())
                            enemy_bullet = Enemies_Bullets(attack_enemy.rect.centerx, attack_enemy.rect.bottom)
                            enemy_bullets_group.add(enemy_bullet)
                            last_enemy_shot = time_now

                        # sprites update
                        spaceship.update()
                        bullet_group.update()
                        enemy_group.update()
                        enemy_bullets_group.update()

                    # countdown
                    if countdown_start > 0:
                        draw_ready('GET READY!', fontready1, white, 190, 400 + 50)
                        draw_ready(str(countdown_start), fontready2, white, 300 - 10, 400 + 100)
                        timer = pygame.time.get_ticks()
                        if timer - last_countdown_start > 1000:
                            countdown_start -= 1
                            last_countdown_start = timer

                    explosion_group.update()

                    # draw sprites
                    space_ship_group.draw(screen)
                    bullet_group.draw(screen)
                    enemy_group.draw(screen)
                    enemy_bullets_group.draw(screen)
                    explosion_group.draw(screen)

                    print("vita: " + str(nhealth))

                else:
                    n_image = 82
                    break
                    #print("you lost")
                    #DEVE RICOMINCIARE DA CAPO IL GIOCO


                for event in pygame.event.get():

                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                clock.tick(60) #da i
            #esercito

        elif n_image == 81:
            print("I WON")
            fade_atterraggio(600, 800, screen, yellow_font)
            # METTI QUI IL FIGHT CON IL GORILLA
            n_image = 83

        elif n_image == 82:
            #SONO UN PERDENTE
            print("Sono un perdente")
            pygame.quit()
            sys.exit()
            #MENU

        elif n_image == 83:
            #print("ho vinto")
            reset()
            runGame = True
            levelCount = 3
            while runGame:
                if levelCount == 3:        
                    mainWindow(bg_lvl3)
                    game_layout3()
                    pygame.time.wait(150)
                    
                    if hp_bar_en == []:
                        #player_win()
                        #pygame.time.wait(1500)
                        #endScreen()
                        turnCheck = True
                        levelCount = 3
                        runGame = False
                        pygame.quit()
                        sys.exit()

                    if hp_bar_pg == []:
                        pygame.time.wait(1500)
                        pygame.quit()
                        sys.exit()

                    if turnCheck == True:
                        gameButton(162, 534, 257, 59, event_Fire2, turnCheck)
                        gameButton(445, 534, 257, 59, event_Slash, turnCheck)
                        gameButton(162, 616, 257, 59, event_Dodge3, turnCheck)
                        gameButton(445, 616, 257, 59, event_Block3, turnCheck)
                    else:
                        turnNMB = 0
                        pygame.time.wait(400)
                        event_Enemy3()


    # movements
    if n_livello == 1:
        if moving_right == True:
            if n_image <= 3:
                if player_location[0] > 888 and player_location[1] > 330:
                    print("I can't go here")
                else:
                    player_location[0] += 4
                    player_locx = player_location[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
            else:
                player_location[0] += 4
                player_locx = player_location[0]
                print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        if moving_left == True:
            if player_location[0] < 120 and player_location[1] > 330:
                print("I can't go here")
            else:
                player_location[0] -= 4
                player_locx = player_location[0]
                print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))


    elif n_livello == 2:
        #print("Livello: " + str(n_livello))
        if n_image != 5 and n_image != 18 and n_image != 14 and n_image != 15 and n_image != 16 and n_image!= 17:
            if n_image < 7 or n_image > 13:
                if moving_right == True:
                    if (check_posx_salvini1 == 0):
                        if n_image == 6:
                            if (player_location2[0] >= 490):
                                print("I can't go here...")
                            else:
                                player_location2[0] += 3
                                player_locx = player_location2[0]
                                print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                                if n_image == 6:
                                    if (player_location2[0] >= 328 or player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                                        n_image = 7

                if moving_left == True:
                    if n_image == 6:
                        if (player_location2[0] <= 328):
                            print("I can't go here...")
                            check_posx_salvini1 = 1
                        else:
                            player_location2[0] -= 3
                            player_locx = player_location2[0]
                            print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                            if n_image == 6:
                                if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                                    n_image = 7

                if moving_up == True:
                    print(check_posx_salvini1)
                    if (check_posx_salvini1 == 1):
                        player_location2[1] -= 3
                        player_locy = player_location2[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                        if n_image == 6:
                            if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                                n_image = 7
                    else:
                        print("I can't go here...")

                if moving_down == True:

                    if (player_location2[0] >= 328) and (player_location2[1] >= 390 and player_location2[1] >= 550):
                        print("I can't go here...")
                    else:
                        player_location2[1] += 3
                        player_locy = player_location2[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                        if n_image == 6:
                            if (player_location2[0] >= 328 and player_location2[0] <= 412) and (player_location2[1] >= 148 and player_location2[1] <= 196):
                                n_image = 7

        elif n_image == 18:
            if moving_right == True:
                if(player_location2[0] >= 370):
                    check_posx_salvini2 = 1
                else:
                    player_location2[0] += 3
                    player_locx = player_location2[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if (player_location2[0] >= 343 and player_location2[0] <= 395) and (player_location2[1] <= -5):
                        n_image = 19
                        n_livello = 3
                        print(n_livello)

            if moving_up == True:
                if check_posx_salvini2 == 1:
                    player_location2[1] -= 3
                    player_locx = player_location2[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if (player_location2[0] >= 343 and player_location2[0] <= 395) and (player_location2[1] <= -5):
                        n_image = 19
                        n_livello = 3
                        print(n_livello)



    elif n_livello == 3:
        if  n_image == 19:
            if moving_right == True:
                if check_posx_chef1 == 1:
                    player_location3[0] += 4
                    player_locx = player_location3[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                elif check_posx_chef1 == 4:
                    if player_location3[0] >= 380:
                        check_posx_chef1 = 5
                        print("Dialogo con chef...")
                        n_image = 20
                    else:
                        player_location3[0] += 4
                        player_locx = player_location3[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                else:
                    print("I can't go here...")

            if moving_left == True:
                if check_posx_chef1 == 2:
                    if player_location3[0] == 264:
                        print("I can't go here...")
                        check_posx_chef1 = 3
                    else:
                        player_location3[0] -= 4
                        player_locx = player_location3[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                else:
                    print("I can't go here...")

            if moving_up == True:
                if check_posx_chef1 == 0:
                    player_location3[1] -= 4
                    player_locy = player_location3[1]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    if (player_location3[0] == 308 and player_location3[1] == 507):
                        check_posx_chef1 = 2
                elif check_posx_chef1 == 3:
                    if player_location3[1] <= 90:
                        print("I can't go here...")
                        check_posx_chef1 = 4
                    else:
                        player_location3[1] -= 4
                        player_locy = player_location3[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                else:
                    print("I can't go here...")

        elif n_image == 26:
                if moving_left == True:
                    if check_posx_chef1 == 5:
                        if player_location3[0] <= 264:
                            print("I can't go here...")
                            check_posx_chef1 = 6
                        else:
                            player_location3[0] -= 3
                            player_locx = player_location3[0]
                            print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                    else:
                        print("I can't go here...")

                if moving_up == True:
                    if check_posx_chef1 == 6:
                        player_location3[1] -= 3
                        player_locy = player_location3[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                        if (player_location3[1] <= 3):
                            check_posx_chef1 = 7
                            n_image = 27

                    else:
                        print("I can't go here...")

        elif n_image == 27:
            if moving_right == True:
                if check_posx_chef1 == 8:
                    if player_location4[0] >= 202:
                        print("I can't go here...")
                        check_posx_chef1 = 9
                    else:
                        player_location4[0] += 3
                        player_locx = player_location4[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))


            if moving_left == True:
                if check_posx_chef1 == 11:
                    if player_location4[0] == 190:
                        print("I can't go here...")
                        check_posx_chef1 =12
                    else:
                        player_location4[0] -= 3
                        player_locx = player_location4[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))


            if moving_up == True:
                if check_posx_chef1 == 7:
                    if player_location4[1] <=394:
                        print("I can't go here...")
                    else:
                        player_location4[1] -= 3
                        player_locy = player_location4[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                        if n_apple1 == 0:
                            if (player_location4[0] >= 173) and (player_location4[0] <= 181) and (player_location4[1] >= 347) and (player_location4[1] <= 394):
                                show_apple1 = "none"
                                check_apple_sound = "yes"
                                n_apple1 = 1
                                play_apple_sound(check_apple_sound)
                                n_apple += 1
                                check_posx_chef1 = 8

                        elif n_apple2 == 0:
                            if (player_location4[0] >= 191) and (player_location4[0] <= 211) and (player_location4[1] >= 322) and (player_location4[1] <= 342):
                                show_apple2 = "none"
                                check_apple_sound = "yes"
                                n_apple2 = 1
                                play_apple_sound(check_apple_sound)
                                n_apple += 1

                elif check_posx_chef1 == 9:
                    if player_location4[1] <=342:
                        print("I can't go here...")
                    else:
                        player_location4[1] -= 3
                        player_locy = player_location4[1]
                        if n_apple2 == 0:
                            if (player_location4[0] >= 191) and (player_location4[0] <= 211) and (player_location4[1] >= 322) and (player_location4[1] <= 342):
                                show_apple2 = "none"
                                check_apple_sound = "yes"
                                n_apple2 = 1
                                play_apple_sound(check_apple_sound)
                                n_apple += 1
                                check_posx_chef1 = 10

                else:
                    print("I can't go here...")


            if moving_down == True:
                if check_posx_chef1 == 10:
                    if player_location4[1] == 431:
                        print("I can't go here...")
                        check_posx_chef1 = 11
                    else:
                        player_location4[1] += 3
                        player_locy = player_location4[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
                elif check_posx_chef1 == 12:
                    if player_location4[1] == 500:
                        print("I can't go here...")
                        n_image = 28
                        check_posx_chef1 = 13
                    else:
                        player_location4[1] += 3
                        player_locy = player_location4[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        elif n_image == 28:
            if moving_down == True:
                if check_posx_chef1 == 13:
                    if player_location5[1] >= 267:
                        print("I can't go here...")
                        check_posx_chef1 = 14
                    else:
                        player_location5[1] += 3
                        player_locy = player_location5[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))
            if moving_left == True:
                if check_posx_chef1 == 14:
                    if player_location5[0] <= 0:
                        print("I can't go here...")
                        check_posx_chef1 =15
                        n_image = 29
                    else:
                        player_location5[0] -= 3
                        player_locx = player_location5[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        elif n_image == 29:
            if moving_down == True:
                if check_posx_chef1 == 16:
                    if player_location6[1] >= 390:
                        n_image = 30
                        check_posx_chef1 = 17
                    else:
                        player_location6[1] += 3
                        player_locy = player_location6[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

            if moving_left == True:
                if check_posx_chef1 == 15:
                    if player_location6[0] <= 305:
                        print("I can't go here...")
                        if n_apple3 == 0:
                            show_apple3 = "none"
                            check_apple_sound = "yes"
                            n_apple3 = 1
                            play_apple_sound(check_apple_sound)
                            n_apple += 1
                            check_posx_chef1 = 16
                    else:
                        player_location6[0] -= 3
                        player_locx = player_location6[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        elif n_image == 40:
            if moving_down == True:
                if check_posx_chef1 == 17:
                    if player_location6[1] >= 430:
                        print("I can't go here...")
                    else:
                        player_location6[1] += 3
                        player_locy = player_location6[1]
                        if n_apple4 == 0:
                            if (player_location6[1] == 400):
                                show_apple4 = "none"
                                check_apple_sound = "yes"
                                n_apple4 = 1
                                play_apple_sound(check_apple_sound)
                                n_apple += 1
                                check_posx_chef1 = 18
            if moving_up == True:
                if check_posx_chef1 == 18:
                    if player_location6[1] <= 218:
                        check_posx_chef1 = 19
                        print("I can't go here...")
                    else:
                        player_location6[1] -= 3
                        player_locy = player_location6[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

            if moving_right == True:
                if check_posx_chef1 == 19:
                    if player_location6[0] >= 550:
                        check_posx_chef1 = 20
                        n_image = 41
                        print("I can't go here...")
                    else:
                        player_location6[0] += 3
                        player_locy = player_location6[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        elif n_image == 41:
            if moving_right == True:
                if check_posx_chef1 == 20:
                    if player_location7[0] >= 264:
                        check_posx_chef1 = 21
                        print("I can't go here...")
                    else:
                        player_location7[0] += 3
                        player_locy = player_location7[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

            if moving_up == True:
                if check_posx_chef1 == 21:
                    if player_location7[1] <= 87:
                        check_posx_chef1 = 22
                        print("I can't go here...")
                    else:
                        player_location7[1] -= 3
                        player_locy = player_location7[1]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

            if moving_right == True:
                if check_posx_chef1 == 22:
                    if player_location7[0] >= 380:
                        n_image = 42
                        print("Dialogo con Chef")
                    else:
                        player_location7[0] += 3
                        player_locy = player_location7[0]
                        print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))


    elif n_livello == 4:
        if n_image == 72:
            if moving_up == True:
                if player_location8[1] <= 148:
                    n_image = 73
                    print("I can't go here...")
                else:
                    player_location8[1] -= 3
                    player_locy = player_location8[1]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        elif n_image == 73:
            if moving_left == True:
                if player_location8[0] <= 414:
                    n_image = 74
                    print("I can't go here...")
                else:
                    player_location8[0] -= 3
                    player_locx = player_location8[0]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        elif n_image == 74:
            if moving_up == True:
                if player_location8[1] <= 105:
                    n_image = 75
                    print("I can't go here...")
                else:
                    player_location8[1] -= 3
                    player_locy = player_location8[1]
                    print("---x--- " + str(player_locx) + "\t" + "---y--- " + str(player_locy))

        #elif n_image == 27:



    #gestione eventi

    for event in pygame.event.get():
    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if n_image == 6 or n_image == 18 or n_image == 19:
                pass

            elif n_image == 26 or n_image == 27 or n_image == 28 or n_image == 29 or n_image == 40 or n_image == 41 or (n_image >= 72 and n_image <= 74):
                pass

            elif n_image == 81:
                n_image += 2

            else:
                n_image += 1

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

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


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