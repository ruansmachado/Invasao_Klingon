import pygame.font
from pygame.sprite import Group
from nave import Nave



class Placar:
    """Class que reporta o score do jogador"""

    def __init__(self, ik_game):
        """Inicializa a coleta de dados"""
        self.ik_game = ik_game
        self.screen = ik_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ik_game.configuracoes
        self.stats = ik_game.stats

        # Font para dispositive os dados
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # Inicia o placar inicial
        self.prep_placar()
        self.prep_placar_score()
        self.prep_level()
        self.prep_naves()

    def prep_placar(self):
        """Torna o placar em imagem"""
        rounded_placar = round(self.stats.score, -1)
        placar_str = "{:,}".format(rounded_placar)
        self.placar_image = self.font.render(placar_str, True, self.text_color, (12, 13, 17, 255))

        # Posiciona o placar na parte superior direita da tela
        self.placar_rect = self.placar_image.get_rect()
        self.placar_rect.right = self.screen_rect.right - 20
        self.placar_rect.top = 20

    def show_placar(self):
        self.screen.blit(self.placar_image, self.placar_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.naves.draw(self.screen)

    def prep_placar_score(self):
        """Torna o mais alto score em uma imagem"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, (12, 13, 17, 255))

        # Centraliza o high score no alto da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.placar_rect.top

    def check_high_score(self):
        """Checa se existe um novo high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_placar_score()

    def prep_level(self):
        """Score board"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, (12, 13, 17, 255))

        # Posição do level
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.placar_rect.right
        self.level_rect.top = self.placar_rect.bottom + 10


    def prep_naves(self):
        """Amostra quantas naves ainda restam"""
        self.naves = Group()
        for nave_num in range(self.stats.nave_left):
            nave = Nave(self.ik_game)
            nave.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/aventine_ship.bmp'),
                                                                    (50, 20)), 90)
            nave.rect.x = 10 + nave_num * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)
