#! /usr/bin/env python3

import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion: 
    '''Overall class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game, and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height)) #Display settings
        pygame.display.set_caption("Alien Invasion") #Game Caption
        
        self.ship = Ship(self)

    def check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            self.check_events()
            #Watch for keyboard and mouse events
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()            