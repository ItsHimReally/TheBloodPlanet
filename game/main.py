from Editor import Base
import pygame


pygame.init()
screen = pygame.display.set_mode()
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True
# объект игрока
player = Base.SpriteObject('player', None, 'player', Base.Transform(), 'sprites/main.png')
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
            button.on_click(pygame.mouse.get_pos())
    pressed = pygame.mouse.get_pressed()[0]
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    # реакции на нажатия клавиш

    if keys[pygame.K_a]:
        player.transform.translate(-2)
    elif keys[pygame.K_d]:
        player.transform.translate(2)
    elif keys[pygame.K_w]:
        player.transform.translate(0, -2)

    player.paint(screen)
    button.paint(screen)
    pygame.display.update()

pygame.quit()
exit()