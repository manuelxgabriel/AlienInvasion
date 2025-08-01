#!/usr/bin/env python3

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Response to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
            print(f'[{self.ship.rect.x}, 0]')
        if event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
            print(f'[{self.ship.rect.x}, 0]')
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        """Respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip the new screen"""
        # Redraw the screen during each pass through the loop
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image, (0, 0))

        # Display the ship
        self.ship.blitme()

        # Make the most recent drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # Make the game instance, run the game.
    ai = AlienInvasion()
    ai.run_game()
