import pygame
from pygame.sprite import Sprite


class Tiro(Sprite):
    """Class para manipular os tiros disparados pela nave"""
    def __init__(self, ai_game):
        """Cria um disparo na posição atual da nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.configuracoes = ai_game.configuracoes
        self.cor = self.configuracoes.tiro_cor

        # Cria um disparo rect na posição (0, 0) e reposiciona no local certo
        self.rect = pygame.Rect(0, 0, self.configuracoes.tiro_width,
                                self.configuracoes.tiro_height)
        self.rect.midtop = ai_game.nave.rect.midtop

        # Armazena a posição do disparo como um decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move o tiro para cima na tela"""
        # Atualiza a posição decimal do disparo
        self.y -= self.configuracoes.tiro_vel
        # Atualiza a posição rect
        self.rect.y = self.y

    def draw_tiro(self):
        """Desenha o tiro na tela"""
        pygame.draw.rect(self.screen, self.cor, self.rect)
