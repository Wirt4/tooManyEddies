import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.f_speed = 0.25
        self.f_limit = 2
        #laser settings
        self.laser_speed = 2.0
        #will eventually refactor laser to be a graphical pair of beams
        self.laser_color = (255, 0, 0) # want red
        self.laser_capacity = 1
        self.laser_height = 200
        #eddie settings
        self.eddie_drop_speed = 10
        self.eddie_dir = 1
        self.shrink_factor = 0.9
        self.eddie_accelerate = 1.2
        self.laser_accelerate = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #can initialize an event drop rate here

    def initialize_dynamic_settings(self):
        self.eddie_speed = 1.0
        self.eddie_size = pygame.image.load('images/eddie.bmp').get_rect().size
        self.frasier_size = pygame.image.load('images/frasier.bmp').get_rect().size
        self.laser_size = pygame.image.load('images/lasers.bmp').get_rect().size
        self.laser_height = 200
        self.laser_offset = 17
        self.eddie_points= 50


    def increase_speed(self):
        if self.eddie_speed < 0:
            self.eddie_speed /= self.eddie_accelerate
        else:
            self.eddie_speed *= self.eddie_accelerate
        self.laser_speed *= self.laser_accelerate

        self.eddie_size = self._shrink_tuple(self.eddie_size)
        self.frasier_size = self._shrink_tuple(self.frasier_size)
        self.laser_size = self._shrink_tuple(self.frasier_size)
        self.laser_height = self._shrink(self.laser_height)
        self.laser_offset = self._shrink(self.laser_offset)

        self.eddie_points = int(self.eddie_points* self.score_scale)
        #would be great if frasier and his eye lasers got proportionaltely smaller
    def _shrink(self, number):
        return int(number * self.shrink_factor)

    def _shrink_tuple(self, size):
        return (int(size[0] *self.shrink_factor),  int(size[1] * self.shrink_factor))