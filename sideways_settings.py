class Sideways_Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1.5

        # Bullet settings
        self.sideways_bullet_speed = 2.0
        self.sideways_bullet_width = 15
        self.sideways_bullet_height = 3
        self.sideways_bullet_color = (60, 60, 60)
        self.sideways_bullets_allowed = 3