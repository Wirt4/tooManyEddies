import sys
import pygame
from settings import Settings
from frasier import Frasier

class TooManyEddies:
    'overall class to manage assets and behavior'
    def __init__(self):
        pygame.init()
        self.settings = Settings()
       # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Too Many Eddies")
        self.frasier = Frasier(self)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.frasier.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.frasier.moving_left = True
        elif event.key == pygame.K_q or pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.frasier.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.frasier.moving_left = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.frasier.blitme()
        pygame.display.flip()

    def run_game(self):
        #primary game loop
        while True:
            self.check_events()
            self.frasier.update()
            self.update_screen()

if __name__ =='__main__':
    tme = TooManyEddies()
    tme.run_game()