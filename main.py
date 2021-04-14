import pygame,sys
import numpy as np
from square import Square

pygame.init()

COLORS = {
    'BLACK' : (0, 0, 0),
    'WHITE' : (255, 255, 255),
    'BLUE'  : (0, 0, 200),
    'GREEN' : (0, 200, 0),
    'RED'   : (200, 0, 0)    
}

WINDOW_SIZE = (640,480)
tile_size = 10

grid_list = np.empty(shape= (WINDOW_SIZE[0]//tile_size, WINDOW_SIZE[1]//tile_size),dtype= object)
def grid_init():
    for i in range(len(grid_list)):
        for j in range(len(grid_list[0])):
            rect = pygame.Rect(i * tile_size, j * tile_size, tile_size, tile_size)
            grid_list[i][j] = Square(rect)

def draw_grid():
    for line in grid_list:
        for sqr in line:
            pygame.draw.rect(window, (0,0,0), sqr.rect)
            pygame.draw.rect(window, (200,200,200), sqr.rect, 1)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Langston Ant')

grid_init()
while True:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_grid()
    pygame.display.update()
