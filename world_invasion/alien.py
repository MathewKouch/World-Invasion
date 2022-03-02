import pygame
from pygame.sprite import Sprite
import math

SHIP_SIZE = (64,32)
SHIP_SIZE_SM = (50,25)


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen,posx, posy,n):
        """Initiliazes the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.posx = posx
        self.posy = posy
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('./images/alien_purple.png')
        self.image = pygame.transform.scale(self.image,SHIP_SIZE_SM)
        self.rect =  self.image.get_rect()

        # Start each new alien near the top of the screen.
        self.rect.x = posx + self.ai_settings.screen_width//2
        self.rect.y = posy + self.ai_settings.screen_height//2

        # Distance to middle
        self.x = float((self.ai_settings.screen_width//2) - self.posx)
        self.y = float((self.ai_settings.screen_height//2) - self.posy)

        self.dx = float(self.x*ai_settings.alien_speed_factor*0.0005)
        self.dy = float(self.y*ai_settings.alien_speed_factor*0.0005)


    def check_edges(self):
        # """Return True if alien is at edge of screen"""
        if (
            self.rect.centerx > self.ai_settings.screen_width
            or self.rect.centerx < 0
        ) or (
            self.rect.centery > self.ai_settings.screen_height
            or self.rect.centery < 0
        ):
            # If at edge, bounce back in 
            self.dx *= -1
            self.dy *= -1

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right"""
    
        self.x -= self.dx*self.ai_settings.alien_speed_factor
        self.y -= self.dy*self.ai_settings.alien_speed_factor

        self.rect.x = self.x + self.ai_settings.screen_width//2
        self.rect.y = self.y + self.ai_settings.screen_height//2
