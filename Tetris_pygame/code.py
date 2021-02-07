import pygame
import random

pygame.init() # INITILISING
pygame.font.init()


# Variables
WIDTH = 800
HEIGHT = 700
P_WIDTH = 300
P_HEIGHT = 600
BLOCK_SIZE = 30
TOP_LEFT_X = (WIDTH - P_WIDTH)//2
TOP_LEFT_Y = (HEIGHT - P_HEIGHT)


# Colors
RED = (255,0,0)
WHITE = (0,0,0)
BLACK = (255,255,255)
GREY = (128,128,128)


S = [['.....',
      '......', 
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S,Z,I,O,J,L,T]

shape_colors = [RED,RED,RED,RED,RED,RED,RED] # We will customise later

# Defining pieces and its variables
class Piece:
    def __init__(self,col,row,shape):
        self.x = col 
        self.y = row 
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def Create_Grid(locked_position={}):

    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if (j,i) in locked_position:
                grid[i][j] = locked_position[(j,i)]

    return grid
# get a random
def Get_Shape():
    # Piece(x,y,shape)
    global shapes,shape_colors 
    return Piece(5,0,random.choice(shapes))

def Draw_Text_Middle(surface,text,size,color):
    font = pygame.font.SysFont('comicsans',size,bold = True)
    label = font.render(text,1,color)
    surface.blit(label,(TOP_LEFT_X + P_WIDTH // 2 - (label.get_width()//2),TOP_LEFT_Y + P_HEIGHT//2-label.get_height()//2))






def Draw_Window(surface,grid,last_score,score=0):
    surface.fill(WHITE)
    pygame.font.init()
    font = pygame.font.SysFont('comicsans',60)
    label = font.render('Tetris',1,BLACK)
    surface.blit(label,(TOP_LEFT_X+P_WIDTH//2 - label.get_width()//2 ,30))

    font = pygame.font.SysFont('comicsans',30)
    label = font.render('score: '+str(score),1,BLACK)

    sx = TOP_LEFT_X + P_WIDTH + 50 
    sy = TOP_LEFT_Y + P_HEIGHT//2 - 100 
    surface.blit(label,(sx+20,sy+160))

    # high score 
    label = font.render('HIgh Score: '+str(score),1,BLACK)

    sx = TOP_LEFT_X - 200 
    sy = TOP_LEFT_Y + 200
    surface.blit(label,(sx+20,sy+160))

    for i in range(len(grid)): 
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (TOP_LEFT_X + j*BLOCK_SIZE, TOP_LEFT_Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    pygame.draw.rect(surface,RED, (TOP_LEFT_X, TOP_LEFT_Y ,P_WIDTH,P_HEIGHT),5)

    pygame.display.update()
    Draw_Grid(surface,grid)
    # pygame.display.update()

# Draw Grid (Curr Situation)
def Draw_Grid(surface,grid):

    sx = TOP_LEFT_X
    sy = TOP_LEFT_Y

    for i in range(len(grid)):
        pygame.draw.line(surface,GREY,(sx, sy+ i*BLOCK_SIZE),(sx+P_WIDTH,sy+i*BLOCK_SIZE))

        for j in range(len(grid[i])):
            pygame.draw.line(surface,GREY,(sx+j*BLOCK_SIZE,sy),(sx+j*BLOCK_SIZE,sy+ P_WIDTH))

def Convert_Shape_Format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i,line in enumerate(format):
        row = list(line)
        for j,col in enumerate(row):
            if col == '0':
                positions.append((shape.x+j,shape.y+i))

    for i,pos in enumerate(positions):
        positions[i] = (pos[0]-2,pos[1]-4)

    return positions



def Valid_Space(shape,grid):
    accepted_pos = [[(j,i) for j in range(10) if grid[i][j] == WHITE]for i in range(20)]
    # making thing on Dimensional
    accepted_pos = [j for sub in accepted_pos for j in sub]
    formatted = Convert_Shape_Format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] >= 0:
                return False
    return True

def Check_Lost(positions):
    for pos in positions:
        x,y = pos
        if y<1:
            return True
    return False

def Draw_Next_Shape(shape,surface):
    font = pygame.font.SysFont('comicsans',30)
    label = font.render('NEXT SHAPE',1,BLACK)

    sx = TOP_LEFT_X + P_WIDTH + 50 
    sy = TOP_LEFT_Y + P_HEIGHT // 2 - 100 

    format = shape.shape[shape.rotation % len(shape.shape)]

    for i,line in enumerate(format):
        row = list(line)
        for j,col in enumerate(row):
            if col == '0':
                pygame.draw.rect(surface,shape.color,(sx+j*BLOCK_SIZE,sy+i*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),0)

            
    surface.blit(label,(sx+10,sy-30))


def Clear_Row(grid,locked):

    inc =  0 

    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if WHITE not in row:
            inc+=1
            ind = i 
            for j in range(len(row)):
                try:
                    del locked[(j,i)]
                except:
                    continue 
    
    if inc > 0:
        for key in sorted(list(locked),key = lambda x:x[1])[::-1]:
            x,y = key 
            if y < ind:
                newkey = (x,y+inc)
                locked[newkey] = locked.pop(key)
    return inc 

def Update_Score(nscore):
    score = Max_Score()

    with open('score.txt','w') as f:
        if int(score)<=nscore:
            f.write(str(nscore))
        else:
            f.write(str(score))
     
def Max_Score():
    with open('score.txt','r') as f:
        lines = f.readlines()
        score = lines[0].strip()
    return score 







def main(win):

    last_score = Max_Score()

    locked_position = {}

    grid = Create_Grid(locked_position)

    change_piece = False

    run = True 

    current_piece = Get_Shape()

    next_piece = Get_Shape()

    clock = pygame.time.Clock()

    fall_time = 0 # the speed Piece fall (WE CAN SET SPEED ACCORDING TO LABELS)

    fall_speed = 0.25

    level_time = 0

    score = 0 

    while run:

        grid = Create_Grid(locked_position)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick() # FPS depend on the computer's setting

        if level_time/1000>20:
            level_time = 0 
            if fall_time > 0.12:
                fall_speed -= 0.005 
            



        if fall_time/1000>fall_speed:
            fall_time = 0
            current_piece.y+=1
            if not(Valid_Space(current_piece,grid)) and current_piece.y>0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:# close the window bro
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(Valid_Space(current_piece,grid)):
                        current_piece.x += 1

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
                        current_piece.rotation -= 1

        shape_pos = Convert_Shape_Format(current_piece)

        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y>-1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p  =(pos[0],pos[1])
                locked_position[p] = current_piece.color
            current_piece = next_piece
            next_piece = Get_Shape()
            change_piece = False
            score += 10 * Clear_Row(grid,locked_position)
        
        Draw_Window(win,grid,last_score,score)
        Draw_Next_Shape(next_piece,win)
        pygame.display.update()

        if Check_Lost(locked_position):
            Draw_Text_Middle(win,'YOU LOST',80,BLACK)
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            Update_Score(score)
    




        


def main_menu(win):
    run = True 
    while run:
        win.fill(WHITE)
        Draw_Text_Middle(win,'Please Press Any Key to Play',60,BLACK)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.KEYDOWN:
                main(win)
    pygame.display.quit()



win = pygame.display.set_mode((WIDTH,HEIGHT)) # window that will shown to you

pygame.display.set_caption('Tetris') # caption set to tetris

main_menu(win)





