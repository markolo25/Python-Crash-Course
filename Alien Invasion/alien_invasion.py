import sys
import pygame



def run_game():
    pygame.init() #make game
    screen = pygame.display.set_mode((1200,800)) #make window
    pygame.display.set_caption("Alien Invasion") #title for window
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        pygame.display.flip()
    
    
    
run_game()