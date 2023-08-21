import pygame


class Menu:
    def __init__(self,display,font = None,type = 30,color_text = (255,255,255)):
        self.text = []
        self.text_rect = []
        self.font = pygame.font.Font(font, type)
        self.color_text = color_text
        self.display = display
        self.nomber_menu = -1
    
    def create_button(self,text = "", rect = (0,0,0,0)):
        text1 = self.font.render(text, True, self.color_text)
        rec = pygame.Rect(rect)
        rec2 = text1.get_rect()
        self.text.append(text1)
        self.text_rect.append(pygame.Rect(rec.x,rec.y,rec2.w,rec2.h))  
    
    def create_button2(self,pictures, rect = (0,0,0,0)):
        text1 = pygame.transform.scale(pictures,(rect[2],rect[3]))
        rec = pygame.Rect(rect)
        self.text.append(text1)
        self.text_rect.append(pygame.Rect(rec.x,rec.y,rec.w,rec.h))  
        
    def select(self):
        x,y= pygame.mouse.get_pos()
        for i in range(len(self.text)):
            if pygame.Rect.collidepoint(self.text_rect[i],(x,y))  :
                self.nomber_menu = i
                return i
            
    def draw_menu (self,color_rec = (-1,-1,-1)):
        for i in range(len(self.text)):
            if self.nomber_menu != -1 :
                
                pygame.draw.rect(self.display,color_rec,self.text_rect[self.nomber_menu])
            self.nomber_menu = -1 
            self.display.blit(self.text[i] , (self.text_rect[i].x , self.text_rect[i].y))
            

            

        
                     
        
        
          
        
    
    
        
        
        
        


