import pygame as pg
from pygame import font

pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

def select_number():
    done = False
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render('Qual o número de jogadores?', True, green)
    screen.blit(text, (100, 100))
    rect2 = pg.Rect(150, 300, 30, 30)
    text2 = '2'
    txt_surface2 = FONT.render(text2, True, blue)
    screen.blit(txt_surface2, (150 + 5, 300 + 5))
    pg.draw.rect(screen, blue, rect2, 2)
    rect3 = pg.Rect(250, 300, 30, 30)
    text3 = '3'
    txt_surface3 = FONT.render(text3, True, blue)
    screen.blit(txt_surface3, (250 + 5, 300 + 5))
    pg.draw.rect(screen, blue, rect3, 2)
    rect4 = pg.Rect(350, 300, 30, 30)
    text4 = '4'
    txt_surface4 = FONT.render(text4, True, blue)
    screen.blit(txt_surface4, (350 + 5, 300 + 5))
    pg.draw.rect(screen, blue, rect4, 2)
    pg.display.flip()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect2.collidepoint(event.pos):
                    return text2

                elif rect3.collidepoint(event.pos):
                    return text3

                elif rect4.collidepoint(event.pos):
                    return text4

def submit():

    done = False
    blue = (0, 0, 128)
    rect2 = pg.Rect(150, 300, 30, 30)
    text2 = 'Submit'
    txt_surface2 = FONT.render(text2, True, blue)
    screen.blit(txt_surface2, (150 + 5, 300 + 5))
    pg.draw.rect(screen, blue, rect2, 2)
    for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect2.collidepoint(event.pos):
                    print(text2)
                    return True
            else:
                return False

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)



def main():
    quant = select_number()
    print(quant)
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_boxes = [input_box1]
    done = False


    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()


        screen.fill((30, 30, 30))

        for box in input_boxes:
            box.draw(screen)
        pg.display.flip()
        clock.tick(30)




if __name__ == '__main__':
    main()
    pg.quit()
