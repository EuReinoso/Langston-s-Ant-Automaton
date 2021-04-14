import pygame

pygame.init()

class Square:
    def __init__(self,rect,graf):
        self.rect = pygame.Rect(rect)
        self.graf = graf
        self.state = 0
        self.dir = graf[self.state]
        self.adjacents = {'up' : None, 'down' : None, 'left' : None, 'right' : None}
    
    def next_color(self):
        if self.state < len(self.graf):
            self.dir = self.graf[self.state]
            self.state += 1
        else: 
            self.state = 1
            self.dir = self.graf[self.state]
        
