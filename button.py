import pygame.font
import random

class Button:

    def __init__(self, tme_game):
        """intialize all button attributes"""
        self.screen = tme_game.screen
        self.settings = tme_game.settings
        self.screen_rect = self.screen.get_rect()
        self.button_color = self.settings.bg_color
        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(self.settings.font, self.settings.score_font_size)
        self.rect = pygame.Rect(0, 0, self.screen_rect.width, self.screen_rect.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(random.choice(self.settings.button_messages).upper())

    def _prep_msg(self, msg):
        """turns msg into renderd screen image, centers text on button"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

    #might like a fade-out function here, can call when is clicked