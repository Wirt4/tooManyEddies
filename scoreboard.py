import pygame
from pygame.sprite import Group
from frasier import Frasier


class Scoreboard:

    def __init__(self, tme_game):
        """inistializes members for score"""
        self.tme_game = tme_game
        self.screen = tme_game.screen
        self.screen_rect = tme_game.screen.get_rect()
        self.settings = tme_game.settings
        self.stats = tme_game.stats
        #font settings
        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(self.settings.font, self.settings.score_font_size)
        #set initial score image
        self.prep_score()
        #self.prep_high_score()
        self.prep_level()
        self.prep_frasiers()
        self.prep_q_msg()

    def prep_frasiers(self):
        """creates a row of tiny frasier heads to show how many lives are left"""
        self.frasiers = Group()
        for frasier_num in range(self.stats.frasiers_left):
            frasier = Frasier(self.tme_game, self.settings.icon_size)
            frasier.rect.x = self.settings.icon_margin + frasier_num * frasier.rect.width
            frasier.rect.y = self.settings.icon_margin
            self.frasiers.add(frasier)

    # def prep_high_score(self):
    #     """turns high score into rendered image"""
    #     high_score = round(self.stats.high_score, -1)
    #     high_score_str = "High Score: " + "{:,}".format(high_score)
    #     self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
    #     self.high_score_rect = self.high_score_image.get_rect()
    #     self.high_score_rect.centerx = self.screen_rect.centerx
    #     self.high_score_rect.top = self.score_rect.top

    def prep_q_msg(self):
        """creates a rendered quit message"""
        q_msg = "press 'q' to quit"
        self.q_msg_img = self.font.render(q_msg, True, self.text_color, self.settings.bg_color)
        self.q_msg_rect =self.q_msg_img.get_rect()
        self.q_msg_rect.left = self.screen_rect.left
        self.q_msg_rect.bottom = self.screen_rect.bottom

    def prep_score(self):
        """creates a rendered score from data"""
        rounded_score = round(self.stats.score, -1)
        score_str = "Current Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """draws rendered score and lives on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        #self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.frasiers.draw(self.screen)
        self.screen.blit(self.q_msg_img, self.q_msg_rect)

    # def check_high_score(self):
    #     """see if there's a new high score"""
    #     if self.stats.score > self.stats.high_score:
    #         self.stats.high_score = self.stats.score
    #         self.prep_high_score()

    def prep_level(self):
        """turn level into rendered image"""
        level_str = "Level " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + self.settings.icon_margin