import sys
import pygame

from settings import Settings
from board import Board


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

    def run_game(self):
        """ This is the main loop of the game. """
        while True:
            self._check_events()
            self.board.update_position()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.board.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.board.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.board.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.board.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.board.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    bb = BouncingBall()
    bb.run_game()
