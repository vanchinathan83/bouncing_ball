import pygame
import random

class Ball:
    """ This is the class that controls the ball. """

    def __init__(self, bb_game):
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.screen_rect = bb_game.screen.get_rect()

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.game_stats = bb_game.game_stats
        self.increment_x = True
        self.increment_y = True

    def update_position(self):
        """ This method makes the ball move in a diagonal fashion. """
        self._update_movement()

        if self.increment_x:
            self.rect.x += self.settings.ball_speed
            # make sure that the next movement 
            # does not cross the screen
            if self.rect.right >= self.screen_rect.right:
                self.rect.right = self.screen_rect.right
                self.increment_x = False
        else:
            self.rect.x -= self.settings.ball_speed
            if self.rect.left <= self.screen_rect.left:
                self.rect.left = self.screen_rect.left
                self.increment_x = True

        if self.increment_y:
            self.rect.y += self.settings.ball_speed
        else:
            self.rect.y -= self.settings.ball_speed
            if self.rect.top < 0:
                self.rect.top = 0
                self.increment_y = True

    def _update_movement(self):
        if self.rect.top <= self.screen_rect.top:
            self.increment_y = True
        if self.rect.right >= self.screen_rect.right:
            self.increment_x = False
        if self.rect.left <= self.screen_rect.left:
            self.increment_x = True

    def blitme(self):
        """ Draw the ball. """
        self.screen.blit(self.image, self.rect)