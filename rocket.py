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


    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)