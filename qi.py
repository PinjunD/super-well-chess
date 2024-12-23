import pygame
from pygame.sprite import Sprite

class qi(Sprite):
    def __init__(self, ai_game, loc, da=0):
        super().__init__()
        self.screen = ai_game.screen
        self.type = ai_game.type
        if da:
            if self.type == 1:
                self.image = ai_game.settings.daqi2
            else:
                self.image = ai_game.settings.daqi1
        else:
            if self.type == 1:
                self.image = ai_game.settings.qi1
            else:
                self.image = ai_game.settings.qi2

        self.rect = self.image.get_rect()
        self.rect.center = loc

    def draw(self):
        self.screen.blit(self.image, self.rect)