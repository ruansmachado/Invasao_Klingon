class GameStats:
    """Monitora os dados do jogo"""

    def __init__(self, ai_game):
        """Inicia a coleta"""
        self.settings = ai_game.configuracoes
        self.reset_stats()

        # Começa o jogo de forma inativa
        self.game_active = False

        # O High score não deve nunca ser resetado
        self.high_score = 0

    def reset_stats(self):
        """Inicializa as estatiticas que serão utilizadas durante o jogo"""
        self.nave_left = self.settings.nave_limit
        self.score = 0
        self.level = 1
