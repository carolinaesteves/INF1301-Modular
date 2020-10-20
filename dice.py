# Tabela de Versionamento do Módulo Dado
# Desenvolvedor do Módulo: Victor Fróes, Ana Carolina Esteves, João Pedro Botelho
#
# Tabela baseada no git log do repositório local do módulo
# 
# Autor Victor Fróes,Ana Carolina Esteves, João Pedro Botelho no dia 25/09:
# cria rollDice e showDice
import pygame
import random

def rollDice():
    dice = random.randrange(1,7)
    return dice

def showDice(dice):
    print(dice)
#carrega gráfico
