import pygame

pygame.init()

class Ant:
    def __init__(self, square):
        self.actual = square
        self.dir = 'right'
    
    def walk(self):
        
        if self.dir == 'right':
            if self.actual.dir == 'r':
                next_square = self.actual.adjacents['down']
                next_dir = 'down'
            if self.actual.dir == 'l':
                next_square= self.actual.adjacents['up']
                next_dir = 'up'

        if self.dir == 'left':
            if self.actual.dir == 'r':
                next_square = self.actual.adjacents['up']
                next_dir = 'up'
            if self.actual.dir == 'l':
                next_square = self.actual.adjacents['down']
                next_dir = 'down'
        
        if self.dir == 'up':
            if self.actual.dir == 'r':
                next_square = self.actual.adjacents['right']
                next_dir = 'right'
            if self.actual.dir == 'l':
                next_square = self.actual.adjacents['left']
                next_dir = 'left'
        
        if self.dir == 'down':
            if self.actual.dir == 'r':
                next_square = self.actual.adjacents['left']
                next_dir = 'left'
            if self.actual.dir == 'l':
                next_square = self.actual.adjacents['right']
                next_dir = 'right'
        
        self.actual.next_color()
        self.actual = next_square
        self.dir = next_dir
            