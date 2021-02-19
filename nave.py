import pygame


class Nave:
    """Class para definir os parametros da nave"""
    def __init__(self, ai_game):
        """Inicia a nave e as configurações da posição inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.configuracoes
        self.screen_rect = ai_game.screen.get_rect()
        # Carrega a imagem da nave e mapea a posição
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/aventine_ship.bmp'),
                                                                    (130, 55)), 90)
        self.rect = self.image.get_rect()
        # Cria uma nova nave no parte baixa centralizado no meio da imagem
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um valor decimal para a posição horizontal da nave
        self.x = float(self.rect.x)
        # Movimento indicado
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da nave baseado no movimento indicado"""
        # Atualiza o valor x da nave, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.nave_velocidade
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.nave_velocidade
        # Atualiza o objeto rect da self.x
        self.rect.x = self.x

    def center_nave(self):
        """Centraliza a nave"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Posiciona a nave na sua posição padrão"""
        self.screen.blit(self.image, self.rect)
