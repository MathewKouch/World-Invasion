class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self, phase=None):
        """Initialize the game's settings."""
        color= {'sky blue':(201,233,246),'black':(0,0,0),'pink':(235,135,206),
                'orange':(255,165,0),'midnight purple':(46,27,71),'fluoro blue':(8, 39, 245)}

        if phase != 'test':
            # Screen settings
            self.screen_width = 1200
            self.screen_height = 800
            self.bg_color = color['midnight purple']

            # Ship settings
            self.ship_speed = 2
            self.ship_limit = 3 # number of lives

            # Bullet settings
            self.bullet_width = 16
            self.bullet_height = 16
            self.bullet_color = color['orange']
            self.bullets_allowed = 20
            self.side_bullet_color = color['pink']
            self.bomb_color = color['fluoro blue']
            self.bomb_radius = 6

            # Alien settings
            self.fleet_drop_speed = 10
            # fleet direction of 1 represetns right; -1 represents left.
            self.fleet_direction = 1
            
            # Star background settings
            self.star_count = 50
            self.star_speed = 0.5
        
        else:
            # Screen settings
            self.screen_width = 1200
            self.screen_height = 800
            self.bg_color = color['midnight purple']

            # Ship settings
            self.ship_speed = 1
            self.ship_limit = 2

            # Bullet settings
            self.bullet_speed_factor = 10
            self.bullet_width = 6
            self.bullet_height = 6
            self.bullet_color = color['orange']
            self.bullets_allowed = 3

            # Alien settings
            self.alien_speed_factor = 3
            self.fleet_drop_speed = 100
            # fleet direction of 1 represetns right; -1 represents left.
            self.fleet_direction = 1
            
            # Star background settings
            self.star_count = 200
            self.star_speed = 0.5
        
        # How quickly the game speeds up
        self.speedup_scale = 1.05

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed_factor = 32
        self.bomb_speed_factor = 1.5
        self.alien_speed_factor = 1

        self.world_radius = 70
        # fleet direction of 1 represetns right; -1 represents left.
        self.fleet_direction = 1
    
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale