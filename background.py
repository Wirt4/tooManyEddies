"a way to get the apartment into the game"
import pygame

from pygame.sprite import Sprite


class Background(Sprite):

    def __init__(self, tme_game):
        super().__init__()
        self.screen = tme_game.screen
        self.image = pygame.image.load('images/apartment.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.settings = tme_game.settings

    def blitme(self):
        self.screen.blit(self.image, self.rect)