import pygame
from pygame.sprite import Sprite
from configs import Configuracoes


class Background(Sprite):

    def __init__(self, ai_game):
        super().__init__()  #call Sprite initializer
        self.configs = Configuracoes()
        self.screen = ai_game.screen
        self.image = pygame.transform.scale(pygame.image.load("images/space.jpg"), (self.configs.screen_width, self.configs.screen_height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

    def blitme(self):
        """Posiciona a nave na sua posição padrão"""
        self.screen.blit(self.image, self.rect)