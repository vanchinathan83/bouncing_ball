import sys
import pygame
import pygame.sprite

from settings import Settings
from board import Board
from ball import Ball
from game_stats import GameStats


class BouncingBall:
    """ Class to manage the bouncing ball game. """

    def __init__(self):
        """ Intialize the game. """
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("Bouncing Ball")

        self.board = Board(self)
        self.game_stats = GameStats(self)
        self.ball = Ball(self)

    def run_game(self):
        """ This is the main loop of the game. """
        while True:
            self._check_events()
            if self.game_stats.is_game_active:
                self.board.update_position()
                self._check_ball_bounce()
                self.ball.update_position()
            self._update_screen()

    def _check_ball_bounce(self):
        """ Check whether the ball is bouncing off the board. """
        if self.board.rect.colliderect(self.ball.rect):
            self.ball.increment_y = False

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.board.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.board.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.board.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.board.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.board.blitme()
        self.ball.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    bb = BouncingBall()
    bb.run_game()
