import sys
import pygame
from bullet import Bullet
from alien import Alien
from stars_background import Star
from random import randint
from time import sleep
from side_bullet import Side_Bullet
from bomb import Bomb
from earth import Earth
import math

def check_keydown_events(event,ai_settings, screen, ship, bullets, side_bullets):
    """Responds to key presses"""
    # Move the ship when arrow key is pressed
    if event.key == pygame.K_RIGHT:
        ship.acw = True
    elif event.key == pygame.K_LEFT:
        ship.cw = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_RETURN:
        fire_side_bullet(ai_settings, screen, ship, side_bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if limit not reached yet.""" 
    # only if remaining bullets left
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def fire_side_bullet(ai_settings, screen, ship, side_bullets):
    """Fires a bullet if limit not reached yet.""" 
    # only if remaining bullets left
    if len(side_bullets) < ai_settings.bullets_allowed:
        new_bullet = Side_Bullet(ai_settings, screen, ship)
        side_bullets.add(new_bullet)

def check_keyup_events(event,ship):
    # STOP the ship when arrow key is pressed
        if event.key == pygame.K_RIGHT:
            ship.acw = False
        elif event.key == pygame.K_LEFT:
            ship.cw = False

def check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens, side_bullets, sb):
    """Responds to keypresses and mouse events"""
    # Watch for keyboard and mouse event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        
        # Move the ship when arrow key is pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets, side_bullets)

        # Stop moving ship when arrow key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
        # Checks mouse click on play button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, bullets, aliens, side_bullets, sb)

def check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, bullets, aliens, side_bullets, sb):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Rest the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide mouse cursor.
        pygame.mouse.set_visible(False)

        # Resets the game stats
        stats.reset_stats()
        stats.game_active = True

        # Resets the scoreboard image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        side_bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship
        
            
def update_bullets(ai_settings, screen, aliens, bullets, ship,sb, stats, side_bullets):
    # Update bullets positions
    bullets.update()
    side_bullets.update()

    # Get rid of bullets that have dissappeared
    for bullet in bullets.copy():
        if bullet.rect.centerx not in range(ai_settings.screen_width) and bullet.rect.centery not in range(ai_settings.screen_height):
            bullets.remove(bullet)
    for sbullet in side_bullets.copy():
        if sbullet.rect.centerx not in range(ai_settings.screen_width) and sbullet.rect.centery not in range(ai_settings.screen_height):
            side_bullets.remove(sbullet)

    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets, sb, stats, side_bullets)
    

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets, sb, stats, side_bullets):
    """Responds to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets,aliens,True, True)
    scollisions = pygame.sprite.groupcollide(side_bullets,aliens,True, True)

    if collisions or scollisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If alien fleet destroy, start new level.
        # Destroy existing bullets, speed up game, and creat new fleet.
        bullets.empty()
        side_bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def update_background(stars):
    stars.update()

def get_number_aliens_x(ai_settings, alien_width):
    # sourcery skip: inline-immediately-returned-variable
    """Determin the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x


def get_number_rows(ai_settings, ship_height,alien_height):
    # sourcery skip: inline-immediately-returned-variable
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = ai_settings.screen_height - (3*alien_height) - ship_height
    number_rows = int(available_space_y / (2* alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number, number_aliens_x):
    """Create an alien and place it in the row"""
    n=0.8
    alienT = Alien(ai_settings, screen, 0, 0,'test')
    alien_radial_width = float(n*360/number_aliens_x)

    w = ai_settings.screen_width
    h = ai_settings.screen_height
    alien_width = alienT.rect.width
    alien_height = alienT.rect.height

    yg = alien_width
    xg = alien_height
    x = ((pow(0.99,2*alien_number)*w*0.2)+w*0.2)*math.cos(alien_radial_width*alien_number*math.pi/180) + (ai_settings.screen_width*0.5)
    y = ((pow(0.99,2*alien_number)*h*0.2)+h*0.2)*math.sin(alien_radial_width*alien_number*math.pi/180) + (ai_settings.screen_height*0.5)
    
    alien = Alien(ai_settings, screen, x , y, alien_number)
    alien.rect.x = x 
    alien.rect.y = y 

    aliens.add(alien)
    
def create_fleet(ai_settings, screen,ship,aliens):
    """Create a full fleet of aliens."""

    # Create an alien and find the number of aliens in a row.
    # Space between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen,0,0,'f')
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    number_rows = 2
    number_aliens_x = 16
    # Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number, number_aliens_x)

def create_star(ai_settings, screen, stars):
    star = Star(ai_settings,screen)
    star.rect.x = randint(0,ai_settings.screen_width)
    star.rect.y = randint(0,int(ai_settings.screen_height*0.8))
    stars.add(star)

def create_stars(ai_settings, screen, stars):
    for _ in range(ai_settings.star_count):
        create_star(ai_settings, screen, stars)



def update_screen(ai_settings, screen, ship, bullets, aliens, stars, play_button, stats, sb, side_bullets, earth):
    
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Redraw all bullets behind ship and aliens
    for sbullet in side_bullets.sprites():
        sbullet.draw_bullet()


    ship.blitme()
    # earth.blitme()
    pygame.draw.circle(screen,(0,0,200),(ai_settings.screen_width//2,ai_settings.screen_height//2),60)
    aliens.draw(screen)

    # Draw the score info
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, side_bullets, sb):
    """Responds ti ship being hit by alien"""
    # Decrement ships left.
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        side_bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause game for 0.5 seconds
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    return True

def check_aliens_bottom(ai_settings, aliens, ship, stats, screen, bullets, side_bullets, sb):
    """Check if fleet hits the ground"""
    screen_rect = screen.get_rect()

    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, side_bullets, sb)
            break
    
def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, side_bullets, sb):
    """Update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for aliens hitting the bottom of the screen    
    # Look for alien-ship collisions.
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, side_bullets, sb)

    # check_aliens_bottom(ai_settings, aliens, ship, stats, screen, bullets, side_bullets, sb)

    

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        alien.check_edges()

def change_fleet_direction(ai_settings, aliens):
    """Drop entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()