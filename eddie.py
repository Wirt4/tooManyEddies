import pygame
from pygame.sprite import Sprite
import os


class Eddie(Sprite):
    """initilizes an eddie sprite, size is a tuple"""

    def __init__(self, tme_game, size):
        super().__init__()
        self.settings = tme_game.settings
        self.screen = tme_game.screen
        self.image = pygame.image.load(os.path.join(self.settings.image_folder_path, 'eddie.bmp'))
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        """Move Eddie right or left"""
        self.x += self.settings.eddie_speed * self.settings.eddie_dir
        self.rect.x = self.x

    def at_edge(self):
        """return True if eddie is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
