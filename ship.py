import pygame


class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its stating position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship-retro.bmp')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = self.rect.x

        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag"""
        # if self.moving_right:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.x += self.settings.ship_speed
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # self.rect.x -= self.settings.ship_speed
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
