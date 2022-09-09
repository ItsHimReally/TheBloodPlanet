from Editor import Base
import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True
# объект игрока
player = Base.Player('player', None, 'player', Base.Transform(Base.Vector2(0, 0), Base.Vector2(100, 85)), ['sprites\Slime\Idle\idle_0.png', 'sprites\Slime\Idle\idle_1.png', 'sprites\Slime\Idle\idle_2.png', 'sprites\Slime\Idle\idle_3.png', 'sprites\Slime\Idle\idle_4.png'])
player_jump_animation = []
for i in range(17):
    player_jump_animation.append(f'sprites/Slime/Jump/jump_{i}.png')
player.add_animation('jump', player_jump_animation, 50)
# объект заднего фона
background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'sprites/background.png')
# объект кнопки
# button = Base.Button(lambda: print("clicked!!"), 'background', None, 'bg', Base.Transform(Base.Vector2(200, 200)), 'sprites/button.png')
rectangle = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(100, 700), Base.Vector2(272, 249)), 'sprites/1.png')
rectangle1 = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(500, 700), Base.Vector2(272, 249)), 'sprites/1.png')
rectangle2 = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 350), Base.Vector2(500, 220)), 'sprites/1.png')
while game:
    background.paint(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     button.on_click()
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    player.move(keys)
    # реакции на нажатия клавиш
    # rectangle.paint(screen)
    a = False
    if not player.check_collision(rectangle) and not player.check_collision(rectangle1) and not player.check_collision(rectangle2):
        player.collisions = [False, False, False, False]
    pygame.draw.rect(screen, (255, 0, 0), rectangle.rect)
    pygame.draw.rect(screen, (0, 0, 255), rectangle1.rect)
    pygame.draw.rect(screen, (255, 0, 255), rectangle2.rect)
    pygame.draw.rect(screen, (0, 0, 255), player.rect)
    player.paint(screen)

    # button.paint(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()