import pygame,sys
import numpy as np
from square import Square
from ant import Ant

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

COLORS = {
    0 : (0, 0, 0),
    1  : (0, 0, 200),
    2 : (0, 200, 0),
    3   : (200, 0, 0)    
}

graf = {
    0 : 'r',
    1 : 'l',
    2 : 'r'
}

WINDOW_SIZE = (640,480)
tile_size = 10

grid_list = np.empty(shape= (WINDOW_SIZE[0]//tile_size, WINDOW_SIZE[1]//tile_size),dtype= object)

def grid_init():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            rect = pygame.Rect(i * tile_size, j * tile_size, tile_size, tile_size)
            grid_list[i][j] = Square(rect, graf)

def adjacents_init():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            if i > 0:
                grid_list[i][j].adjacents['up'] = grid_list[i - 1][j]
            if i < len(grid_list) - 1:
                grid_list[i][j].adjacents['down'] = grid_list[i + 1][j]
            if j > 0:
                grid_list[i][j].adjacents['left'] = grid_list[i][j - 1]
            if j < len(grid_list[0]) - 1:
                grid_list[i][j].adjacents['right'] = grid_list[i][j + 1]

def draw_grid():
    for line in grid_list:
        for sqr in line:
            if sqr.state == 0:
                pygame.draw.rect(window, COLORS[sqr.state], sqr.rect)
            if sqr.state == 1:
                pygame.draw.rect(window, COLORS[sqr.state], sqr.rect)
            if sqr.state == 2:
                pygame.draw.rect(window, COLORS[sqr.state], sqr.rect)

            if sqr == ant.actual:
                pygame.draw.rect(window, WHITE, sqr.rect)
            
            #pygame.draw.rect(window, COLORS['WHITE'], sqr.rect, 1)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Langston Ant')


grid_init()
adjacents_init()

ant  = Ant(grid_list[len(grid_list)//2][len(grid_list[0])//2])
while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ant.walk()
    draw_grid()
    pygame.display.update()
