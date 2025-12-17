import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, ai_game):
        """Initialize the rocket's starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.bg_color = (0, 0, 0)

        # Load the rocket's image
        self.image = pygame.image.load("images/rocket.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Place Rocket at the center.
        self.rect.center = self.screen_rect.center

        # Get float value for x-position of rocket
        self.x = float(self.rect.x)

        # Get float value for x-position of rocket
        self.y = float(self.rect.y)

        # Initial movement status of ship at x axis
        self.moving_right = False
        self.moving_left = False

        # Initial movement status of ship at y axis
        self.moving_top = False
        self.moving_bottom = False


    def update_x_axis(self):
        """Update the rocket's x-axis location based on the movement flag."""

        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update self.rect from self.x
        self.rect.x = self.x


    def update_y_axis(self):
        """Update the rocket's y-axis location based on the movement flag."""
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
            
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update self.rect from self.y
        self.rect.y = self.y


    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)