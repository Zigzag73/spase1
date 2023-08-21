import pygame

pygame.init()
class Animation():
    def __init__(self,x,y,w,h,speed = 10,pictures = None) -> None:
        self.rec = pygame.rect.Rect(x,y,w,h)
        self.pictures = pictures
        self.tic = 0
        self.spin = 0
        self.speed = speed
        self.animations = []
        

    def animation_plus(self,path,number_of_pictures):
        a = []
        for i in range(number_of_pictures):
            a.append(pygame.transform.scale((pygame.image.load(str(path)+str(i+1)+".png")),(self.rec.w,self.rec.h)))
        self.animations.append(a)
    def draw_animation(self,display,nomber_animation,spin):
        self.tic +=1
        if self.tic == self.speed:
            self.tic = 0
            self.spin +=1
        if self.spin > spin:
            self.spin = 0
        display.blit(self.animations[nomber_animation][self.spin],(self.rec.x,self.rec.y))
        
    def forward(self,up,down,right,left,speed_forward):
        if up:
            self.rec.y -= speed_forward
        if down:
            self.rec.y += speed_forward
        if right:
            self.rec.x += speed_forward
        if left:
            self.rec.x -= speed_forward    
       
            
        
        