from Editor import Base
import pygame


def is_clicked(button_rect, click_rect):
    if button_rect.collidepoint(click_rect):
        button.on_click()


pygame.init()
screen = pygame.display.set_mode()
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True
# объект игрока
player = Base.SpriteObject('player', None, 'player', Base.Transform(), 'C:/Users\Danya/RedPlanet-Game/sprites/main.png')
# объект заднего фона
background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'C:/Users\Danya/RedPlanet-Game/sprites/background.png')
# объект кнопки
button = Base.Button(is_clicked, 'background', None, 'bg', Base.Transform(Base.Vector2(200, 200)), 'C:/Users\Danya/RedPlanet-Game/sprites/button.png')

while game:
    background.paint(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pressed = pygame.mouse.get_pressed()[0]
    pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    # реакции на нажатия клавиш

    if pressed:
        is_clicked(button.sprite.get_rect(), pos)
    elif keys[pygame.K_a]:
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