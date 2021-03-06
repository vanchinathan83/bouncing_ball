

class GameStats:
    """ This class stores all the stats of the game. """

    def __init__(self, bb_game):
        self.settings = bb_game.settings
        self.is_game_active = True
        self.score = 0
        self.no_of_lives = self.settings.max_lives
        self.score_checkpoint = 1000

    def update_score(self):
        """ Updates the score of the game. """
        self.score += round(float(self.settings.ball_speed *
                                  self.settings.no_of_balls * .2))

        if self.score > self.score_checkpoint * self.settings.no_of_balls:
            self.settings.ball_speed += 1
            self.settings.board_speed += 4
            self.score_checkpoint += 1000

        if self.score > 5000 * self.settings.no_of_balls:
            self.settings.no_of_balls += 1

    def decrement_lives(self):
        if self.no_of_lives:
            self.no_of_lives -= 1
        else:
            self.is_game_active = False
