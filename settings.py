import pygame
import sys
import os
class Settings:
    def __init__(self):
        self.screen_width = 1536
        self.screen_height = 864
        self.bg_color = (0, 0, 0)
        self.f_speed = 0.25
        self.f_limit = 2
        #will eventually refactor laser to be a graphical pair of beams
        self.laser_color = (255, 0, 0) # want red
        self.laser_capacity = 3
        self.laser_height = 200
        #eddie settings
        self.eddie_drop_speed = 10
        self.eddie_dir = 1
        self.shrink_factor = 0.9
        self.eddie_accelerate = 1.2
        self.laser_accelerate = 1.1
        self.score_scale = 1.5
        self.image_folder_path = self.initialize_path()
        self.initialize_dynamic_settings()
        #can initialize an event drop rate here
        #self.font ="Times New Roman"
        self.font = "Times New Roman"
        self.score_font_size = 48
        self.text_color = (255, 255, 255)

        self.icon_size = (40, 40)
        self.icon_margin = 10
        self.button_messages = ["PERSIAN RUG, WE HARDLY KNEW YE", "NO, BAD EDDIE", "NO, BAD FRASIER", "Apotheosis",
                                "Send in the hounds", "A most unusual talent", "It's from his mother's side",
                                "Jack Russell terror", "les chiens de l’enfer ", "The ultimate space invader",
                                "Many Eddies", "dog :1, man: 0", "Charybdis", "What until you see his ears",
                                "Where is your god now?", "Tossed Salads and Scrambled Eddies", ]


    def _get_img_size(self, img_name):
        img = pygame.image.load(os.path.join(self.image_folder_path, img_name))
        return img.get_rect().size

    def initialize_dynamic_settings(self):
        self.eddie_speed = 2.0
        self.eddie_size = self._get_img_size('eddie.bmp')
        self.frasier_size = self._get_img_size('frasier.bmp')
        self.laser_size = self._get_img_size('lasers.bmp')
        self.laser_height = 200
        self.laser_offset = 17
        self.eddie_points= 50
        self.laser_speed = 2.0

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

    def speed_shift_up(self):
        self.f_speed *= 2
        self.eddie_drop_speed *= 2
        self.eddie_speed *= 2
        self.laser_speed *= 2

    def speed_shift_down(self):
        self.f_speed /= 2
        self.eddie_drop_speed /= 2
        self.eddie_speed /= 2
        self.laser_speed /= 2

    def initialize_path(self):
        if getattr(sys, 'frozen', False):
            CurrentPath = sys._MEIPASS
        else:
            CurrentPath = os.path.dirname(__file__)
        return  os.path.join(CurrentPath, 'images')

