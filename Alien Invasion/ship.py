import pygame

class Ship():
    
    def __init__(self, screen):
        self.screen = screen
    
        #load image to a rectangle
        self.image = pygame.image.load('images/ship.png')
        w,h = self.image.get_size()
        scale = .15
        self.image = pygame.transform.scale(self.image, (int(w * scale), int(h * scale)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        #place rectnagle at center bottom screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        #draw ship
        self.screen.blit(self.image, self.rect)
    
    
