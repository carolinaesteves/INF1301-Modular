import pygame
from pygame import mixer
import menu

def startGame():
    #vai para o módulo Partida, onde o jogo começa
    return


pygame.init()

#carrega imagens
logo_l = pygame.image.load('logo-l.png')
logo_u = pygame.image.load('logo-u.png')
logo_d = pygame.image.load('logo-d.png')
logo_o = pygame.image.load('logo-o.png')
ays = pygame.image.load('w-ays.png')

#carrega musica de fundo
mixer.music.load('gold-saucer-8bit.wav')
mixer.music.set_volume(0.4)

menu.executaMenu(logo_l,logo_u,logo_d,logo_o,ays)
startGame()