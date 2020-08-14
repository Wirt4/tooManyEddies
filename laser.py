import pygame
from pygame.sprite import Sprite
import os

class Laser(Sprite):

    def __init__(self, tme_game, size):
        """initialize laser members"""
        super().__init__()
        self.screen = tme_game.screen
        self.settings = tme_game.settings
        #self.image = pygame.image.load('images/lasers.bmp')
        self.image = pygame.image.load(os.path.join(self.settings.image_folder_path, 'lasers.bmp'))
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect.midtop = (tme_game.frasier.rect.centerx - self.settings.laser_offset,
                           tme_game.screen.get_rect().height-self.settings.laser_height)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y

    def draw_laser(self):
        self.screen.blit(self.image, self.rect)
