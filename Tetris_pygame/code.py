import pygame
import random

pygame.init()

# 
P_WIDTH = 300 
P_HEIGHT = 600 
WIDTH = 600 
HEIGHT = 800 
BLOCK_SIZE = 30 
TOP_LEFT_X = (WIDTH - P_WIDTH)//2
TOP_LEFT_y = (HEIGHT - P_HEIGHT)

win = pygame.display.set_mode((HEIGHT,WIDTH))

shapes = [S,Z,I,O,J,L,T] 
RED = (256,0,0)
shape_color = [RED,RED,RED,RED,RED,RED,RED]# we will customise later 
class Piece:
    def __init__(self,x,y,shape):
        self.x = x 
        self.y = y 
        self.shape = shape 
        self.color = shape_color[shape.index(shape)]
        self.rotation = 0 

class Create_Grid:
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (j,i) in locked:
                grid[i][j] = locked[(j,i)]
    return grid 

class Get_Shape():
    return random.choice(shapes)
