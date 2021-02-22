import pygame.font

class Botao:
    def __init__(self,ai_game,msg):
        """Inicializa os atributos"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Dimensões e propriedades do botão
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Construir o rect e centralizar-lo
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # O botão de ínicio tem que aparecer apenas uma vez
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Torna a mensagem em uma imagem renderizada e centraliza o texto no botão"""
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_botao(self):
        # Desenha um botão vazio e imprimi a mensagem no meio
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)