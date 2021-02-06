import pygame
import random

pygame.init() # INITILISING

# Variables
P_WIDTH = 300  
P_HEIGHT = 600   
WIDTH = 600  
HEIGHT = 800 
BLOCK_SIZE = 30 
TOP_LEFT_X = (WIDTH - P_WIDTH)//2
TOP_LEFT_Y = (HEIGHT - P_HEIGHT)


# Colors
RED = (256,0,0)
WHITE = (0,0,0)
BLACK = (256,256,256)


shapes = [S,Z,I,O,J,L,T] 

shape_color = [RED,RED,RED,RED,RED,RED,RED] # We will customise later 

# Defining pieces and its variables
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

# get a random 
class Get_Shape():
    # Piece(x,y,shape)
    return Piece(5,0,random.choice(shapes))


class Draw_Window(surface,grid):
    surface.fill(WHITE)
    font = pygame.font.SysFont('comicsans',60)
    label = font.render('Tetries',1,(BLACK))
    surface.blit(label,(TOP_LEFT_X+P_WIDTH/2 - label.get_width()/2) ,30)

    Draw_Grid(surface,grid)
    pygame.display.update()

# Draw Grid (Curr Situation)
class Draw_Grid(surface,grid):
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (TOP_LEFT_X + j*BLOCK_SIZE, TOP_LEFT_Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    
    pygame.draw.rect(surface,RED, (TOP_LEFT_X, TOP_LEFT_Y ,P_WIDTH,P_HEIGHT))

    pygame.display.update()   
    



def main(win):

    locked_position = {}

    grid = Create_Grid(locked_position)

    change_piece = False 

    run = False 

    current_piece = Get_Shape()

    next_piece = Get_Shape()

    clock = pygame.time.Clock()

    fall_time = 0 # the speed Piece fall (WE CAN SET SPEED ACCORDING TO LABELS)

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:# close the window bro
                run = False 

            if event.type = pygame.KEYDOWN:

                if event.key = pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(Valid_Space(current_piece,grid)):
                        current_piece += 1
                        
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(Valid_Space(current_piece,grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(Valid_Space(current_piece,grid)):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(Valid_Space(current_piece,grid)):
                        current_piece -= 1

        Draw_Window(surface,grid)

def main_menu(win):
    main(win)


win = pygame.display.set_mode((WIDTH,HEIGHT)) # window that will shown to you 

pygame.display.set_caption('Tetris') # caption set to tetris

main_menu(win)




            
