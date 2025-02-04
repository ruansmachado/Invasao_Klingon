import pygame
import os
from pygame.sprite import Sprite


class Klingon(Sprite):
    """Class que representa as naves klingons e configura sua posição inicial"""

    def __init__(self, ik_game):
        """Cria a nave e a posiciona"""
        super().__init__()
        self.screen = ik_game.screen
        self.settings = ik_game.configuracoes

        # Carrega a imagem da nave e define os atributos rect
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('complemento/bird_of_prey.bmp')), (70, 60))
        self.rect = self.image.get_rect()

        # Cria uma nova nave perto do lado esquerdo superior na tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata da nave
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna True se as naves klingons atigir a borda da tela"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move a nave klingo para a direita ou esquerda"""
        self.x += (self.settings.vel_klingon *
                   self.settings.direcao_frota)
        self.rect.x = self.x
