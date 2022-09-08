from Editor import Base
import pygame


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True
# объект игрока
player = Base.Player('player', None, 'player', Base.Transform(), 'sprites/main.png')
# объект заднего фона
background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'sprites/background.png')
# объект кнопки
button = Base.Button(lambda: print("clicked!!"), 'background', None, 'bg', Base.Transform(Base.Vector2(200, 200)), 'sprites/button.png')

while game:
    background.paint(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.on_click()
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    player.move(keys)
    # реакции на нажатия клавиш



    player.paint(screen)
    button.paint(screen)
    pygame.display.update()

pygame.quit()
exit()