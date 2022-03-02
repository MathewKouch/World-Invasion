from bullet import Bullet
import pygame

class Side_Bullet(Bullet):
    """Bullet that shoots from the side of the ship, moving along x direction"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__(ai_settings, screen, ship)
    # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0,ai_settings.bullet_height, ai_settings.bullet_width)
        self.rect.centerx = ship.rect.centerx
        self.rect.top =  ship.rect.centery

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
        self.color = ai_settings.side_bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
