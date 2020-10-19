import pygame as pg
from pygame import font

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Ludo")
COLOR_INACTIVE = pg.Color(26,35,126)
COLOR_ACTIVE = pg.Color(255,17,17)
FONT = pg.font.Font("8bit2.TTF", 26)
FONTnum = pg.font.Font("8bit.TTF", 50)
FONTletras = pg.font.Font("8bit2.TTF", 32)
branco = (255,255,255)
madeira=(165,128,100)
verde = (0, 255, 0)
trigo = (216,216,191)

def select_number():

    done = False
    screen.fill((0, 0, 0))
    # Escrevendo na tela a pergunta do titulo
    text = FONTletras.render('Qual o numero de jogadores?', True, verde)
    screen.blit(text, (100, 100))
    # Escrevendo na tela numero 2 e a sua borda para poder criar um botão
    rect2 = pg.Rect(250, 300, 40, 40)
    text2 = '2'
    txt_surface2 = FONTnum.render(text2, True, trigo)
    screen.blit(txt_surface2, (260, 305))
    pg.draw.rect(screen, trigo, rect2, 2)
    # Escrevendo na tela numero 3 e a sua borda para poder criar um botão
    rect3 = pg.Rect(350, 300, 40, 40)
    text3 = '3'
    txt_surface3 = FONTnum.render(text3, True, trigo)
    screen.blit(txt_surface3, (360, 305))
    pg.draw.rect(screen, trigo, rect3, 2)
    # Escrevendo na tela numero 4 e a sua borda para poder criar um botão
    rect4 = pg.Rect(450, 300, 40, 40)
    text4 = '4'
    txt_surface4 = FONTnum.render(text4, True, trigo)
    screen.blit(txt_surface4, (460, 305))
    pg.draw.rect(screen, trigo, rect4, 2)
    pg.display.flip()
    # Parte do código de definições de eventos, caso clique dentro de alguma borda, funcinando como um botão, ou caso feche o jogo
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect2.collidepoint(event.pos):
                    return text2

                elif rect3.collidepoint(event.pos):
                    return text3

                elif rect4.collidepoint(event.pos):
                    return text4

# Classe utilizada para inputbox de nome dos jogadores

class InputBox:
    # Inicialização do InputBox
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    # Eventos do InputBox
    def eventobox(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # Caso Clique no InputBox, o mesmo é ativado
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Mudança de cor quando está ativo ou inativo
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Entrada de texto
                self.txt_surface = FONT.render(self.text, True, branco)


    def update(self):
        # Aumenta tamanho do inputbox, caso nome não caiba
        width = max(300, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):

        # Desenha na tela o texto
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Desenha na tela a borda
        pg.draw.rect(screen, self.color, self.rect, 2)

    # Limpa o inputbox, apos submit
    def limpar(self):

        self.text = ''
        self.txt_surface = FONT.render(self.text, True, self.color)
        self.active = False

def input_name():

    # Chamando a função para saber quantos jogadores são
    quant = select_number()
    quant = int(quant)
    #Declarando inputbox
    input_box1 = InputBox(100, 150, 300, 35)
    input_boxes = [input_box1]
    # Tela preta
    screen.fill((0, 0, 0))
    # Definindo, desenhando o botao Submit
    rect1 = pg.Rect(100, 250, 140, 35)
    text1 = 'Submit'
    txt_surface1 = FONTletras.render(text1, True, madeira)
    screen.blit(txt_surface1, (107, 255))
    pg.draw.rect(screen, COLOR_INACTIVE, rect1, 2)
    # Definindo a lista que vai retorna a quant de players e os nomes
    lista = []
    # Introduzindo o numero de quantidade de player na lista
    lista.append(quant)
    # Contador
    i = 1
    # While para repetir o código na quantidade de player necessário, assim podendo registrar o nome de todos os jogadores.
    while quant > 0:
        # Iniciando limpando inputbox e a tela
        for box in input_boxes:
            box.limpar()
        screen.fill((0, 0, 0))
        # Definindo titulo pedindo nome e alterando o número do jogador conforme o contador
        text2 = "Digite o nome do jogador numero"
        txt_surface2 = FONTletras.render(text2, True, branco)
        text3 = "{jogador}".format(jogador=i)
        txt_surface3 = FONTnum.render(text3, True, branco)
        done = False
        # While Comandando o inputbox e o botão submit, usuario digita o nome aqui, e aperta botao submit
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                    quant = 0
                if event.type == pg.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        done = True


                for box in input_boxes:
                    box.eventobox(event)

            for box in input_boxes:
                box.update()
            screen.fill((0, 0, 0))
            screen.blit(txt_surface1, (107, 255))
            pg.draw.rect(screen, COLOR_INACTIVE, rect1, 2)
            txt_surface2 = FONTletras.render(text2, True, branco)
            screen.blit(txt_surface2, (50, 50))
            screen.blit(txt_surface3, (720, 50))
            for box in input_boxes:
                box.draw(screen)
            pg.display.flip()
        # Após apertar botão submit, salvamos o nome na nossa lista
        for box in input_boxes:
            lista.append(box.text)
        # Contador de Jogadores do While para saber quantos nomes vai ser submetido
        quant -= 1
        # Contador utilizado no título
        i += 1
        
    # Retorna nossa lista pronta com o número de players, e seus respectivos nomes.
    return lista


if __name__ == '__main__':
    input_name()
    pg.quit()
