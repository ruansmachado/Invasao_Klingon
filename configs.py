class Configuracoes:
    """Class que armazena todas as configurações do Invasão Klingon"""

    def __init__(self):
        """Inicia as configurações do jogo"""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Configurações da nave
        self.nave_velocidade = 1.5
        self.nave_limit = 3
        # Configurações do tiro
        self.tiro_vel = 1.5
        self.tiro_width = 9
        self.tiro_height = 15
        self.tiro_cor = (60, 60, 60)
        self.tiros_permitidos = 6
        # Configurações da nave Klingon
        self.vel_klingon = 2
        self.fleet_drop_speed = 10
        # direção_frota 1 representa a direita; -1 representa a esquerda
        self.direcao_frota = 1
