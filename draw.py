import pygame, sys
import math
import time
import random
import Seeker

# intialize the pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

# title and icon
pygame.display.set_caption("H&S")
icon = pygame.image.load('picture/H&S.png')
pygame.display.set_icon(icon)

# font
font = pygame.font.Font("picture/AndadaSC-Regular.ttf", 50)
font_2 =  pygame.font.Font("picture/Magic.ttf", 50)


#global
# screenWidth = m # the number of tile in x axis
# screenHeight = n # the number of tile in y axis
screenWidth = 48  # the number of tile in x axis
screenHeight = 24  # the number of tile in y axis
#color
WHITE = (255, 255, 255)

speed = 1

# create the screen
screen = pygame.display.set_mode((screenWidth * 32, screenHeight * 32))

# title and icon
pygame.display.set_caption("H&S")
icon = pygame.image.load('picture/H&S.png')
pygame.display.set_icon(icon)

# seeker  
seeker_img = pygame.transform.scale(pygame.image.load('picture/warrior.png'), (32, 32))
seeker_x = 4
seeker_y = 4
seeker_y_change = speed
seeker_x_change = speed


# show the seeker image on screen
def seeker(x, y):
    screen.blit(seeker_img, (x * 32, y * 32))


# seeker border reflex
def seeker_border_reflex(seeker_x, seeker_y, seeker_x_change, seeker_y_change):
    if seeker_x <= 0:
        seeker_x_change = speed
    elif seeker_x >= screenWidth - 1:
        seeker_x_change = -speed
    if seeker_y <= 0:
        seeker_y_change = +speed
    elif seeker_y >= screenHeight - 1:
        seeker_y_change = -speed
    seeker_y += seeker_y_change
    seeker_x += seeker_x_change

    return seeker_x, seeker_y, seeker_x_change, seeker_y_change


# hider
hider_img = pygame.transform.scale(pygame.image.load('picture/dragon.png'), (32, 32))
hider_x = 4
hider_y = 3
hider_y_change = speed
hider_x_change = speed


# show the hider image on screen
def hider(x, y):
    screen.blit(hider_img, (x * 32, y * 32))


# hider border reflex
def hider_border_reflex(hider_x, hider_y, hider_x_change, hider_y_change):
    if hider_x <= 0:
        hider_x_change = speed
    elif hider_x >= screenWidth - 1:
        hider_x_change = -speed
    if hider_y <= 0:
        hider_y_change = speed
    elif hider_y >= screenHeight - 1:
        hider_y_change = -speed
    # hider_y += hider_y_change
    hider_x += hider_x_change

    return hider_x, hider_y, hider_x_change, hider_y_change


# check the collision of seeker and hider 
def is_collision(seeker_x, seeker_y, hider_x, hider_y):
    distance = math.sqrt((math.pow(seeker_x - hider_x, 2)) + (math.pow(seeker_y - hider_y, 2)))
    if distance <= 0:
        return True
    return False


# the tile map
tile_img = pygame.transform.scale(pygame.image.load('picture/square.png'), (32, 32))

# wall
wall_1_img = pygame.transform.scale(pygame.image.load('picture/gemswall1.png'), (32, 32))
wall_2_img = pygame.transform.scale(pygame.image.load('picture/gemswall2.png'), (32, 32))
wall_3_img = pygame.transform.scale(pygame.image.load('picture/gemswall3.png'), (32, 32))
wall_4_img = pygame.transform.scale(pygame.image.load('picture/gemswall4.png'), (32, 32))

# border
border_1_img = pygame.transform.scale(pygame.image.load('picture/border1.png'), (32, 32))
border_2_img = pygame.transform.scale(pygame.image.load('picture/border2.png'), (32, 32))
border_3_img = pygame.transform.scale(pygame.image.load('picture/border3.png'), (32, 32))
border_4_img = pygame.transform.scale(pygame.image.load('picture/border4.png'), (32, 32))


# map function
def tilemap(tile_x, tile_y):
    for i in range(tile_x):
        for j in range(tile_y):
            screen.blit(tile_img, ((j+1) * 32, (i+1) * 32))


# backgrounds
paper_img = pygame.transform.scale(pygame.image.load('picture/paper.jpg'), (screenWidth * 32, screenHeight * 32))
game_over_img = pygame.transform.scale(pygame.image.load('picture/game_over.png'),
                                       (screenWidth * 32, screenHeight * 32))
game_win_img = pygame.transform.scale(pygame.image.load('picture/menu.png'),
                                       (screenWidth * 32, screenHeight * 32))
menu_img = pygame.transform.scale(pygame.image.load('picture/witchermenu.png'), (screenWidth * 32, screenHeight * 32))
hint_img = pygame.transform.scale(pygame.image.load('picture/hint.png'), (32, 32))


# game loop
def Print_score(x, y, size, color, score):
    # font = pygame.font.SysFont(None, size)
    # text = font.render(score, True, color)
    draw_text2(score, color, screen, y*32, x*32, 50, "picture/AndadaSC-Regular.ttf")
    # text_rect = text.get_rect()
    # text_rect.midtop = (y*32, x)
    # screen.blit(text, text_rect)
def Print_result(m,n, score, map):
    if (score <= 0):
        screen.blit(game_over_img, (0,0))
    elif (Scan(m,n, map)):
        screen.blit(game_win_img, (0, 0))
def Scan(m, n, map):
    total = 0
    for i in range(n):
        for j in range(m):
            if (map[i][j] == 2):
                total+=1
    if (total == 0): return True
    return False
# draw text function

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text,1, color)
    textrect = textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj, textrect)
def draw_text2(text, color, surface, x,y, size, fontStyle):
    font = pygame.font.Font(fontStyle, size)
    textobj = font.render(text,1, color)
    textrect = textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj, textrect)

# click bool
click = False

# Main Menu function (open)
def menu():
    while True:
        # Background for menu
        screen.blit(menu_img, (0, 0))

        # title of game
        draw_text('H I D E   &   S E E K', font, (255, 255, 255), screen, 578, 20)


        # Mouse get position

        mx, my = pygame.mouse.get_pos()

        # buttons
        button_1 = pygame.Rect(520, 380, 60, 60)
        button_2 = pygame.Rect(570, 195, 60, 60)
        button_3 = pygame.Rect(740, 110, 60, 60)
        button_4 = pygame.Rect(930, 195, 60, 60)
        button_5 = pygame.Rect(980, 380, 60, 60)
        button_6 = pygame.Rect(630, 250, 300, 350)



        #pygame.draw.rect(screen,(255,0,0),button_6)

        # # Background for menu
        # screen.blit(menu_img, (0, 0))
        #
        # # title of game
        # draw_text('H I D E   &   S E E K', font, (255, 255, 255), screen, 578, 20)

        # Map 1st button
        if button_1.collidepoint((mx, my)):
            time.sleep(0.1)
            draw_text('Map 1', font_2, (255, 255, 255), screen, 360, 380)
            if click:
                Load_map("map1.txt")


        # Map 2nd button
        if button_2.collidepoint((mx, my)):
            time.sleep(0.1)
            draw_text('Map 2', font_2, (255, 255, 255), screen, 410, 195)
            if click:
                Load_map("map2.txt")

        # Map 3rd button
        if button_3.collidepoint((mx, my)):
            time.sleep(0.1)
            draw_text('Map 3', font_2, (255, 255, 255), screen, 740+80, 110)
            if click:
                Load_map("map3.txt")

        # Map 4th button
        if button_4.collidepoint((mx, my)):
            time.sleep(0.1)
            draw_text('Map 4', font_2, (255, 255, 255), screen, 1010, 195)
            if click:
                Load_map("map4.txt")

        # Map 5 button
        if button_5.collidepoint((mx, my)):
            time.sleep(0.1)
            draw_text('Map 5', font_2, (255, 255, 255), screen, 980+80, 380)
            if click:
                Load_map("map5.txt")
        #Exit button
        if button_6.collidepoint((mx, my)):
            time.sleep(0.1)
            draw_text('Exit', font_2, (255, 255, 255), screen, 740, 630)
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click= True
            # if event.type == HOVER
        pygame.display.update()
        mainClock.tick(60)

def game(n, m, map):
    running = True
    seeker = Seeker.Seeker(n, m, map)
    seeker.update_seen()


    while running:
            # RGB-color
            screen.fill((255, 255, 255))
            # background print
            screen.blit(paper_img, (0, 0))
            time.sleep(0.1)
            if (seeker.score > 0 and not Scan(m, n, map)):
                seeker.look()
                seeker.set_direction()
                seeker.move()
            else:
                Print_result(m, n, seeker.score, map)
            for i in range(n):
                for j in range(m):
                    if (i==0 or j==0 or i==n-1 or j==m-1):
                        rand = math.floor(random.uniform(0, 4))
                        if rand == 0:
                            screen.blit(border_1_img, ((j) * 32, (i) * 32))
                        if rand == 1:
                            screen.blit(border_2_img, ((j) * 32, (i) * 32))
                        if rand == 2:
                            screen.blit(border_3_img, ((j) * 32, (i) * 32))
                        if rand == 3:
                            screen.blit(border_4_img, ((j) * 32, (i) * 32))
                    if (map[i][j] == 0):
                        screen.blit(tile_img, ((j+1) * 32, (i+1) * 32))
                    elif (map[i][j] == 1):
                        rand = math.floor(random.uniform(0, 4))
                        if rand == 0:
                            screen.blit(wall_1_img, ((j+1) * 32, (i+1) * 32))
                        if rand == 1:
                            screen.blit(wall_2_img, ((j+1) * 32, (i+1) * 32))
                        if rand == 2:
                            screen.blit(wall_3_img, ((j+1) * 32, (i+1) * 32))
                        if rand == 3:
                            screen.blit(wall_4_img, ((j+1) * 32, (i+1) * 32))

                    elif (map[i][j] == 2):
                        screen.blit(hider_img, ((j+1) * 32, (i+1) * 32))
                    elif (map[i][j] == 3):
                        screen.blit(seeker_img, ((j+1) * 32, (i+1) * 32))
                    elif (map[i][j] == 4):
                        screen.blit(hint_img, ((j+1) * 32, (i+1) * 32))
                    elif (map[i][j] == 6):
                        screen.blit(hint_img, ((j+1) * 32, (i+1) * 32))
            Print_score(0, m / 2, 30, WHITE, str(seeker.score))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            mainClock.tick(60)

# load map function for main
def Load_map(filename):
    file = open(filename, "r")
    line = file.readlines()
    n = int(line[0].split()[0])
    m = int(line[0].split()[1])
    map = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            map[i][j] = int(line[i + 1].split()[j])
    game(n, m, map)