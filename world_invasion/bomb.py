from bullet import Bullet
import pygame

class Bomb(Bullet):
    """A rocket propelled bomb with large blast coverage"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__(ai_settings, screen, ship)
         # Create a bullet rect at (0,0) and then set correct position.
        self.ai_settings = ai_settings
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top =  ship.rect.centery

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.bomb_radius = ai_settings.bomb_radius

        self.color = ai_settings.bomb_color
        self.speed_factor = ai_settings.bullet_speed_factor*ai_settings.bomb_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        if self.rect.y < 0.5*self.ai_settings.screen_height:
            self.bomb_explosion()


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def bomb_explosion(self):
        # Bomb explodes to a square until alien hits...
        
        bombx = self.x-(self.bomb_radius//2)
        bomby = self.y-(self.bomb_radius//2)
        # self.rect = pygame.Rect(bombx, bomby, self.bomb_radius, self.bomb_radius)
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.rect = pygame.draw.circle(self.screen, self.color, (bombx,bomby), self.bomb_radius, 0)
