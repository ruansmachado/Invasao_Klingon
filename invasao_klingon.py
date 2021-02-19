import sys
import pygame
from configuracoes import Configuracoes
from nave import Nave


class InvasaoKlingon:
    """Class para lidar com os comportamentos do jogo"""
    def __init__(self):
        """Inicializa o jogo e cria os recursos"""
        pygame.init()
        self.configuracoes = Configuracoes()
        """Para habilitar modo Fullscreen, retire as anotações 
        dos três códigos abaixo e adicione observação no 'self.screen'"""
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.configuracoes.screen_width = self.screen.get_rect().width
        # self.configuracoes.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.configuracoes.screen_width, self.configuracoes.screen_height))
        pygame.display.set_caption("Invasão Klingon")
        self.nave = Nave(self)

    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._check_events()
            self.nave.update()
            self._update_screen()

    def _check_events(self):
        """Notar o uso do teclado e do mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde as teclas"""
        if event.key == pygame.K_RIGHT:
            # Move a nave para a direita
            self.nave.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde a ausência de interação com o teclado"""
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = False

    def _update_screen(self):
        # Redesenha a tela durante cada passada do loop
        self.screen.fill(self.configuracoes.bg_color)
        self.nave.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    """Cria uma instancia do jogo e inicia a partida"""
    ai = InvasaoKlingon()
    ai.run_game()
