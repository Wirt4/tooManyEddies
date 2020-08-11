import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.f_speed = 0.25
        self.f_limit = 2
        #laser settings
        self.laser_speed = 2.0
        #will eventually refactor laser to be a graphical pair of beams
        self.laser_color = (255, 0, 0) # want red
        self.laser_capacity = 2
        self.f_eye1 = 60
        #eddie settings
        self.eddie_speed = 2.0
        self.eddie_drop_speed = 10
        self.eddie_dir = 1
        self.shrink_factor = 0.9
        self.accelerate = 1.1
        self.initialize_dynamic_settings()
        #can initialize an event drop rate here

    def initialize_dynamic_settings(self):
        self.eddie_speed = 0.07
        self.eddie_size = pygame.image.load('images/eddie.bmp').get_rect().size


    def increase_speed(self):
        if self.eddie_speed < 0:
            self.eddie_speed /= self.accelerate
        else:
            self.eddie_speed *= self.accelerate
        #self.laser_speed *= self.accelerate
        self.eddie_size = (int(self.eddie_size[0] *self.shrink_factor),  int(self.eddie_size[1] * self.shrink_factor))
        #would be great if frasier and his eye lasers got proportionaltely smaller