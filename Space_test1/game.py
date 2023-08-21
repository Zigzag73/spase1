import pygame
import sys
import language as l
import animations as an
from menu import *
pygame.init()

info = pygame.display.Info()
fulldisplay_info = (info.current_w,info.current_h)
size_minimap = (fulldisplay_info[0]/5,fulldisplay_info[0]/5)
nomber_language = 0
width = 500
height = 500
FPS = 60
speed_player = 40

name_display = "Squares"


icon = pygame.transform.scale((pygame.image.load("pictures/icon.png")),(30,30))
menu_bd = pygame.transform.scale(pygame.image.load("pictures/menu_bg.png"),fulldisplay_info)
game_bd = pygame.transform.scale(pygame.image.load("pictures/space.jpg"),fulldisplay_info)
#player = 0
#terra = 1
#sun   = 2
size_icon_minimaps = fulldisplay_info[0]/100
mini_maps_icon = [pygame.transform.scale(pygame.image.load("pictures/terra.png"),(size_icon_minimaps,size_icon_minimaps)),
                  pygame.transform.scale(pygame.image.load("animations/sun_animation/sun_1.png"),(size_icon_minimaps,size_icon_minimaps)),
                  pygame.transform.scale(pygame.image.load("animations/mars_animation/mars_1.png"),(size_icon_minimaps,size_icon_minimaps)),
                  pygame.transform.scale(pygame.image.load("animations/moon_animation/moon_1.png"),(size_icon_minimaps,size_icon_minimaps)),
                  pygame.transform.scale(pygame.image.load("animations/mercury_animation/mercury_1.png"),(size_icon_minimaps,size_icon_minimaps)),
                  pygame.transform.scale(pygame.image.load("animations/venus_animation/venus_1.png"),(size_icon_minimaps,size_icon_minimaps)),
                  pygame.transform.scale(pygame.image.load("pictures/player.png"),(size_icon_minimaps,size_icon_minimaps))]
flang ={
    "up" : False,
    "down": False,
    "right" : False,
    "left": False
}
x = 100
y = 100 

colors = {
    "Red":(255,0,0),
    "Eastern Blue":(30, 129, 176)
}


display = pygame.display.set_mode(fulldisplay_info,pygame.FULLSCREEN)

mini_maps = pygame.Surface((fulldisplay_info[0]/4,fulldisplay_info[0]/4))
mini_maps.set_alpha(100)

clock = pygame.time.Clock()
pygame.display.set_caption(name_display)
pygame.display.set_icon(icon)













#earth =0
#sun   =1
#mars  =2
#moon  =3
#mercury = 4
#venus = 5

space = [an.Animation(500,200,300,300,5),
          an.Animation(-10000,-10000,2000,2000,10),
          an.Animation(6000,8000,250,250,4),
          an.Animation(-600,100,75,75,9),
          an.Animation(-15000,-9000,100,100,6),
          an.Animation(-6000,-15000,290,290,3)]

space[0].animation_plus("animations/terra_animation/terra_",12)
space[1].animation_plus("animations/sun_animation/sun_",12)
space[2].animation_plus("animations/mars_animation/mars_",12)
space[3].animation_plus("animations/moon_animation/moon_",12)
space[4].animation_plus("animations/mercury_animation/mercury_",12)
space[5].animation_plus("animations/venus_animation/venus_",12)





runing = True
def menu1():
    play = Menu(display,"1-blackmoor-let-plain103.ttf",100)  
    play.create_button(l.play[nomber_language],(100,100,300,100)) 
    play.create_button(l.language[nomber_language],(100,250,600,100)) 
    play.create_button(l.exit[nomber_language],(100,400,300,100)) 
    runing1 = True
    while runing1 :
        a = play.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (a == 0) :
                    print("i i i  ха")
                    game1()
                if (a == 1):
                    runing1 = False
                    language_options()
                if (a == 2) :
                    pygame.quit()
                    sys.exit()
                
        display.blit(menu_bd,(0,0))
        display.blit(icon,(0,0))
        
        play.draw_menu((100,100,100))
        pygame.display.update()
        clock.tick(FPS)
  
def language_options():
    global nomber_language
    language_option = Menu(display,"1-blackmoor-let-plain103.ttf",100) 
    language_option.create_button(l.english[nomber_language],(100,100,300,100)) 
    language_option.create_button(l.ukrainian[nomber_language],(100,250,600,100)) 
    language_option.create_button(l.back[nomber_language],(100,400,300,100)) 
    runing1 = True
    while runing1 :
        a = language_option.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (a == 0) :
                    nomber_language = 0  
                if (a == 1):
                    nomber_language = 1
                if (a == 2) :
                    runing1 = False
                    menu1()
                
        display.blit(menu_bd,(0,0))
        display.blit(icon,(0,0))
        
        language_option.draw_menu((100,100,100))
        pygame.display.update()
        clock.tick(FPS)
def game1():
    game = Menu(display,"1-blackmoor-let-plain103.ttf",100)  
    game.create_button2(icon,(0,0,30,30)) 
    global flang
    global speed_player
    runing1 = True
    while runing1 :
        
        a = game.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (a == 0) :
                    pause1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    flang["up"]= True
                if event.key == pygame.K_s:
                    flang["down"]= True
                if event.key == pygame.K_d:
                    flang["right"]= True
                if event.key == pygame.K_a:
                    flang["left"]= True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    flang["up"]= False
                if event.key == pygame.K_s:
                    flang["down"]= False
                if event.key == pygame.K_d:
                    flang["right"]= False
                if event.key == pygame.K_a:
                    flang["left"]= False
         
               
        display.blit(game_bd,(0,0))  
         
        draw_space()
        draw_minimaps()
        game.draw_menu((100,100,100))
        pygame.display.update()
        clock.tick(FPS)

def pause1():
    pause = Menu(display,"1-blackmoor-let-plain103.ttf",100)  
    pause.create_button2(icon,(0,0,30,30)) 
    pause.create_button(l.pausa[nomber_language],(100,400,300,100)) 
    runing2 = True
    while runing2 :
        b = pause.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing1 = not runing1
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (b == 0) :
                    runing2 = False
                if (b == 1):
                    menu1()  
                
            pause.draw_menu((100,100,100))           
            pygame.display.update()
            clock.tick(FPS)
def draw_space():
    for i in range(len(space)):
        space[i].draw_animation(display,0,11)
        space[i].forward(flang["down"],flang["up"],flang["left"],flang["right"],speed_player)

    
def draw_minimaps():
    mini_maps.fill((100,100,100))
    for i in range(len(space)):
        x = 150+(space[i].rec.x/100)
        y = 150+(space[i].rec.y/100)
        mini_maps.blit(mini_maps_icon[i],(x,y))
    
    
    mini_maps.blit(mini_maps_icon[-1],(155,155))
    display.blit(mini_maps,(fulldisplay_info[0]-400,0)) 
    
    
    
menu1()
   
