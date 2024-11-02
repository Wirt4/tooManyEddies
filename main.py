import sys
import pygame
from settings import Settings
from frasier import Frasier
from laser import Laser
from eddie import Eddie
from stats import Stats
from time import sleep
from button import Button
from scoreboard import Scoreboard
import random

class TooManyEddies:
    """overall class to manage assets and behavior"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_size = self.screen.get_rect().size
        pygame.display.set_caption("Too Many Eddies: A Frasier Parody")

        self.stats = Stats(self)
        self.frasier = Frasier(self, self.settings.frasier_size)
        self.lasers = pygame.sprite.Group()
        self.eddies = pygame.sprite.Group()
        self._create_horde()
        self.play_button = Button(self, random.choice(self.settings.button_messages))
        self.pause_button = Button(self, "paused")
        self.title_button = Button(self, random.choice(self.settings.button_messages))
        self.scoreboard = Scoreboard(self)
        self.paused = False
        self.title_card = False

    def _start_level(self):
        self.lasers.empty()
        self._create_horde()
        self.frasier.update_size(self.settings.frasier_size)
        self.scoreboard.prep_level()
        self.scoreboard.prep_frasiers()

    def _frasier_hit(self):
        if self.stats.frasiers_left > 0:
            self.stats.frasiers_left -= 1
            self.eddies.empty()
            self._start_level()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            sleep(5)
            self.frasier = Frasier(self, self.settings.frasier_size)

    def _create_horde(self):
        eddie = Eddie(self, self.settings.eddie_size)
        eddie_width, eddie_height = eddie.rect.size
        fras_height = self.frasier.rect.height
        available_space_x = self.screen_size[0] - (2 * eddie_width)
        available_space_y = self.screen_size[1] - (2 * eddie_height) - fras_height
        num_rows = available_space_y//(2 * eddie_height)
        num_eddies_x = available_space_x//(2 * eddie_width)
        for j in range(num_rows):
            for i in range(num_eddies_x):
                self._create_eddie(j, i)

    def _create_eddie(self, row_num, eddie_num):
        eddie = Eddie(self, self.settings.eddie_size)
        eddie_width, eddie_height = eddie.rect.size
        eddie.x = eddie_width + (2 * eddie_width * eddie_num)
        eddie.rect.y = eddie.rect.height + (2 * eddie.rect.height * row_num)
        eddie.rect.x = eddie.x
        self.eddies.add(eddie)

    def _fire_laser(self):
        if len(self.lasers) < self.settings.laser_capacity and not self.paused:
            new_laser = Laser(self, self.settings.laser_size)
            self.lasers.add(new_laser)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._fire_laser()
            elif event.type == pygame.KEYDOWN:
                    self._const_events(event)

    def _check_play_button(self, mouse_pos):
        """starts a new game when player clicks button"""
        clicked = self.play_button.rect.collidepoint(mouse_pos)
        if clicked and not self.stats.game_active:
            self._start_game()
            #self.play_button = Button(self)

    def _eddie_at_bottom(self):
        """Checks if eddie has reached the bottom of the screen and will RUIN Frasier's new persian rug"""
        screen_rect = self.screen.get_rect()
        for eddie in self.eddies.sprites():
            if eddie.rect.bottom >= screen_rect.bottom:
                self._frasier_hit()
                break

    def _update_screen(self):
        """Draws Frasier and the background"""
        self.screen.fill(self.settings.bg_color)
        self.frasier.blitme()
        self.eddies.draw(self.screen)
        self.scoreboard.show_score()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        if not self.stats.game_active:
            self.play_button.draw_button()
        # if self.title_card:
        #     self.title_button.draw_button()
        pygame.display.flip()

    def _check_horde_edges(self):
        """respond correctly if eddies have reached an edge"""
        for eddie in self.eddies.sprites():
            if eddie.at_edge():
                self._switch_horde_direction()
                break

    def _switch_horde_direction(self):
        """changes eddie's direction as he inches down"""
        for eddie in self.eddies.sprites():
            eddie.rect.y += self.settings.eddie_drop_speed
        self.settings.eddie_dir *= -1

    def run_game(self):
        """primary game loop"""
        while True:
            if self.stats.game_active and not self.paused:
                self.check_events()
                self.frasier.update()
                self.lasers.update()
                self.update_lasers()
                self.update_eddies()
            self.check_exit()
            self._update_screen()

    def check_exit(self):
        """checks for events outside of game loop"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._const_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _const_events(self, event):
        """exits game based on keystroke"""
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.settings.speed_shift_up()
        elif event.key == pygame.K_LEFT:
            self.settings.speed_shift_down()
        elif event.key == pygame.K_p:
            self.paused = False if self.paused else True

    def update_eddies(self):
        """checks if eddie horde hits edge of screen, then updates position of all eddies"""
        self._check_horde_edges()
        self.eddies.update()
        if pygame.sprite.spritecollideany(self.frasier, self.eddies):
            self._frasier_hit()
        self._eddie_at_bottom()

    def update_lasers(self):
        """removes lasers if off of screen"""
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)
        self._check_hits()

    def _check_hits(self):
        """detects laser/eddie colllsions and updates accordingly"""
        collisions = pygame.sprite.groupcollide(self.lasers, self.eddies, True, True)
        if collisions:
            for eddies in collisions.values():
                self.stats.score += self.settings.eddie_points * len(eddies)
            self.scoreboard.prep_score()
            #self.scoreboard.check_high_score()
        if not self.eddies:
            self.show_title_card()
            self.settings.increase_speed()
            self.stats.level += 1
            self._start_level()

    def show_title_card(self):
        card = Button(self, random.choice(self.settings.button_messages))
        card.draw_button()
        sleep(1)




    def _start_game(self):
        """starts a new game"""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.eddies.empty()
        self._start_level()
        pygame.mouse.set_visible(False)


if __name__ =='__main__':
    tme = TooManyEddies()
    tme.run_game()
