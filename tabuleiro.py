import pygame
from pygame import mixer

#inicializa a biblioteca
pygame.init()

#variaveis auxiliares
AxL = (800,700)
branco = (255,255,255)

#seta tela
tela = pygame.display.set_mode(AxL)
tela.fill(branco)

#seta nome do jogo na janela
pygame.display.set_caption("Ludo")

#carrega imagens
tab = pygame.image.load('tabuleiro.png')

pVrm = pygame.image.load('peao vrm.png')
pVer = pygame.image.load('peao vrd.png')

#loop
running = True

while running:
    tela.blit(tab, (0,0))
    
    tela.blit(pVrm, (65,110))
    tela.blit(pVrm, (65, 30))
    tela.blit(pVrm, (170,110))

    
    tela.blit(pVer, (585, 110))

    for event in pygame.event.get():
        #fecha o jogo ao clicar no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
