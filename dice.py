import pygame
import random
import time

__all__ = ["rollDice","loadDiceSprites","showDice","configuraDiceButton","animaDado"]

def rollDice():
    dice = random.randrange(1,7)
    return dice

def loadDiceSprites():
    diceroll = [pygame.image.load('diceroll1.png'), pygame.image.load('diceroll2.png'),
                pygame.image.load('diceroll4.png'), pygame.image.load('diceroll4.png'),
                pygame.image.load('diceroll5.png'), pygame.image.load('diceroll6.png')]
    diceroll1 = pygame.image.load('diceroll1.png')

def showDice(dice):
    if dice == 1:
        dice1 = pygame.image.load('dice1.png')
        screen.blit(dice1, tam)
    if dice == 2:
        dice2 = pygame.image.load('dice2.png')
        screen.blit(dice2, tam)
    if dice == 3:
        dice3 = pygame.image.load('dice3.png')
        screen.blit(dice3, tam)
    if dice == 4:
        dice4 = pygame.image.load('dice4.png')
        screen.blit(dice4, tam)
    if dice == 5:
        dice5 = pygame.image.load('dice5.png')
        screen.blit(dice5, tam)
    if dice == 6:
        dice6 = pygame.image.load('dice6.png')
        screen.blit(dice6, tam)

def configuraDiceButton():
    # seta o dado como botao
    dado = button(10, 620, 512, 512, 'dice1.png')
    tam = (10, 620)
    clock = pygame.time.Clock()
    FPS = 60
    a = Animation(diceroll, 0.1)
    run = True
    dado.draw(screen)
    while run:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if dado.isOver(pos):
                    run = False
                    break
        pygame.display.update()

def animaDado():
    active = True
    timeout = time.time() + 1
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        segundos = clock.tick(FPS) / 1000.0  # segundos de cada loop
        a.update(segundos)
        screen.blit(a.image, tam)
        pygame.display.update()
        if time.time() > timeout:
            break

class button():
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # método que desenha o botão na tela
    def draw(self, win):
        Img = pygame.image.load(self.text)
        win.blit(Img, (self.x, self.y))

    # método que detecta se o mouse está posicionado sobre o botão
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Animation(pygame.sprite.Sprite):

    def __init__(self, images, time_interval):
        self.images = images
        self.image = self.images[0]
        self.time_interval = time_interval
        self.index = 0
        self.timer = 0

    def update(self, seconds):
        self.timer += seconds
        if self.timer >= self.time_interval:
            self.image = self.images[self.index]
            self.index = (self.index + 1) % len(self.images)
            self.timer = 0


