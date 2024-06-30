#Airport Manager
#George Weaver

#Imports
import pygame
from pygame.locals import *
import sys

#Initiating Pygame
pygame.init()

#Game window
#Setting to 0 makes it the size of the screen
swidth = 0
sheight = 0

displaysurf = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("Airport Manager")

#Window Icon
#logo_small = pygame.image.load("logo_icon_small.png")
#icon = pygame.image.load("window_icon.png")
#pygame.display.set_icon(icon)

# setting FPS
FPS = 60
framesps = pygame.time.Clock()

#Colours
black = 0,0,0
white = 255,255,255

#Fonts
matrix_big_fnt = pygame.font.SysFont("dubai",30,False,False)

while True:
    displaysurf.fill(black)
    #sets the key pressed to noting so that nothing is inputed in the textboxes at this point
    event_key_pressed = None
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    text = "Airport Manager"
    rendered_text =matrix_big_fnt.render(text,True, white)
    displaysurf.blit(rendered_text,( 200, 300))

    
    pygame.display.update()
    pygame.display.flip()
    framesps.tick(FPS)