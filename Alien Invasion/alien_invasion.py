import sys
import pygame
from ship import Ship
from settings import Settings



def run_game():
    pygame.init() #make game
    ai_settings = Settings() #make settings object which has settings
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #make window
    pygame.display.set_caption("Alien Invasion") #title for window
    ship = Ship(screen)
    
    while True: #forever loop for the window
        for event in pygame.event.get(): #wait for user to exit
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        pygame.display.flip() #redraw
    
    
    
run_game()