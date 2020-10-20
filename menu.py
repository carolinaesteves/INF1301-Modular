import pygame
from pygame import mixer
import Jogador


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
vol = 0.4

lisJogadores = []

#seta tela inicial
tela = pygame.display.set_mode(AxL)

#seta o nome do jogo na janela
pygame.display.set_caption("Ludo")

#carrega imagens
l = pygame.image.load('logo-l.png')
u = pygame.image.load('logo-u.png')
d = pygame.image.load('logo-d.png')
o = pygame.image.load('logo-o.png')
ays = pygame.image.load('w-ays.png')
eb = pygame.image.load('eb....png')
sImg = pygame.image.load('sound.png')
nsImg = pygame.image.load('no-sound.png')

#carrega musica de fundo
mixer.music.load('gold-saucer-8bit.wav')
mixer.music.set_volume(vol)


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

def willQuit():
    active = True
    
    while active:
        tela.blit(ays, (240,250))
        botaoy.draw(tela)
        botaon.draw(tela)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            #fecha o ojogo ao clicar no X
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botaoy.isOver(pos):
                    pygame.quit()
                    exit()

                if botaon.isOver(pos):
                    active = False
                    tela.fill(preto)
                    show_logo()
                    
            if event.type == pygame.MOUSEMOTION:
                if botaoy.isOver(pos):
                    botaoy.text = 'b-yes-m.png'
                else:
                    botaoy.text = 'b-yes.png'

                if botaon.isOver(pos):
                    botaon.text = 'b-no-m.png'
                else:
                    botaon.text = 'b-no.png'

        pygame.display.update()

def show_logo():
    tela.blit(l, (110, lY));
    tela.blit(u, (195, uY));
    tela.blit(d, (270, dY));
    tela.blit(o, (340, oY));
    
        
#criando os botoes
botaoP = button(330, 300, 130, 55, 'b-play.png')
botaoSc = button(330, 405, 130, 55, 'b-score.png')
botaoQ = button(330, 510, 130, 55, 'b-quit.png')
botaoy = button(260, 380, 130, 55, 'b-yes.png')
botaon = button(420, 380, 130, 55, 'b-no.png')
botaoSo = button(730, 540, 40, 40, 'sound.png')

#loops
intro = True
running = True

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
         
        #fecha o jogo ao clicar no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()

    if timer > 4500:
        intro = False


mixer.music.play(-1)
soundOn = True


while running:
    botaoP.draw(tela)
    botaoSc.draw(tela)
    botaoQ.draw(tela)
    botaoSo.draw(tela)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        #fecha o jogo ao clicar no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoP.isOver(pos):
                running = False
                
           
                
            if botaoSc.isOver(pos):
                tela.blit(eb,(475,320))
            
            if botaoQ.isOver(pos):
                willQuit()

            if botaoSo.isOver(pos):
                if vol == 0.4:
                    vol = 0
                    mixer.music.set_volume(vol)
                else:
                    vol = 0.4
                    mixer.music.set_volume(vol)
                    

        if event.type == pygame.MOUSEMOTION:
            if botaoP.isOver(pos):
                botaoP.text = 'b-play-m.png'
            else:
                botaoP.text = 'b-play.png'

            if botaoSc.isOver(pos):
                botaoSc.text = 'b-score-m.png'
            else:
                botaoSc.text = 'b-score.png'
            
            if botaoQ.isOver(pos):
                botaoQ.text = 'b-quit-m.png'
            else:
                botaoQ.text = 'b-quit.png'
                

    pygame.display.update()

lisJogadores = Jogador.retorna_jogadores(tela)
