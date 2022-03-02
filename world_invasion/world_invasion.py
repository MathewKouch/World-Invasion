import pygame
from earth import Earth
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from stars_background import Star
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from side_bullet import Side_Bullet
from bomb import Bomb

def run_game():
    # Initialise game and create a screen object.
    pygame.init()
    
    # Initialize pygame, settings, and screen object.
    ai_settings = Settings('nope  ')
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make the Play button
    play_button = Button(ai_settings, screen, 'Play')

    # Create an instance for game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens
    # Initializing ship on screen
    ship = Ship(ai_settings, screen)
    bullets = Group() 
    aliens = Group()
    stars = Group()
    side_bullets = Group()
    earth = Earth(ai_settings, screen)
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Create stars background
    gf.create_stars(ai_settings,screen,stars)

    # Start the main loop for the game.
    while True:

        # Listening for user inputs
        gf.check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens, side_bullets, sb)
        
        if stats.game_active:
        # Updates ship position
            ship.update()
            # Updates bullets
            gf.update_bullets(ai_settings, screen, aliens, bullets, ship, sb, stats, side_bullets)
            # Update aliens movement
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets, side_bullets, sb)
            
        
        # Draws ships and bullets on screen
        gf.update_screen(ai_settings, screen, ship, bullets, aliens,stars, play_button, stats,sb, side_bullets, earth)
        # print(f'theta: {ship.theta}')#, x: {ship.rect.centerx}, y: {ship.rect.centery}, size:{ship.rect.size}')
        # Update background        
        #gf.update_background(stars)

run_game()
  

