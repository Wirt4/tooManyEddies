import pygame
from pygame.sprite import Sprite


class Laser(Sprite):

    def __init__(self, tme_game):
        super().__init__()
        self.screen = tme_game.screen
        self.settings = tme_game.settings
        self.color = self.settings.laser_color
        self.rect_1 = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        #TODO: should lasers be two sepearate objects or a bullet bmp on a transparency ?
        self.rect_1.midtop =(tme_game.frasier.rect.centerx, tme_game.screen.get_rect().height - self.settings.f_eye1)
        self.y = float(self.rect_1.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect_1.y = self.y

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect_1)