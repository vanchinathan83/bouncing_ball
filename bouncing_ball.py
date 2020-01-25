import sys
import pygame
import pygame.sprite
import random

from settings import Settings
from board import Board
from ball import Ball
from game_stats import GameStats
from scoreboard import Scoreboard


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
        self.scoreboard = Scoreboard(self)
        self.balls = pygame.sprite.Group()
        self.ball_choices = ["images/ball.png", "images/pink_ball.png", 
                "images/yellow_ball.png"]
        self.balls.add(Ball("images/ball.png", self))

    def run_game(self):
        """ This is the main loop of the game. """
        while True:
            self._check_events()
            if self.game_stats.is_game_active:
                self.board.update_position()
                self._check_ball_bounce()
                self._update_balls()
                self._check_ball_touched_bottom()
                self.game_stats.update_score()
                self.scoreboard.prep_score()
            self._update_screen()

    def _update_balls(self):
        self.balls.update()

    def _check_ball_touched_bottom(self):
        for ball in self.balls.sprites():
            if ball.rect.bottom >= self.screen.get_rect().bottom:
                self.game_stats.decrement_lives()
                ball.rect.center = self.screen.get_rect().center

    def _check_ball_bounce(self):
        """ Check whether the ball is bouncing off the board. """
        for ball in self.balls.sprites():
            if self.board.rect.colliderect(ball.rect):
                ball.increment_y = False

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
        self.scoreboard.show_score()
        self.board.blitme()

        if len(self.balls) < self.settings.no_of_balls:
            self.balls.add(Ball(random.choice(self.ball_choices), self))
        for ball in self.balls.sprites():
            ball.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    bb = BouncingBall()
    bb.run_game()
