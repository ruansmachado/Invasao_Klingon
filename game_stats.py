class GameStats:
    """Monitora os dados do jogo"""

    def __init__(self, ai_game):
        """Inicia a coleta"""
        self.settings = ai_game.configuracoes
        self.reset_stats()

        # Começa o jogo de forma ativida
        self.game_active = True

    def reset_stats(self):
        """Inicializa as estatiticas que serão utilizadas durante o jogo"""
        self.nave_left = self.settings.nave_limit
