from dice import all

pygame.init()
screen = pygame.display.set_mode((800, 700))

#carrega gráfico do dado
dice.loadDiceSprites()
#seta dado como botão
dice.configuraDiceButton()
#animaDado
dice.animaDado()

run = True
dado = dice.rollDice()
print(dado)
while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    dice.showDice()

    pygame.display.update()
