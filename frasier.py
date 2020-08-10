import pygame

class Frasier:
    def __init__(self, tme_game):
        self.screen = tme_game.screen
        self.screen_rect = tme_game.screen.get_rect()
        self.image = pygame.image.load('images/frasier_4.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = tme_game.settings
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right:
            self.x += self.settings.f_speed
        if self.moving_left:
            self.x -= self.settings.f_speed
        self.rect.x = self.x
        #positional cases for an "infinite canvas
        if self.rect.left >= self.screen_rect.right:
            self.x = 0 - (self.rect.right - self.rect.left)

        if self.rect.right < 0:
            self.x = self.screen_rect.right


    def blitme(self):
        self.screen.blit(self.image, self.rect)