import pygame

pygame.init()

class Square:
    def __init__(self,rect):
        self.rect = pygame.Rect(rect)
        self.color = (0, 0, 0)
        self.adjacents = {'up' : None, 'down' : None, 'left' : None, 'right' : None}

    def draw(self,window,color):
        pygame.draw.rect(window, color, self.rect)