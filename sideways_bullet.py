import pygame
from pygame.sprite import Sprite

class Sideways_Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.sideways_settings = ai_game.sideways_settings
        self.color = self.sideways_settings.sideways_bullet_color

        # Create a bullet rect at (0, 0) & then set correct position.
        self.rect = pygame.Rect(0, 0, self.sideways_settings.sideways_bullet_width,
                                self.sideways_settings.sideways_bullet_height)
        # Start the bullet at the ship's right middle and track its x position.
        self.rect.midright = ai_game.sideways_ship.rect.midright

        # Store the bullet's position as a float (x coordinate).
        self.x = float(self.rect.x)

    
    def update(self):
        """Move the bullet right across the screen."""
        # Update the exact position of the bullet.
        self.x += self.sideways_settings.sideways_bullet_speed

        # Update the rect position.
        self.rect.x = self.x


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)