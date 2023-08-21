import pygame

class Area():
    def __init__(self, window, x, y, width, height, color,picture = None):
        self.rec = pygame.Rect(x, y, width, height)
        self.color =color
        self.window = window
        self.x_width = x + width
        self.x_height = y + height
        self.picture = picture
    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rec)
    
    def draw_picture(self):
        self.window.blit(self.picture,(self.rec.x,self.rec.y))
    
    def set_text(self, text):
        f = pygame.font.Font(None, 30)
        self.text = f.render(text, True, (255,215,0))
        self.window.blit(self.text , (self.rec.x , self.rec.y))
    
    def touch(self,enemi):
        return pygame.Rect.colliderect( self.rec,enemi.rec) 
    
    
    