import pygame

pygame.init()

class Square:
    def __init__(self,rect):
        self.rect = pygame.Rect(rect)
        self.color = (0, 0, 0)

    def draw(self,window,color):
        pygame.draw.rect(window, color, self.rect)