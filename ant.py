import pygame

pygame.init()

class Ant:
    def __init__(self, square):
        self.actual = square
        self.dir = 'right'
    
    def walk(self):
        if self.dir == 'right':
            if self.actual.dir == 'r':
                self.actual = self.actual.adjacents['down']
                self.dir = 'down'
            if self.actual.dir == 'l':
                self.actual = self.actual.adjacents['up']
                self.dir = 'up'

        if self.dir == 'left':
            if self.actual.dir == 'r':
                self.actual = self.actual.adjacents['up']
                self.dir = 'up'
            if self.actual.dir == 'l':
                self.actual = self.actual.adjacents['down']
                self.dir = 'down'
        
        if self.dir == 'up':
            if self.actual.dir == 'r':
                self.actual = self.actual.adjacents['right']
                self.dir = 'right'
            if self.actual.dir == 'l':
                self.actual = self.actual.adjacents['left']
                self.dir = 'left'
        
        if self.dir == 'down':
            if self.actual.dir == 'r':
                self.actual = self.actual.adjacents['left']
                self.dir = 'left'
            if self.actual.dir == 'l':
                self.actual = self.actual.adjacents['right']
                self.dir = 'right'
        
        self.actual.next_color()
            