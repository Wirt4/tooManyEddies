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