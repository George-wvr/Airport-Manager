#Airport Manager
#George Weaver

#Imports
import pygame
from pygame.locals import *
import sys
import buttonactions as btnact
import random
import time

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
background = 41, 41, 41

#Fonts
flip_big_fnt = pygame.font.Font("Skyfont.ttf",80)
flip_medium_fnt = pygame.font.Font("Skyfont.ttf",50)
flip_small_fnt = pygame.font.Font("Skyfont.ttf",20)

#Variables
page = "start"
frame_count = 0
time_multiplier = 1
mouse_down = False
mouse_up = False

if swidth < 1200 or sheight < 600:
    page = "not_supported"

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

#Time Incrementation
def increment_time():
    global frame_count, time_multiplier, game_time
    if frame_count == (60/time_multiplier):
        frame_count = 0
        game_time = game_time + 1


#Classes
#Buttons
class Button():
    def __init__(self, x, y, width, height, text, text_col, txt_hgt_col, bgd_colour, border, b_colour, size, action):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        self.size = size
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
        if self.size == "big":
            self.text_surf = generate_flip_big_txt(self.text,self.text_col)
        elif self.size == "small":
            self.text_surf = generate_flip_small_txt(self.text,self.text_col)
        else:
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
        global mouse_up, mouse_down
        if mouse_down == True and mouse_up == True and self.hover() == True:
            self.do_action()
            mouse_down = False
            mouse_up = False

    def do_action(self):
        global page, time_multiplier
        if self.action == "tmu":
            if time_multiplier < 9:
                time_multiplier += 1
        elif self.action == "tmd":
            if time_multiplier > 1:
                time_multiplier -= 1
        else:
            page = btnact.actions(self.action)

#Clouds in the menu screen
class Menu_cloud():
    def __init__(self, image_name,width,height):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.x = random.randint((-self.width-10),(swidth))
        self.y = random.randint(10,(int(sheight/2))-100)
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
            self.y = random.randint(10,(int(sheight/2))-100)
        else:
            self.x += 1

#Plane in the menu
class Menu_plane():
    def __init__(self, image_name,width,height):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_name+".png")
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.x = -self.width
        self.y = 50
        self.active = False

    def draw(self):
        if self.active == True:
            displaysurf.blit(self.image,(self.x,self.y))
            self.slide()

    def slide(self):
        if self.x > swidth:
            self.active = False
            self.x = -self.width
            self.y = 50
        elif self.x >= (swidth/2):
            self.y= self.y - 1
        elif self.y >= (sheight/2):
            self.y= (sheight/2)
        elif self.x <= swidth/2:
            self.y+=1
        self.x += 2

#Page Setups
    #Start Page
        #Buttons
lda_btn = Button((swidth/8),(sheight/6)*2, 200, 65, "Load Game", black, flip_col, None, None, None, "medium", "lda")

set_btn = Button((swidth/8)*7,(sheight/6)*2, 200, 65,"Settings",black, flip_col, None, None, None, "medium", "set")

tut_btn = Button((swidth/8),(sheight/6)*5, 200, 65,"Tutorial", black, flip_col, None, None, None, "medium", "tut")

ext_btn = Button((swidth/8)*7,(sheight/6)*5, 200, 65,"Exit",black, flip_col, None, None, None, "medium", "ext")

cdt_btn = Button((swidth/2),(sheight/6)*5, 200, 65,"Credits",black, flip_col, None, None, None, "medium", "cdt")

start_buttons = [lda_btn,tut_btn,set_btn,ext_btn,cdt_btn]

        #Clouds
cloud1 = Menu_cloud("Cloud1.png",200,99)
cloud2 = Menu_cloud("Cloud2.png",200,76)
cloud3 = Menu_cloud("Cloud3.png",200,76)
clouds = [cloud1,cloud2,cloud3]
        #Plane
m_plane1 = Menu_plane("airbus",200,76)
m_planes = [m_plane1]

    #Game Screen
        #Buttons
lda_btn = Button(60,30, 100, 65, "Home", white, flip_col, None, None, None, "medium", "sta")

set_btn = Button(240,30, 200, 65,"Contracts",white, flip_col, None, None, None, "medium", "con")

tut_btn = Button(470,30, 200, 65,"Upgrades", white, flip_col, None, None, None, "medium", "upg")

ext_btn = Button(690,30, 200, 65,"Schedual",white, flip_col, None, None, None, "medium", "sch")

cdt_btn = Button((swidth-60),30, 200, 65,"help",blue, flip_col, None, None, None, "medium", "ext")

tmu_btn = Button((swidth-250),20, 10, 15,"+",blue, flip_col, None, None, None, "small", "tmu")

tmd_btn = Button((swidth-250),40, 10, 15,"-",blue, flip_col, None, None, None, "small", "tmd")

game_buttons = [lda_btn,tut_btn,set_btn,ext_btn,cdt_btn]

    #Schedual Screen
        #Buttons
lda_btn = Button(60,30, 100, 65, "Home", white, flip_col, None, None, None, "medium", "sta")

set_btn = Button(240,30, 200, 65,"Contracts",white, flip_col, None, None, None, "medium", "con")

tut_btn = Button(470,30, 200, 65,"Upgrades", white, flip_col, None, None, None, "medium", "upg")

ext_btn = Button(690,30, 200, 65,"Dashboard",red, flip_col, None, None, None, "medium", "lda")

cdt_btn = Button((swidth-60),30, 200, 65,"help",blue, flip_col, None, None, None, "medium", "ext")

tmu_btn = Button((swidth-250),20, 10, 15,"+",blue, flip_col, None, None, None, "small", "tmu")

tmd_btn = Button((swidth-250),40, 10, 15,"-",blue, flip_col, None, None, None, "small", "tmd")

schedual_buttons = [lda_btn,tut_btn,set_btn,ext_btn,cdt_btn]

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

    elif page == "load":
        render_text(generate_flip_big_txt("Feature Coming Soon",black),"center",swidth/2,sheight/2-50)
        render_text(generate_flip_big_txt("Loading Game",black),"center",swidth/2,sheight/2+50)
        page = "game"
        start_time = time.time()
        game_time = start_time

    elif page == "game":
        head = pygame.surface.Surface((swidth,60))
        head.fill(black)
        displaysurf.blit(head,(0,0))
        for button in game_buttons:
            button.draw()
            button.hover()
            button.clicked()

        game_time_read = time.localtime(time.time())
        hr = time.strftime("%H",game_time_read)
        min = time.strftime("%M",game_time_read)
        sec = time.strftime("%S",game_time_read)
        text = hr + ":" + min + ":" + sec
        render_text(generate_flip_small_txt(text,white),"topright",swidth-130,10)
        day = time.strftime("%a",game_time_read)
        num = time.strftime("%d",game_time_read)
        month = time.strftime("%b",game_time_read)
        text = day + " " + num + " " + month
        render_text(generate_flip_small_txt(text,white),"topright",swidth-130,30)
        text = "X"+str(time_multiplier)
        render_text(generate_flip_small_txt(text,red),"topright",swidth-218,10)
        increment_time()

    elif page == "schedual":
        head = pygame.surface.Surface((swidth,60))
        head.fill(black)
        displaysurf.blit(head,(0,0))
        for button in schedual_buttons:
            button.draw()
            button.hover()
            button.clicked()
    
    elif page == "not_supported":
        render_text(generate_flip_big_txt("Your screen is too small",white),"center",swidth/2,sheight/2-100)
        render_text(generate_flip_medium_txt("Please play on a larger screen",white),"center",swidth/2,sheight/2-50)
        render_text(generate_flip_medium_txt("Minimum size is 1200px by 600px",white),"center",swidth/2,sheight/2+50)
        text = "Your screen is " + str(swidth) +"px by " + str(sheight) + "px"
        render_text(generate_flip_medium_txt(text,red),"center",swidth/2,sheight/2+100)

    frame_count += 1
    pygame.display.update()
    pygame.display.flip()
    framesps.tick(FPS)