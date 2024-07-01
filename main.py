#Airport Manager
#George Weaver

#Imports
import pygame
from pygame.locals import *
import sys
import buttonactions as btnact
import random

#Initiating Pygame
pygame.init()

#Game window
#Setting to 0 makes it the size of the screen
displaysurf = pygame.display.set_mode((0,0))
pygame.display.set_caption("Airport Manager")

#getting the screens height and width
swidth, sheight = displaysurf.get_size()

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
red = 255,0,0
green = 0,255,0
blue = 0,0,255
flip_col = 255, 203, 7
light_grey = 51, 51, 51

#Fonts
flip_big_fnt = pygame.font.Font("Skyfont.ttf",80)
flip_medium_fnt = pygame.font.Font("Skyfont.ttf",50)
flip_small_fnt = pygame.font.Font("Skyfont.ttf",20)

#Variables
page = "start"

#Functions
def generate_flip_big_txt(text, colour):
    generated_text = flip_big_fnt.render(text,True, colour)
    return generated_text

def generate_flip_medium_txt(text, colour):
    generated_text = flip_medium_fnt.render(text,True, colour)
    return generated_text

def generate_flip_small_txt(text, colour):
    generated_text = flip_small_fnt.render(text,True, colour)
    return generated_text

def render_text(rendered_text,position, x, y):
    if position == "topleft":
        text_rect=rendered_text.get_rect(topleft = (x,y))
    elif position == "bottomleft":
        text_rect=rendered_text.get_rect(bottomleft = (x,y))
    elif position == "topright":
        text_rect=rendered_text.get_rect(topright = (x,y))
    elif position == "bottomright":
        text_rect=rendered_text.get_rect(bottomright = (x,y))
    else:
        text_rect=rendered_text.get_rect(center = (x,y))
    displaysurf.blit(rendered_text,text_rect)

#Classes
#Buttons
class Button():
    def __init__(self, x, y, width, height, text, text_col, txt_hgt_col, bgd_colour, border, b_colour, action):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        self.text = text
        self.text_col = text_col
        self.hgt_text_col = txt_hgt_col
        self.og_text_col = text_col
        self.bgd_colour = bgd_colour
        self.border = border
        self.border_colour = b_colour
        self.action = action
        self.rect = pygame.Rect((self.x_pos - self.width/2),(self.y_pos - self.height/2),self.width,self.height)

    def draw(self):
        if self.bgd_colour != None:
            pygame.draw.rect(displaysurf,self.colour,self.rect,self.width,10)

        self.text_surf = generate_flip_medium_txt(self.text,self.text_col)        
        txt_width = self.text_surf.get_width()
        txt_height = self.text_surf.get_height()
        txt_x_pos = self.x_pos -(txt_width/2)
        txt_y_pos = self.y_pos - (txt_height/2)

        displaysurf.blit(self.text_surf, (txt_x_pos,txt_y_pos))

        if self.border != None:
            pygame.draw.rect(displaysurf,self.border_colour,self.rect,self.border,10)
    
    def hover(self):
        m_x, m_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_x,m_y):
            self.text_col = self.hgt_text_col
            return True
        else:
            self.text_col = self.og_text_col
            return False
        
    def clicked(self):
        if pygame.mouse.get_pressed()[0]== True and self.hover() == True:
            self.do_action()

    def do_action(self):
        if self.action == "ext":
            btnact.exit()

class Menu_cloud():
    def __init__(self, image_name,width,height):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.x = random.randint((-self.width-10),(swidth))
        self.y = random.randint(10,(sheight/2)-100)
        self.active = True
        if self.x <= -self.width:
            self.active = False
        else:
            self.active = True

    def draw(self):
        if self.active == True:
            displaysurf.blit(self.image,(self.x,self.y))
            self.slide()

    def slide(self):
        if self.x > swidth:
            self.active = False
            self.x = -self.width
            self.y = random.randint(10,(sheight/2)-100)
        else:
            self.x += 1

class Menu_plane():
    def __init__(self, image_name,width,height):
        self.width = width
        self.height = height
        self.image1 = pygame.image.load(image_name+".png")
        self.image2 = pygame.image.load(image_name+"2.png")
        self.image3 = pygame.image.load(image_name+"3.png")
        self.x = -self.width
        self.y = 30
        self.active = False
        self.direction = "in"

    def set_surface(self):
        if self.direction == "in":
            self.image = pygame.transform.scale(self.image2,(self.width,self.height))
        elif self.direction == "out":
            self.image = pygame.transform.scale(self.image3,(self.width,self.height))
        else:
            self.image = pygame.transform.scale(self.image1,(self.width,self.height))

    def draw(self):
        if self.active == True:
            self.set_surface()
            displaysurf.blit(self.image,(self.x,self.y))
            self.slide()

    def slide(self):
        if self.x > swidth:
            self.active = False
            self.x = -self.width
            self.y = random.randint(10,(sheight/2)-100)
        elif self.x >= (swidth/2):
            self.y= self.y - 1
            self.direction = "out"
        elif self.y >= (sheight/2):
            self.y= (sheight/2)
            self.direction = "none"
        elif self.x <= swidth/2:
            self.y+=1
            self.direction = "in"
        self.x += 2



        

#Page Setups
    #Start Page
        #Buttons
lda_btn = Button((swidth/8),(sheight/6)*2, 200, 65, "Load Game", black, flip_col, None, None, None, "lda")

set_btn = Button((swidth/8)*7,(sheight/6)*2, 200, 65,"Settings",black, flip_col, None, None, None, "set")

tut_btn = Button((swidth/8),(sheight/6)*5, 200, 65,"Tutorial", black, flip_col, None, None, None, "tut")

ext_btn = Button((swidth/8)*7,(sheight/6)*5, 200, 65,"Exit",black, flip_col, None, None, None, "ext")

start_buttons = [lda_btn,tut_btn,set_btn,ext_btn]

cloud1 = Menu_cloud("Cloud1.png",200,99)
cloud2 = Menu_cloud("Cloud2.png",200,76)
cloud3 = Menu_cloud("Cloud3.png",200,76)
clouds = [cloud1,cloud2,cloud3]

m_plane1 = Menu_plane("airbus",200,76)
m_planes = [m_plane1]


while True:
    displaysurf.fill(green)
    #sets the key pressed 
    event_key_pressed = None
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    if page == "start":
        #Adding the background image
        bgd = pygame.image.load("mainBackground.png")
        bgd = pygame.transform.scale(bgd,(swidth,sheight))
        displaysurf.blit(bgd,(0,0))

        #renderig the title
        for plane in m_planes:
            if plane.active == False:
                if random.randint(0,100) == 1:
                    plane.active = True
            plane.draw()
        for cloud in clouds:
            if cloud.active == False:
                if random.randint(0,100) == 1:
                    cloud.active = True
            cloud.draw()
        for button in start_buttons:
            button.draw()
            button.hover()
            button.clicked()
        render_text(generate_flip_big_txt("Airport Manager",black),"center",swidth/2,50)

    
    pygame.display.update()
    pygame.display.flip()
    framesps.tick(FPS)