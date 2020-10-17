import pygame
from pygame import mixer


#inicializa a biblioteca pygame
pygame.init()

branco = (255,255,255)
verde = (0,253,0)
preto = (0,0,0)

AxL = (800,600)
lY = -300
uY = -300
dY = -300
oY = -300

#seta tela inicial
tela = pygame.display.set_mode(AxL)

#seta o nome do jogo na janela
pygame.display.set_caption("Ludo")

#carrega imagens da cutscene inicial
l = pygame.image.load('logo-l.png')
u = pygame.image.load('logo-u.png')
d = pygame.image.load('logo-d.png')
o = pygame.image.load('logo-o.png')

#carrega musica de fundo
mixer.music.load('gold-saucer-8bit.wav')
mixer.music.set_volume(0.4)


#define um botão genérico
class button():
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    #método que desenha o botão na tela
    def draw(self, win):
        Img = pygame.image.load(self.text)
        win.blit(Img,(self.x, self.y))

    #método que detecta se o mouse está posicionado sobre o botão
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def mov_l(l,x,y):
    tela.blit(l, (x,y))

#cria botao incial
botaoIni = button(370, 160, 64, 64, 'play.png')

#loop da cutscene inicial
intro = True

while intro:
    Lisdown = False
    Uisdown = False
    Disdown = False
    Oisdown = False
    timer = pygame.time.get_ticks()
    
    tela.fill(preto)
    
    
    if lY < 40:
        mov_l(l, 110, lY)
        lY += 0.8
    else:
        Lisdown = True
        
    if timer > 1300:
        if uY < 40:
            mov_l(u, 195, uY)
            uY += 0.9
        else:
            Uisdown = True
    if timer > 2100:
        if dY < 50:
            mov_l(d, 270, dY)
            dY += 1.2
        else:
            Disdown = True
    if timer > 3100:
        if oY < 40:
            mov_l(o, 340, oY)
            oY += 1.4
        else:
            Oisdown = True


    if Lisdown:
        mov_l(l, 110, 40)
    if Uisdown:
        mov_l(u, 195, 40)
    if Disdown:
        mov_l(d, 270, 50)
    if Oisdown:
        mov_l(o, 340, 40)
        
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
         
        #fecha o jogo ao clicar no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    if timer > 4273:
        intro = False
        

mixer.music.play(-1)

#loop do menu
running = True

while running:

    #fecha o jogo ao clicar no X
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if botaoIni.isOver(pos):
            print('clicou no botao')

