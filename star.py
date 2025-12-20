import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, ai_game):
        """Initialize a star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star's image and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)