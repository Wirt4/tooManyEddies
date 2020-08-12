import pygame
from pygame.sprite import Sprite

class Frasier(Sprite):
    def __init__(self, tme_game, size):
        super().__init__()
        self.screen = tme_game.screen
        self.screen_rect = tme_game.screen.get_rect()
        self.image = pygame.image.load('images/frasier.bmp')
        self.settings = tme_game.settings
        self.update_size(size)

    def update(self):
        """Updates Frasier's position, he basically tracks to the mouse"""
        self.x = pygame.mouse.get_pos()[0]
        if self.x < self.screen_rect.size[0] - self.rect.size[0]:
            self.rect.x = self.x

    def blitme(self):
        """draws frasier"""
        self.screen.blit(self.image, self.rect)

    def update_size(self, size):
        """shrinks frasier"""
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
