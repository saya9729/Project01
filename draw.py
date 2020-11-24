import pygame
import math
import time
# intialize the pygame
pygame.init()

# global variables

screenWidth = 15 # the number of tile in x axis
screenHeight = 11 # the number of tile in y axis
speed = 1

# create the screen
screen = pygame.display.set_mode((screenWidth*64, screenHeight*64))


# title and icon
pygame.display.set_caption("H&S")
icon = pygame.image.load('H&S.png')
pygame.display.set_icon(icon)


# seeker  
seeker_img = pygame.image.load('dragon.png')
seeker_x = 4
seeker_y = 4
seeker_y_change = speed
seeker_x_change = speed


# show the seeker image on screen
def seeker(x, y):
    screen.blit(seeker_img, (x*64, y*64))


# seeker border reflex
def seeker_border_reflex(seeker_x, seeker_y, seeker_x_change, seeker_y_change):

    if seeker_x <= 0:
        seeker_x_change = speed
    elif seeker_x >= screenWidth-1:
        seeker_x_change = -speed
    if seeker_y <= 0:
        seeker_y_change = +speed
    elif seeker_y >= screenHeight-1:
        seeker_y_change = -speed
    seeker_y += seeker_y_change
    seeker_x += seeker_x_change

    return seeker_x, seeker_y, seeker_x_change, seeker_y_change


# hider
hider_img = pygame.image.load('warrior.png')
hider_x = 4
hider_y = 3
hider_y_change = speed
hider_x_change = speed


# show the hider image on screen
def hider(x, y):
    screen.blit(hider_img, (x*64, y*64))


# hider border reflex
def hider_border_reflex(hider_x, hider_y, hider_x_change, hider_y_change):
    if hider_x <= 0:
        hider_x_change = speed
    elif hider_x >= screenWidth-1:
        hider_x_change = -speed
    if hider_y <= 0:
        hider_y_change = speed
    elif hider_y >= screenHeight-1:
        hider_y_change = -speed
    # hider_y += hider_y_change
    hider_x += hider_x_change

    return hider_x, hider_y, hider_x_change, hider_y_change

# check the collision of seeker and hider 
def is_collision(seeker_x, seeker_y, hider_x, hider_y):
    distance = math.sqrt((math.pow(seeker_x-hider_x, 2)) + (math.pow(seeker_y - hider_y, 2)))
    if distance <= 0 :
        return True
    return False


# the tile map
tile_img = pygame.image.load('square.png')


# map function
def tilemap(tile_x, tile_y):
    for i in range(tile_x):
        for j in range(tile_y):
            screen.blit(tile_img, (i*64, j*64))



# game loop
running = True
while running:

    # RGB-color
    screen.fill((255, 255, 255))


    # edge border for seeker and hider
    hider_x, hider_y, hider_x_change, hider_y_change = hider_border_reflex(hider_x, hider_y, hider_x_change, hider_y_change)
    seeker_x, seeker_y, seeker_x_change, seeker_y_change = seeker_border_reflex(seeker_x, seeker_y, seeker_x_change, seeker_y_change)


    # check the collision
    collision = is_collision(seeker_x, seeker_y, hider_x, hider_y)
    if collision:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tilemap(screenWidth, screenHeight)
    seeker(seeker_x, seeker_y)
    hider(hider_x, hider_y)
    time.sleep(0.1)
    pygame.display.update()