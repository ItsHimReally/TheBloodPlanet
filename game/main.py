from Editor import Base
import pygame


pygame.init()
screen = pygame.display.set_mode()
pygame.mouse.set_visible(0)
pygame.display.set_caption('')

game = True
# объект игрока
player = Base.SpriteObject('player', None, 'player', Base.Transform(), 'C:/Users\Danya/RedPlanet-Game/sprites/main.png')

while game:
    screen.fill([0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    # реакции на нажатия клавиш
    if keys[pygame.K_a]:
        player.transform.translate(-2)
    elif keys[pygame.K_d]:
        player.transform.translate(2)
    elif keys[pygame.K_w]:
        player.transform.translate(0, -2)

    player.paint(screen)
    pygame.display.update()

pygame.quit()
exit()

