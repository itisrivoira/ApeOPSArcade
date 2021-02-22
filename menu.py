import pygame
from pygame.locals import *
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import os
import time
import sys
import math

pygame.init()
pygame.mixer.init()

class player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
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

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1
            
        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1


config = {'DEBUG': False, 'sound_effects': True, 'background_music': True, 'show_score': True, 'high_scores': [0, 0, 0, 0, 0, 0, 0, 0, 0]}

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()
runner = player(200, 313, 64, 64)
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
BLUE = 0, 0, 255
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 70
TOGGLE_WIDTH = BUTTON_WIDTH * 1.875
TOGGLE_ADJ = BUTTON_WIDTH * 0.245
tmp = None
music_pause = False

pygame.mixer.music.load ( "./Sound/ncsound.mp3" )  # Get the first track from the playlist
pygame.mixer.music.play(-1)  


def text_objects(text, font):
    textSurface = font.render(text, True, "black")
    return textSurface, textSurface.get_rect()


def redWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))


def windowCharacter():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    pygame.display.update()


def quitGame():
    pygame.quit()
    quit()


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def toggle_btn(text, x, y, w, h, click, text_colour=BLACK, enabled=True, draw_toggle=True, blit_text=True, enabled_color=LIGHT_BLUE, disabled_color=GREY):
    mouse = pygame.mouse.get_pos()
    # draw_toggle and blit_text are used to reduce redundant drawing and blitting (improves quality)
    rect_height = h // 2
    if rect_height % 2 == 0:
        rect_height += 1
    if enabled and draw_toggle:
        pygame.draw.rect(win, WHITE, (x + TOGGLE_WIDTH - h // 12, y, TOGGLE_ADJ, rect_height))
        pygame.draw.rect(win, enabled_color, (x + TOGGLE_WIDTH, y, TOGGLE_ADJ, rect_height))
        draw_circle(win, int(x + TOGGLE_WIDTH), y + h // 4, h // 4, enabled_color)
        draw_circle(win, int(x + TOGGLE_WIDTH + TOGGLE_ADJ), y + h // 4, h // 4, enabled_color)
        draw_circle(win, int(x + TOGGLE_WIDTH + TOGGLE_ADJ), y + h // 4, h // 5, WHITE)  # small inner circle
    elif draw_toggle:
        pygame.draw.rect(win, WHITE, (x + TOGGLE_WIDTH - h // 12, y, TOGGLE_ADJ, rect_height))
        pygame.draw.rect(win, disabled_color, (x + TOGGLE_WIDTH, y, TOGGLE_ADJ, rect_height))
        draw_circle(win, int(x + TOGGLE_WIDTH), y + h // 4, h // 4, disabled_color)
        draw_circle(win, int(x + TOGGLE_WIDTH + TOGGLE_ADJ), y + h // 4, h // 4, disabled_color)
        draw_circle(win, int(x + TOGGLE_WIDTH), y + h // 4, h // 5, WHITE)  # small inner circle
    if blit_text:
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        text_surf, text_rect = text_objects(text, smallText)
        text_rect.topleft = (x, y)
        win.blit(text_surf, text_rect)
    global tmp
    tmp = x + TOGGLE_WIDTH < mouse[0] < x + TOGGLE_WIDTH + w and y < mouse[1] < y + h
    return x + TOGGLE_WIDTH < mouse[0] < x + TOGGLE_WIDTH + w and y < mouse[1] < y + h and click and pygame.time.get_ticks() > 100


def options_menu():
    global music_pause
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    pygame.display.update()
    show = True
    draw_bg_toggle = draw_effects_toggle = True
    mouse = pygame.mouse.get_pos()
    while show:
        click = False
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4 and (pressed_keys[K_LALT] or pressed_keys[K_RALT]) or event.key == K_q))
            if event.type == QUIT or alt_f4:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                click = True

        if toggle_btn("Background Music", 250, 100, BUTTON_WIDTH, BUTTON_HEIGHT, click, enabled=config['background_music'], draw_toggle = draw_bg_toggle):
            draw_bg_toggle = True
            config['background_music'] = not config['background_music'];
            if tmp:
                clickedBtn = pygame.mouse.get_pressed()
                if clickedBtn[0] == 1:
                    music_pause = not music_pause
            if music_pause:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        elif toggle_btn("Sound Effects", 250, 200, BUTTON_WIDTH, BUTTON_HEIGHT, click,  enabled=config['sound_effects'], draw_toggle = draw_effects_toggle):
            draw_effects_toggle = True
            config['sound_effects'] = not config['sound_effects'];
        elif button("Back", 350, 280, BUTTON_WIDTH - 20, BUTTON_HEIGHT - 20, LIGHT_BLUE, BLUE, click):
            return
        else:
            draw_bg_toggle = draw_effects_toggle = False
        pygame.display.update()
        clock.tick(60)
        

def button(msg, x, y, w, h, iCol, aCol, click = False, action = None):
    mouse = pygame.mouse.get_pos()
    clickedBtn = pygame.mouse.get_pressed()
    val = False
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, aCol, (x, y, w, h))
        if clickedBtn[0] == 1 and action != None:
            action()
        if click and pygame.time.get_ticks() > 100:
            val = True
    else:
        pygame.draw.rect(win, iCol, (x, y, w, h), 6)
        pygame.draw.rect(win, iCol, (x+4, y+4, w-7, h-7))
    
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w/2)), y + (h/2) )
    win.blit(textSurf, textRect)
    return val


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
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Ape OPS Arcade", largeText)
        TextRect.center = ((W/2, H/3))
        win.blit(TextSurf, TextRect)
        

        button("Play", 150, 330, 100, 50, (25, 35, 255), (0, 0, 255), action = game_loop)
        button("Options", 350, 330, 100, 50, (25, 35, 255), (0, 0, 255), action = options_menu)
        button("Quit", 550, 330, 100, 50, (25, 35, 255), (0, 0, 255), action = quitGame)
        
        pygame.display.update()
        clock.tick(60)


bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

def game_loop():

    runGame = True
    while runGame:
        global bgX
        global bgX2
        windowCharacter()
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
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not(runner.jumping):
                runner.jumping = True
        
        if keys[pygame.K_DOWN]:
            if not(runner.sliding):
                runner.sliding = True

        clock.tick(speed)

game_intro()