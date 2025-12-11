import pygame

class Character:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the character & her starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image & get its rect.
        self.image = pygame.image.load("images/female_bard.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    
    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)