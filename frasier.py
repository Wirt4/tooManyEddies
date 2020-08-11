import pygame
from pygame.sprite import Sprite

class Frasier:
    def __init__(self, tme_game):
        self.screen = tme_game.screen
        self.screen_rect = tme_game.screen.get_rect()
        #self.image = pygame.image.load('images/frasier_4.bmp')
        self.image = pygame.image.load('images/frasier.bmp') #greyboxing
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = tme_game.settings
        self.x = float(self.rect.x)

    def update(self):
        self.x = pygame.mouse.get_pos()[0]
        if self.x < self.settings.screen_width - self.rect.width:
            self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    #TODO: write "center_frasier() method
    def center_frasier(self):
        """Centers frasier on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)