import pygame,sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() #inizializzo pygame
pygame.display.set_caption('Ape Ops Arcade')
WINDOW_SIZE = (1280,720)
pygame.display.set_caption('Ape Ops Arcade')
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) #finestra di gioco
bg_image = pygame.image.load("Immaginiscrause/bgwhite.jpg") #background
pg_image = pygame.image.load("Immaginiscrause/hornyProtag.png") #protagonista
enemy_image = pygame.image.load("Immaginiscrause/hornySalvini.png") #nemico
menufight_image = pygame.image.load("Immaginiscrause/menu_ingame_fight.png") #menu fighting
iconpg_image = pygame.image.load("Immaginiscrause/medic_Icon.png") #icon image pg
iconen_image = pygame.image.load("Immaginiscrause/salvini_Icon.png") #icon image enemy
#pg hp
fullhppg_image = pygame.image.load("Immaginiscrause/hp_heart.png") #icon image fullhp
fullhp2pg_image = pygame.image.load("Immaginiscrause/hp_heart.png") #icon image fullhp
grayhppg_image = pygame.image.load("Immaginiscrause/hp_heart_gray.png") #icon image grayhp
#enemy hp
fullhpen_image = pygame.image.load("Immaginiscrause/hp_heart.png") #icon image fullhp
fullhp2en_image = pygame.image.load("Immaginiscrause/hp_heart.png") #icon image fullhp
grayhpen_image = pygame.image.load("Immaginiscrause/hp_heart_gray.png") #icon image grayhp

font = pygame.font.SysFont(None, 45)
color = "#000000"

def message_to_screen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [x, y])

while True:
    screen.blit(bg_image, (0, 0))   #bg
    screen.blit(pg_image,(100,85))  #pg
    screen.blit(enemy_image,(900,110))  #enemy
    screen.blit(menufight_image, (100, 475))    #menufight
    screen.blit(iconpg_image, (10, 10)) #iconpg
    screen.blit(iconen_image, (1175, 10))   #iconenemy
    #pg hp
    screen.blit(fullhppg_image, (150, 40))
    screen.blit(fullhp2pg_image, (215, 40))
    screen.blit(grayhppg_image, (280, 40))
    #enemy hp
    screen.blit(fullhpen_image, (920, 40))
    screen.blit(fullhp2en_image, (985, 40))
    screen.blit(grayhpen_image, (1050, 40))

    message_to_screen("KOWALSKI LEGASOV",color, 85,10)
    message_to_screen("BRIGADIERE RUSPA", color, 845, 10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)