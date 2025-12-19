import sys

import pygame
from sideways_settings import Sideways_Settings
from sideways_shooter_ship import Sideways_Ship
from sideways_bullet import Sideways_Bullet

class Sideways_Invasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.sideways_settings = Sideways_Settings()

        self.screen = pygame.display.set_mode((0, 0),
                                              pygame.FULLSCREEN)
        self.sideways_settings.screen_width = self.screen.get_rect().width
        self.sideways_settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.sideways_ship = Sideways_Ship(self)
        self.sideways_bullets = pygame.sprite.Group()


    def run_game(self):
            """Start the main loop for the game"""
            while True:
                self._check_events()
                self.sideways_ship.update()
                self._update_bullets()
                self._update_screen()
                self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses & mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)


            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.sideways_ship.moving_top = True


        elif event.key == pygame.K_DOWN:
            self.sideways_ship.moving_bottom = True


        elif event.key == pygame.K_q:
            sys.exit()


        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _fire_bullet(self):
        """Create a new bullet & add it to the bullets group."""
        if len(self.sideways_bullets) < (self.sideways_settings.sideways_bullets_allowed):
            new_sideways_bullet = Sideways_Bullet(self)
            self.sideways_bullets.add(new_sideways_bullet)


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.sideways_ship.moving_top = False


        elif event.key == pygame.K_DOWN:
            self.sideways_ship.moving_bottom = False


    def _update_bullets(self):
        """Update the position of bullets & get rid of old ones"""
        # Update bullet positions.
        self.sideways_bullets.update()

        # Get rid of bullets that have disappeared.
        for sideways_bullet in self.sideways_bullets.copy():
            if sideways_bullet.rect.left >= self.sideways_settings.screen_width:
                self.sideways_bullets.remove(sideways_bullet)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.sideways_settings.bg_color)

        for sideways_bullet in self.sideways_bullets.sprites():
            sideways_bullet.draw_bullet()

        self.sideways_ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = Sideways_Invasion()
    ai.run_game()