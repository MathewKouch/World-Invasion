import pygame
from pygame.sprite import Sprite
import math

class Bullet(Sprite):
    """A class to manage bulles fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship'current postion."""
        super(Bullet, self).__init__() #inherit properties from Sprite
        self.screen = screen

        # Create a bullet rect at (0,0) and then set correct position.
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect = pygame.Rect(0, 0, 50,50)
        self.theta = ship.theta
        self.rect.center = ship.rect.center
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""

        # Update the decima position of the bullet.
        self.y += self.speed_factor*math.sin(self.theta*math.pi/180)
        self.x += self.speed_factor*math.cos(self.theta*math.pi/180)
        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullets to the screen."""
        # Rectangular bullets
        # pygame.draw.rect(self.screen, self.color, self.rect)
        # Draws circular bullets
        pygame.draw.circle(self.screen,(223,45,8),self.rect.center,100)

