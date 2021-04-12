import pygame
from pygame.locals import *
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import os
import time
import sys
import math
import random
#import cv2

pygame.mixer.pre_init()
pygame.init()

class Player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    fall = pygame.image.load(os.path.join('images', '0.png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
        self.hitbox = ()
        self.falling = False

    def draw(self, win):
        
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))

        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//28], (self.x,self.y))
            self.jumpCount += 1
            
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
       
        elif self.sliding or self.slideUp:
           
            if self.slideCount < 20:
                self.y += 1
            
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x, self.y + 3, self.width - 8, self.height - 35)
            
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
                self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 13)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) Mostra hitbox


class Saw(object):

    img = [pygame.image.load(os.path.join('images', 'SAW0.png')), pygame.image.load(os.path.join('images', 'SAW1.png')), pygame.image.load(os.path.join('images', 'SAW2.png')), pygame.image.load(os.path.join('images', 'SAW3.png'))]

    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0

    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        if self.count >= 8:
            self.count = 0 
        win.blit(pygame.transform.scale(self.img[self.count//2], (64, 64)), (self.x, self.y))
        self.count += 1
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) Mostra hitbox
    
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
    

class Spike(Saw):

    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28, 315)
        win.blit(self.img, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) Mostra hitbox

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False


def redWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))


def mainWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    for w in objects:
        w.draw(win)
    pygame.display.update()


def quitGame():
    pygame.quit()
    quit()


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def reset():
    global objects, bgX, bgX2, runner, pause, fall_speed

    bgX = 0
    bgX2 = bg.get_width()
    objects = []
    runner = Player(200, 313, 64, 64)
    pause = 0
    fall_speed = 0
    mainWindow()
    game_intro()


config = {'DEBUG': False, 'sound_effects': True, 'background_music': True, 'show_score': True, 'high_scores': [0, 0, 0, 0, 0, 0, 0, 0, 0]}

objects = []

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()
runner = Player(200, 313, 64, 64)
pygame.time.set_timer(USEREVENT + 1, random.randrange(2300, 3500))
speed = 60
clock = pygame.time.Clock()

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
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 70
TOGGLE_WIDTH = BUTTON_WIDTH * 1.875
TOGGLE_ADJ = BUTTON_WIDTH * 0.245
tmp = None
music_pause = False
pause = 0
fall_speed = 0
showMusicToggle = True
showSoundEffectToggle = True

pygame.mixer.music.load( "./Sound/ncsound.ogg" )  # Get the first track from the playlist
pygame.mixer.music.play(-1) 

def text_objects(text, font, color = BLACK):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def commandsList():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    pygame.display.update()
    show = True
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
        clock.tick(60)


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
        clock.tick(60)
    showBtn = False


def menuButton(img, x, y, w, h, click = False, action = None):
    
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


def endScreen():

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        win.blit(bg, (0, 0))
        death = pygame.image.load(os.path.join('menuAssets', 'died.png'))
        restart = pygame.image.load(os.path.join('menuAssets', 'restart.png'))
        win.blit(death, (W/4, H/3 - 50))
        win.blit(restart, (W/4 - 10, H / 2))
        pygame.display.update()
    
    global objects, bgX, bgX2, runner, pause, fall_speed

    bgX = 0
    bgX2 = bg.get_width()
    objects = []
    runner = Player(200, 313, 64, 64)
    pause = 0
    fall_speed = 0
    mainWindow()
    game_intro()


# def video():
    
#     video = cv2.VideoCapture('./Sound/file_example_MP4_1920_18MG.mp4')
#     if (video.isOpened() == False):
#         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    
#     while (video.isOpened()):
#         ret, frame = video.read()
#         if ret:
#             cv2.imshow('Frame', frame)
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 break
#         else:
#             break
        
#         video.release()
#         cv2.destroyAllWindows()

#     pygame.time.wait(3000)   
#     game_loop()


def game_intro():

    music_pause = False
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        redWindow()

        title = pygame.image.load(os.path.join('menuAssets', 'title.png'))
        win.blit(title, (25, 0))

        menuButton("play_button.png", W/4 + 20, 215, 382, 80, action = game_loop)
        menuButton("options_button.png", W/3 - 10, 345, 301, 47, action = options_menu)
        
        pygame.display.update()
        clock.tick(60)


def game_loop():

    global bgX, bgX2, pause, fall_speed
    runGame = True
    #end = False
    while runGame:
        mainWindow()

        #if end:
        #    endScreen()
        if pause > 0:
            pause += 1
            if pause > fall_speed * 2:
                endScreen()

        for obj in objects:
            if obj.collide(runner.hitbox):
                runner.falling = True
                #end = True
                if pause == 0:
                    fall_speed = speed
                    pause = 1

            obj.x -= 1.8
            if obj.x < obj.width * - 1:
                objects.pop(objects.index(obj))

        bgX -= 1.8
        bgX2 -= 1.8
        
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()
        
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                runGame = False
                pygame.quit()
                quit()
            
            if event.type == USEREVENT + 1:
                tmp = random.randrange(0, 2)
                if tmp == 0:
                    objects.append(Saw(810, 310, 64, 64))
                else:
                    objects.append(Spike(810, 0, 48, 320))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not(runner.jumping):
                runner.jumping = True
        
        if keys[pygame.K_DOWN]:
            if not(runner.sliding):
                runner.sliding = True

        if keys[K_ESCAPE]:
            reset()

        clock.tick(speed)

game_intro()