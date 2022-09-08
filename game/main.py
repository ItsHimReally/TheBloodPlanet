from Editor import Base
import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True
# объект игрока
player = Base.Player('player', None, 'player', Base.Transform(Base.Vector2(100, 100), Base.Vector2(100, 60)), ['sprites\Slime\Idle\idle_0.png', 'sprites\Slime\Idle\idle_1.png', 'sprites\Slime\Idle\idle_2.png', 'sprites\Slime\Idle\idle_3.png', 'sprites\Slime\Idle\idle_4.png'])
# player.add_animation('second', ['sprites/1.png', 'sprites/2.png'], 1000)
# player.set_animation('second', )
# объект заднего фона
background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'sprites/background.png')
# объект кнопки
# button = Base.Button(lambda: print("clicked!!"), 'background', None, 'bg', Base.Transform(Base.Vector2(200, 200)), 'sprites/button.png')
rectangle = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(272, 249)), 'sprites/1.png')
while game:
    background.paint(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     button.on_click()
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    player.move(keys)
    if player.check_collision(rectangle):
        print("okay")
    # реакции на нажатия клавиш
    rectangle.paint(screen)
    player.paint(screen)

    # button.paint(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()