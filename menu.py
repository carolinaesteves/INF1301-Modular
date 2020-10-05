import pygame

#inicializa a biblioteca pygame
pygame.init()

branco = (255,255,255)
verde = (0,253,0)
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

telaVerde = False
#loop da cutscene inicial e do menu inicial
intro = True
while intro:
    Lisdown = False
    Uisdown = False
    Disdown = False
    Oisdown = False
    
    tela.fill(branco)
    lY += 0.8
    uY += 0.8
    
    if lY < 40:
        mov_l(l, 110, lY)
    else:
        Lisdown = True
        
    if Lisdown:
        mov_l(l, 110, 40)

        
    if uY < 50:
        mov_l(u, 190, uY)
    else:
        Uisdown = True
        
    if Uisdown:
        mov_l(u, 190, 50)
        

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
         
        #fecha o jogo ao clicar no X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

