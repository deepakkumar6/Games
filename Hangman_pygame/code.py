# Hangman Game by Deepak Kumar


import pygame
import os
import math
import random
from words import word_list
# from pic import *
# initial setup display
pygame.init()
WIDTH,HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hangman_pygame')# for display the caption of the game


# button's pos
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (GAP + RADIUS*2)*13)/2)
# startx = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2* RADIUS) / 2)
starty = 400
for i in range(26):
    x = startx+GAP*2 + ((RADIUS*2 + GAP)*(i%13))
    # x = startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i//13)*(GAP+RADIUS*2))
    letters.append([x,y,chr(ord('A')+i),True])


# fonts
LETTER_FONT = pygame.font.SysFont('comicsans',39)
WORD_FONT = pygame.font.SysFont('comicsans',50)
TITLE_FONT = pygame.font.SysFont('comicsans',50)


# load images
images = []
for i in range(7):
    img = pygame.image.load('hangman'+str(i)+'.png')
    images.append(img)


# game variables
hangman_status = 0
word = random.choice(word_list).upper()
guessed = []


WHITE = (255,255,255)
BLACK = (0,0,0)
# set up game loop
FPS = 60 # fps -frame per second
clock = pygame.time.Clock()
run = True

def draw():
    # filling the color
    win.fill(WHITE)
    # draw Title
    text = TITLE_FONT.render("HANGMAN GAME",1,BLACK)
    win.blit(text,(WIDTH//2-text.get_width()//2,20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word+= letter + ' '
        else:
            display_word += '_'+' '
    text = WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))

    # draw letter

    for letter in letters:
        x,y,ltr,vis = letter
        if vis:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            txt = LETTER_FONT.render(ltr,1,BLACK)
            win.blit(txt,(x-txt.get_width()/2,y-txt.get_height()//2))


    # drawing the hangman images
    win.blit(images[hangman_status],(150,100))
    # update the display
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message,1,BLACK)
    win.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2-text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

while run :

    clock.tick(FPS)

    draw()


    for event in pygame.event.get():# checking every event

        if event.type == pygame.QUIT:
            # this is cross button when we hover over x right corner
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,vis = letter
                if vis:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis<RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    draw()
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won :
        display_message('YOU WON!')

        break
    if hangman_status==6:
        display_message('YOU LOST!')
        break



pygame.quit() # this mean close the window






