import pygame
from random import randint
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        """Initialise star background"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load a star image
        self.image = pygame.image.load('./images/star.png')
        self.image = pygame.transform.scale(self.image,(8,8))
        self.rect = self.image.get_rect() # gets rect dim of image
        self.screen_rect = screen.get_rect()

        self.image_earth = pygame.image.load('./images/earth.png')
        self.image_earth = pygame.transform.scale(self.image,(90,68))
        self.image_earth_rect = self.image_earth.get_rect() # gets rect dim of image

        self.image_earth_rect.center = self.screen_rect.center

        # Start each star at top left corner with one width and heigth away
        self.rect.x = randint(0,self.screen_rect.width)
        self.rect.y = self.screen_rect.height-100

        self.x = float(self.rect.x)
        self.speed_factor = ai_settings.star_speed

    def update(self):
        """Move the stars from right to left"""
        self.x = (self.x-self.speed_factor) % self.ai_settings.screen_width
        self.rect.x = self.x

    def blitme(self):
        """"Draw star on screen"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image_earth, self.image_earth_rect)
    # def draw_star(self):
    #     """Draw star """
    #     self.screen.blit(self.image, self.rect)

