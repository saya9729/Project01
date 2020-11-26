# import world
import draw
import pygame


pygame.init()
# input data-------------------------


file = open("map1.txt", "r")
line = file.readlines()
n = int(line[0].split()[0])
m = int(line[0].split()[1])
map = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        map[i][j] = int(line[i + 1].split()[j])

global_mutation_rate=0.01
vision_radius=3
hint_interval=5
hint_radius=3
# World=world.world(5,2000)AA

# def draw():
#     draw.draw_data()
#
#     if not World.done():
#         World.update()
#     else:
#         World.genetic_algorithm()

draw.draw_data(n,m,map)
