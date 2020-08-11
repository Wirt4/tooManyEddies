import pygame
from pygame.sprite import Sprite


class Laser(Sprite):

    def __init__(self, tme_game):
        super().__init__()
        self.screen = tme_game.screen
        self.settings = tme_game.settings
        self.color = self.settings.laser_color
        #self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self.image = pygame.image.load('images/lasers.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.midtop =(tme_game.frasier.rect.centerx - 17, tme_game.screen.get_rect().height-200)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y

    def draw_laser(self):
        self.screen.blit(self.image, self.rect)