import pygame, random, sys

from pygame.locals import *

#Initiating Pygame
pygame.init()

#Game window
#Setting to 0 makes it the size of the screen
displaysurf = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Movement Testing")

# setting FPS
FPS = 60
framesps = pygame.time.Clock()

background = (0,0,0)
wall_colour = (50,50,50)
checkin_colour = (0,150,200)

class Traveler():
    def __init__(self):
        self.flight_num = 1
        self.colour = 1
        self.target = 0
        self.route = ["door1 outside", "door1 inside", "check in", "security", "gate"]
        self.x_pos = 575
        self.y_pos = 580
        self.queue_pos = None
    
    def draw(self):
        pygame.draw.circle(displaysurf, self.get_colour(self.colour),(self.x_pos,self.y_pos), 10)
        self.move()

    def move(self):
        x_target, y_target = get_target_position(self.route[self.target])
        if self.x_pos > x_target:
            self.x_pos -= 1
        elif self.x_pos < x_target:
            self.x_pos += 1
        if self.y_pos > y_target:
            self.y_pos -= 1
        elif self.y_pos < y_target:
            self.y_pos += 1

        self.check_at_location()

    def check_at_location(self):
        target_x, target_y = get_target_position(self.route[self.target])
        if self.x_pos == target_x and self.y_pos == target_y:
            if self.target < len(self.route):
                self.target += 1

    def get_colour(self, colour_val):
        if colour_val == 1:
            return (255,255,255)
    
all_travelers = []

def get_target_position(target_name):
    if target_name == "door1 outside":
        return 540,550
    if target_name == "door1 inside":
        return 540, 500
    if target_name == "check in":
        for desk in all_checkin_desks:
            if desk.full == False:
                

    else:
        return random.randint(0,1000), random.randint(0,600)
    
class Checkin_desk():
    def __init__(self):
        self.x_pos = 775
        self.y_pos = 400
        self.width = 200
        self.height = 50
        self.queue = []
        self.full = False


    def draw(self):
        pygame.draw.rect(displaysurf, checkin_colour, (self.x_pos, self.y_pos, self.width, self.height))

all_checkin_desks = [Checkin_desk()]

while True:
    displaysurf.fill(background)
    #sets the key pressed 
    event_key_pressed = None
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            mouse_up = True

    #Terminal Walls
    pygame.draw.rect(displaysurf,wall_colour,(0,520,1000,20))
    pygame.draw.rect(displaysurf, wall_colour, (490, 200, 20, 320))


    if len(all_travelers) == 0:
        all_travelers.append(Traveler())

    for traveler in all_travelers:
        traveler.draw()

    all_facilities = [all_checkin_desks]

    for type in all_facilities:
        for facility in type:
            facility.draw()


    pygame.display.update()
    pygame.display.flip()
    framesps.tick(FPS)