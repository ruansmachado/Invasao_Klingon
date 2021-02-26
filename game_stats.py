import pygame


class GameStats:
    """Monitora os dados do jogo"""

    def __init__(self, ik_game):
        """Inicia a coleta"""
        self.settings = ik_game.configuracoes
        self.reset_stats()

        # Começa o jogo de forma inativa
        self.game_active = False
        self.battle_music = pygame.mixer.Sound("images/first_contact.mp3")  # Assimilation battle sound
        self.battle_music.play(loops=-1)
        self.battle_music.set_volume(0.8)

        # O High score não deve nunca ser resetado
        self.high_score = 0

    def reset_stats(self):
        """Inicializa as estatiticas que serão utilizadas durante o jogo"""
        self.nave_left = self.settings.nave_limit
        self.score = 0
        self.level = 1
