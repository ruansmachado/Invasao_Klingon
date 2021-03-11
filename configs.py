import pygame
import os


class Configuracoes:
    """Class que armazena todas as configurações do Invasão Klingon"""

    def __init__(self):
        """Inicia as configurações das stats do jogo"""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.background = pygame.transform.scale(pygame.image.load(
            os.path.join("complemento/space.jpg")), (1440, 900))
        self.logo = pygame.transform.scale(pygame.image.load(
            os.path.join("complemento/STAR-TREK-LOGO.png")), (650, 366))
        self.rect = self.background.get_rect()
        # Configurações da nave
        self.nave_limit = 3
        # Configurações do tiro
        self.tiro_width = 9
        self.tiro_height = 15
        self.tiro_cor = (94, 23, 16, 255)
        self.tiros_permitidos = 3
        # Configurações da nave Klingon
        self.fleet_drop_speed = 10

        # Velocidade do jogo
        self.speedup_scale = 1.1

        # Velocidade em que aumenta os pontos da nave inimiga
        self.placar_scale = 1.5

        self.inicializar_dinamica_configs()

    def inicializar_dinamica_configs(self):
        """Inicializa as configurações que são alteradas durante o jogo"""
        self.nave_velocidade = 1.5
        self.tiro_vel = 3.0
        self.vel_klingon = 1

        # direção_frota 1 representa a direita; -1 representa a esquerda
        self.direcao_frota = 1

        # Score
        self.klingon_points = 10

    def aumentar_vel(self):
        """Aumenta velocidade das naves e dos pontos ao abater uma nave inimiga"""
        self.nave_velocidade *= self.speedup_scale
        self.tiro_vel *= self.speedup_scale
        self.vel_klingon *= self.speedup_scale

        self.klingon_points = int(self.klingon_points * self.placar_scale)
