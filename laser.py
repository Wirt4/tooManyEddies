import pygame
from pygame.sprite import Sprite


class Laser(Sprite):

    def __init__(self, tme_game):
        super().__init__()
        self.screen = tme_game.screen
        self.settings = tme_game.settings
        self.color = self.settings.laser_color
        self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self._layer = self.rect.bottom
        #sprites.add(self, layer=self.layer)

        #self.rect.midtop = (tme_game.frasier.rect.midtop)
        self.rect.midtop =(tme_game.frasier.rect.centerx, tme_game.screen.get_rect().height - self.settings.f_eye1)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)