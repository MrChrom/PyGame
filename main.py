import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

# variable to keep our main loop running
running = True

# main loop
while running:
    # for loop through the even queue
    for event in pygame.event.get():
        # check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals
        if event.type == KEYDOWN:
            # if the Esc key has been pressed, set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False

