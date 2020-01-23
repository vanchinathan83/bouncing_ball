import pygame

class Ball:
    """ This is the class that controls the ball. """

    def __init__(self, bb_game):
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.screen_rect = bb_game.screen.get_rect()

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.moving_up = True
        self.moving_down = True
        self.within_bounds = self.rect.x <= self.settings.screen_width and self.rect.y <= self.settings.screen_height

    def update_position(self):
        """ This method makes the ball move in a diagonal fashion. """
        self.within_bounds = self.rect.x <= self.settings.screen_width and self.rect.y <= self.settings.screen_height 
        if self.rect.x > 0 and self.rect.y > 0 and self.moving_up:
            self.rect.x -= self.settings.ball_speed
            self.rect.y -= self.settings.ball_speed
        elif self.rect.x <= 0 or self.rect.y <=0 or (self.moving_down and self.within_bounds):
            self.moving_up = False
            self.moving_down = True
            self.rect.x += self.settings.ball_speed
            self.rect.y += self.settings.ball_speed
        elif self.rect.x >= self.settings.screen_width or self.rect.y >= self.settings.screen_height:
            self.moving_up = True
            self.moving_down = False
            self.rect.x -= self.settings.ball_speed
            self.rect.y -= self.settings.ball_speed

    def blitme(self):
        """ Draw the board. """
        self.screen.blit(self.image, self.rect)