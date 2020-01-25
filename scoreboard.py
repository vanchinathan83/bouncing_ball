import pygame.font


class Scoreboard:
    """ Scoreboard of the game. """

    def __init__(self, bb_game):
        self.bb_game = bb_game
        self.screen = bb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = bb_game.settings
        self.game_stats = bb_game.game_stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """ Make the score into a image. """
        score_str = "{:,}".format(self.game_stats.score)
        self.score_image = self.font.render("Score:" + score_str, True,
            self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)