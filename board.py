import pygame

class Board:
    """ This class will control the bouncing board. """

    def __init__(self, bb_game):
        """ Init the board and its starting position. """
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.screen_rect = bb_game.screen.get_rect()

        # Load the board image
        self.image = pygame.image.load('images/rectangle.png')
        self.rect = self.image.get_rect()

        # start the board at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        """ Update the position of the board. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.board_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.board_speed

    def blitme(self):
        """ Draw the board. """
        self.screen.blit(self.image, self.rect)
