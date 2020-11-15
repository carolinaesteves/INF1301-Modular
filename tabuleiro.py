import pygame
from pygame import mixer

import peao

#inicializa a biblioteca
pygame.init()

#variaveis auxiliares
AxL = (800,700)
branco = (255,255,255)

#carrega imagens
tab = pygame.image.load('tabuleiro.png')

def draw(numJog):
    #seta tela
    tela = pygame.display.set_mode(AxL)
    tela.fill(branco)

    #seta nome do jogo na janela
    pygame.display.set_caption("Ludo")

    #loop do tabuleiro
    running = True

    while running:
        tela.blit(tab, (0,0))

        peao.initDraw(tela, numJog)

        for event in pygame.event.get():
            #fecha o jogo ao clicar no X
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

