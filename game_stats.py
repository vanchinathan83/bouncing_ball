

class GameStats:
    """ This class stores all the stats of the game. """

    def __init__(self, bb_game):
        self.settings = bb_game.settings
        self.is_game_active = True
        self.score = 0
        self.no_of_lives = self.settings.max_lives

    def update_score(self):
        """ Updates the score of the game. """
        self.score += self.settings.ball_speed * self.settings.no_of_balls
        if self.score > 5000 * self.settings.no_of_balls:
            self.settings.no_of_balls += 1
            self.settings.ball_speed += 5
            self.settings.board_speed += 20

    def decrement_lives(self):
        if self.no_of_lives:
            self.no_of_lives -= 1
        else:
            self.is_game_active = False
