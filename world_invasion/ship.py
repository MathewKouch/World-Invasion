 # required to obtain rect dimensions of screen and rocket image
import pygame
from pygame.sprite import Sprite
import math

SHIP_SIZE = {'rectangle':(64/2,128//2),'square':(70,70),'square-sm':(35,35),'square-xsm':(20,20)} 
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        
        self.SHIP_SIZE = {'rectangle':(64/2,128//2),'square':(70,70)} 
        """Initialise the ship and its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('./images/orange_space_ship.png')
        self.image = pygame.transform.scale(self.image,SHIP_SIZE['square-xsm'])
        self.rect = self.image.get_rect() # gets rect dim of image
        self.screen_rect = screen.get_rect()

        # starting angle is 90 degrees, most closest position to bottom of screen. theta between [-180,180) 
        self.theta = 270.0
        self.theta_ship = 0.0

        self.r =  self.ai_settings.world_radius
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.centery = self.screen_rect.centery - self.r
    
        # Stores a decimal value of the ship's center.
        self.x = float(self.rect.centerx) 
        self.y = float(self.rect.centery)
        # Movement flag
        self.acw = False # anticlockwise
        self.cw = False # clockwise

        # Movement flag
        self.rot_right = False
        self.rot_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.acw:

            self.theta -= self.ai_settings.ship_speed
            self.theta %= 360


            self.x = math.cos(self.theta*math.pi/180)*self.r + self.screen_rect.centerx
            self.y = math.sin(self.theta*math.pi/180)*self.r + self.screen_rect.centery
            # self.image = pygame.transform.rotate(self.image,1)

        if self.cw:
            
            self.theta += self.ai_settings.ship_speed
            self.theta %= 360

            self.x = math.cos(self.theta*math.pi/180)*self.r + self.screen_rect.centerx
            self.y = math.sin(self.theta*math.pi/180)*self.r + self.screen_rect.centery
            # self.image = pygame.transform.rotate(self.image,-1)

        if self.theta%5==0:
          
            if self.acw:
                self.image = pygame.image.load('./images/orange_space_ship.png')
                self.image = pygame.transform.scale(self.image,SHIP_SIZE['square-xsm'])
                self.image = pygame.transform.rotate(self.image,0)
                self.image = pygame.transform.rotate(self.image,-(self.theta-270))
            if self.cw:
                self.image = pygame.image.load('./images/orange_space_ship.png')
                self.image = pygame.transform.scale(self.image,SHIP_SIZE['square-xsm'])
                self.image = pygame.transform.rotate(self.image,0)
                self.image = pygame.transform.rotate(self.image,-(self.theta-270))

        """Update ships orientation based on the rotation flag"""
        # if self.rot_right and self.rect.top<self.screen_rect.height:
        # self.image = pygame.image.load('./images/orange_space_ship.png')
        # self.image = pygame.transform.scale(self.image,SHIP_SIZE['square-sm'])
        # self.image = pygame.transform.rotate(self.image,-(self.theta-270))

        self.rect.centerx = float(self.x)
        self.rect.centery = float(self.y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on screen"""
        
        # self.centerx = self.screen_rect.centerx
        # self.centery = self.screen_rect.centery - self.r
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.centery = self.screen_rect.centery - self.r