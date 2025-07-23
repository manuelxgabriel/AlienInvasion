import pygame


class Settings:
    """Class that stores all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen setting
        self.screen_width = 600
        self.screen_height = 400
        # self.bg_color = "#000000"
        self.bg_image = pygame.image.load('images/space-background.bmp')
        self.bg_image = pygame.transform.scale(self.bg_image, (1200, 800))
        self.ship_speed = 1.5


