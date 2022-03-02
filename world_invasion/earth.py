import pygame
from random import randint
from pygame.sprite import Sprite


class Earth(Sprite):
    def __init__(self, ai_settings, screen):
        super(Earth, self).__init__()
        """Initialise star background"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load a star image
        self.image = pygame.image.load('./images/earth.png')
        self.image = pygame.transform.scale(self.image,(90,68))
        self.rect = self.image.get_rect() # gets rect dim of image
        self.screen_rect = screen.get_rect()

        # Start each star at top left corner with one width and heigth away
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """"Draw star on screen"""
        self.screen.blit(self.image, self.rect)
    
    # def draw_star(self):
    #     """Draw star """
    #     self.screen.blit(self.image, self.rect)

