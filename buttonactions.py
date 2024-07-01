#Button Actions
import pygame
import sys

def exit():
    pygame.quit()
    sys.exit()

def none():
    return "start"

def actions(action):
    if action == "ext":
        exit()
    elif action == "lda":
        return "load"
    elif action == "sta":
        return "start"
    else:
        return none()
