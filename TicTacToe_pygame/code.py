import pygame
import os
import random

pygame.init() # this step is must

#initial setup display
WIDTH,HEIGHT=1400,620
win = pygame.display.set_mode((WIDTH,HEIGHT))


# fonts
LETTER_FONT = pygame.font.SysFont("stencil",180)
print(pygame.font.get_fonts())

# board
board_pic = pygame.image.load('board_pic.png')

# color (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

# adjusting frame per second
FPS = 60
clock = pygame.time.Clock()

cell_pos = [[200, 200, 0, False, ' '], [200, 400, 1, False, ' '], [200, 600, 2, False, ' '],\
            [400, 200, 3, False, ' '], [400, 400, 4, False, ' '], [400, 600, 5, False, ' '],\
            [600, 200, 6, False, ' '], [600, 400, 7, False, ' '], [600, 600, 8, False, ' ']]





# game variable
player_type = ['X','O']

player = random.choice(player_type)

def draw():
    # print board
    win.fill(RED)
    win.blit(board_pic,(0,0))

    # print
    for cell in cell_pos:
        x,y,idx,vis,pyr=cell
        if vis:
            txt = LETTER_FONT.render(pyr,1,BLACK)
            win.blit(txt,(x-155,y-150))
    curr_player = LETTER_FONT.render(player,1,BLACK)
    win.blit(curr_player,(1169, 238))
    pygame.display.update()

# check game things
def check_if_game_over(board):
    # Rows Check
    if (board[0][4]==board[1][4]==board[2][4] and board[0][4] in 'OX')or \
       (board[3][4]==board[4][4]==board[5][4] and board[3][4] in 'OX')or \
       (board[6][4]==board[7][4]==board[8][4] and board[6][4] in 'OX'):
       return False

    # Columns Check
    if (board[0][4]==board[3][4]==board[6][4] and board[0][4] in 'OX')or \
       (board[1][4]==board[4][4]==board[7][4] and board[1][4] in 'OX')or \
       (board[2][4]==board[5][4]==board[8][4] and board[2][4] in 'OX'):
       return False

    # Diagonal Check
    if (board[0][4]==board[4][4]==board[8][4] and board[0][4] in 'OX')or \
       (board[2][4]==board[4][4]==board[6][4] and board[2][4] in 'OX'):
       return False

    return True

def display_message(message):

    pygame.time.delay(1000)
    win.fill(WHITE)
    text = LETTER_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2-text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)




def index(x,y,X,Y):
    return X-200<=x<=X and Y-200<=y<=Y


turn = 0
run = True
while run:

    clock.tick(FPS)

    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            print(m_x,m_y)

            for cell in cell_pos:
                x,y,idx,vis,pyr=cell
                if not vis:
                    if index(m_x,m_y,x,y):
                        cell[3] = True # if true print somethings
                        cell[4] = player
                        player = 'X' if player =='O' else 'O' # switch player
                        turn += 1
                        break

    draw()
    # check if anyone win
    won = check_if_game_over(cell_pos)
    if not won:
        pygame.time.delay(1000)
        player = 'X' if player =='O' else 'O' # we flipped here because we flip the player in adv(line 110)
        display_message('{} WON!'.format(player))
        run = False
        break

    if turn == 9:
        pygame.time.delay(1000)
        display_message('Tie')
        run = False
        break






