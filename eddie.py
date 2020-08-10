import pygame
from pygame.sprite import Sprite

class Eddie(Sprite):
    def __init__(self, tme_game):
        super().__init__()
        self.screen = tme_game.screen
        self.image = pygame.image.load('images/eddie.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings = tme_game.settings

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
