import sys
import pygame
from settings import Settings
from frasier import Frasier
from laser import Laser
from eddie import Eddie

class TooManyEddies:
    'overall class to manage assets and behavior'
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Too Many Eddies")
        self.frasier = Frasier(self)
        self.lasers = pygame.sprite.Group()
        self.eddies = pygame.sprite.Group()
        self._create_horde()

    def _create_horde(self):
        eddie = Eddie(self)
        eddie_width, eddie_height = eddie.rect.size #eddie is a square
        fras_height = self.frasier.rect.height
        available_space_x = self.settings.screen_width - (2 * eddie_width)
        available_space_y = self.settings.screen_height - (3 * eddie_height) - fras_height
        num_rows = available_space_y//(2 * eddie_height)
        num_eddies_x = available_space_x//(2 * eddie_width)
        for j in range(num_rows):
            for i in range(num_eddies_x):
                self._create_eddie(j, i)

    def _create_eddie(self, row_num, eddie_num):
        eddie = Eddie(self)
        eddie_width, eddie_height = eddie.rect.size
        eddie.x = eddie_width + (2 * eddie_width * eddie_num)
        eddie.rect.y = eddie.rect.height + (2 * eddie.rect.height * row_num)
        eddie.rect.x = eddie.x
        self.eddies.add(eddie)

    def _fire_laser(self):
        if len(self.lasers)<self.settings.laser_capacity:
            new_laser = Laser(self)
            self.lasers.add(new_laser)

    def check_keydown_events(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
            self._fire_laser()
        elif event.key == pygame.K_RIGHT:
            self.frasier.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.frasier.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
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
        """Draws Frasier and the background"""
        self.screen.fill(self.settings.bg_color)
        self.frasier.blitme()
        self.eddies.draw(self.screen)
        for laser in self.lasers.sprites():
            laser.draw_laser()
        pygame.display.flip()

    def _check_horde_edges(self):
        """respond correctly if eddies have reached an edge"""
        for eddie in self.eddies.sprites():
            if eddie.at_edge():
                self._switch_horde_direction()
                break

    def _switch_horde_direction(self):
        for eddie in self.eddies.sprites():
            eddie.rect.y += self.settings.eddie_drop_speed
        self.settings.eddie_dir *= -1

    def run_game(self):
        """primary game loop"""
        while True:
            self.check_events()
            self.frasier.update()
            self.update_screen()
            self.lasers.update()
            self.update_lasers()
            self.update_eddies()

    def update_eddies(self):
        """checks if eddie horde hits edge of screen, then updates position of all eddies"""
        self._check_horde_edges()
        self.eddies.update()

    def update_lasers(self):
        """removes lasers if off of screen"""
        for laser in self.lasers.copy():
            if laser.rect_1.bottom <= 0:
                self.lasers.remove(laser)

if __name__ =='__main__':
    tme = TooManyEddies()
    tme.run_game()
