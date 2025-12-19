import pygame

class Sideways_Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.sideways_settings = ai_game.sideways_settings
        self.screen_rect = ai_game.screen.get_rect()
        self.bg_color = (0, 0, 0)

        # Load the ship image & get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft 

        # Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.moving_top = False
        self.moving_bottom = False


    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the ship's y value, not the rect.
        if self.moving_top and self.rect.top > 0:
            self.y -= self.sideways_settings.ship_speed
            
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.sideways_settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)