import sys
import os
from time import sleep

import pygame

from configs import Configuracoes
from game_stats import GameStats
from placar import Placar
from botao import Botao
from nave import Nave
from tiro import Tiro
from klingons import Klingon


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
        # Cria uma instância para armazenar os dados do jogo
        self.stats = GameStats(self)
        self.placar = Placar(self)
        self.placar = Placar(self)
        # Músicas de fundo
        self.open_music = pygame.mixer.Sound(
            os.path.join("complemento/tng_open.mp3"))  # Abertura da série Star Trek: Next Generation
        self.battle_music = pygame.mixer.Sound(
            os.path.join("complemento/first_contact.mp3"))  # Assimilation battle sound
        # Sprites
        self.nave = Nave(self)
        self.tiros = pygame.sprite.Group()
        self.klingons = pygame.sprite.Group()
        self._criar_frota()

        # Botão de iniciar
        self.play_botao = Botao(self, "Iniciar")

        # Icon
        self.icon = pygame.transform.scale(pygame.image.load(
            os.path.join("complemento/klingon_icon.png")), (35, 35))
        pygame.display.set_icon(self.icon)

    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._check_events()
            self.open_music.play(loops=-1)
            self.open_music.set_volume(0.1)
            if self.stats.game_active:
                self.nave.update()
                self.open_music.stop()
                if self.open_music.stop:
                    self.battle_music.play(loops=-1)
                self._update_tiros()
                self._update_klingons()

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
            elif event.type == pygame.MOUSEBUTTONDOWN and self.stats.game_active is False:
                mouse_pos = pygame.mouse.get_pos()
                self._check_iniciar_botao(mouse_pos)
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(os.path.join("complemento/computerbeep_10.mp3")))

    def _check_iniciar_botao(self, mouse_pos):
        """Inicia um novo jogo quando o usuário clicar no botão"""
        click_botao = self.play_botao.rect.collidepoint(mouse_pos)
        if click_botao and not self.stats.game_active:
            # Reset as configs do jogo
            self.configuracoes.inicializar_dinamica_configs()
            # Reset os stats do jogo
            self.stats.reset_stats()
            self.stats.game_active = True
            self.placar.prep_placar()
            self.placar.prep_level()
            self.placar.prep_naves()

            # Retira os aliens e disparos da partida antiga
            self.klingons.empty()
            self.tiros.empty()

            # Cria uma nova frota e centraliza a nave
            self._criar_frota()
            self.nave.center_nave()

            # Esconder o cursor do mouse
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Responde as teclas"""
        if event.key == pygame.K_RIGHT:
            # Move a nave para a direita
            self.nave.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self._iniciar_jogo()
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("complemento/computerbeep_10.mp3"))
        elif event.key == pygame.K_SPACE and self.stats.game_active is True:
            self._dispara_tiro()

    def _iniciar_jogo(self):
        # Reset as configs do jogo
        self.configuracoes.inicializar_dinamica_configs()
        # Reset os stats do jogo
        self.stats.reset_stats()
        self.stats.game_active = True
        self.placar.prep_placar()

    def _check_keyup_events(self, event):
        """Responde a ausência de interação com o teclado"""
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = False

    def _dispara_tiro(self):
        """Cria um novo disparo e adiciona esse tiro em uma lista"""
        if len(self.tiros) < self.configuracoes.tiros_permitidos:
            novo_disparo = Tiro(self)
            self.tiros.add(novo_disparo)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("complemento/torp.mp3")))
        pygame.mixer.Channel(1).set_volume(0.35)

    def _update_tiros(self):
        """Atualiza a posição dos disparos e se deleta os antigos"""
        # Atualiza a posição
        self.tiros.update()
        # Deleta os tiros após sairem da tela
        for tiro in self.tiros.copy():
            if tiro.rect.bottom <= 0:
                self.tiros.remove(tiro)
        self._check_colisao_disparo()

    def _check_colisao_disparo(self):
        # Checar se algum disparo atingiu uma nave inimiga
        # Se sim, retirar a nave klingon da tela
        colisao = pygame.sprite.groupcollide(self.tiros, self.klingons, True, True)
        if colisao:
            for klingon in colisao.values():
                self.stats.score += self.configuracoes.klingon_points * len(klingon)
            self.placar.prep_placar()
            self.placar.check_high_score()
        if not self.klingons:
            # Destroi os tiros existentes e cria uma nova tropa
            self.tiros.empty()
            self._criar_frota()
            self.configuracoes.aumentar_vel()

            # Aumenta o nível
            self.stats.level += 1
            self.placar.prep_level()

    def _update_klingons(self):
        """Atualiza a posição de todas as naves Klingons"""
        self._check_fleet_edges()
        self.klingons.update()

        # Colisão de naves
        if pygame.sprite.spritecollideany(self.nave, self.klingons):
            self._nave_hit()

        # Verifica se a nave klingon atingiu o fundo da tela
        self._check_klingons_bottom()

    def _nave_hit(self):
        """Responde a nave caso seja atingida por uma nave klingon"""
        if self.stats.nave_left > 0:
            # Decrementa nave_left
            self.stats.nave_left -= 1
            self.placar.prep_naves()

            # Se livra das naves restantes e disparos
            self.klingons.empty()
            self.tiros.empty()

            # Cria uma nova frota de naves e centraliza a nave
            self._criar_frota()
            self.nave.center_nave()

            # Pausa
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _criar_frota(self):
        """Cria as naves Bird of Prey"""
        # Cria os Klingons e amostra a quantidade de naves em uma fileira
        # O espaço entre cada nave é igual a largura de uma nave
        klingon = Klingon(self)
        klingon_width, klingon_height = klingon.rect.size
        espaco_disp_x = self.configuracoes.screen_width - (2 * klingon_width)
        numero_klingons_x = espaco_disp_x // (2 * klingon_width)

        # Determina a primeira frota completa de Klingons
        nave_height = self.nave.rect.height
        espaco_disp_y = (self.configuracoes.screen_height -
                         (3 * klingon_height) - nave_height)
        num_fileiras = espaco_disp_y // (2 * klingon_height)

        # Cria a primeira fileira de naves
        for num_fileiras in range(num_fileiras):
            for quant_klingon in range(numero_klingons_x):
                self._criar_klingon(quant_klingon, num_fileiras)

    def _criar_klingon(self, quant_klingon, num_fileiras):
        """Cria uma nave e a posiciona em uma fileira"""
        klingon = Klingon(self)
        klingon_width, klingon_height = klingon.rect.size
        klingon.x = klingon_width + 2 * klingon_width * quant_klingon
        klingon.rect.x = klingon.x
        klingon.rect.y = klingon.rect.height + 2 * klingon.rect.height * num_fileiras
        self.klingons.add(klingon)

    def _check_fleet_edges(self):
        """Responde apropriadamente se qualquer nave klingon atingir a borda da tela"""
        for klingon in self.klingons.sprites():
            if klingon.check_edges():
                self._mudar_direcao_frota()
                break

    def _check_klingons_bottom(self):
        """Checa se alguma nave klingon atingiu o fundo da tela"""
        screen_rect = self.screen.get_rect()
        for klingon in self.klingons.sprites():
            if klingon.rect.bottom >= screen_rect.bottom:
                # Trata da mesma forma como se a nave fosse atingida
                self._nave_hit()
                break

    def _mudar_direcao_frota(self):
        """Mudar a direção da frota inteira"""
        for klingon in self.klingons.sprites():
            klingon.rect.y += self.configuracoes.fleet_drop_speed
        self.configuracoes.direcao_frota *= -1

    def _update_screen(self):
        # Redesenha a tela durante cada passada do loop
        # self.screen.fill(self.configuracoes.bg_color)
        self.screen.blit(self.configuracoes.background, [0, 0])
        self.nave.blitme()
        for tiros in self.tiros.sprites():
            tiros.draw_tiro()
        self.klingons.draw(self.screen)
        self.placar.show_placar()

        # Desenha o botão de Íniciar se o jogo estiver inativo
        if not self.stats.game_active:
            self.screen.blit(self.configuracoes.background, [0, 0])
            self.nave.blitme()
            self.play_botao.draw_botao()
            self.screen.blit(self.configuracoes.logo, [270, 35])

        pygame.display.flip()


if __name__ == '__main__':
    """Cria uma instancia do jogo e inicia a partida"""
    ik = InvasaoKlingon()
    ik.run_game()
