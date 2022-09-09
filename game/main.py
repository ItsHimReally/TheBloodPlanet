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
multiplier = 5
background = Base.SpriteObject('background', None, 'bg', Base.Transform(Base.Vector2(0, 0), Base.Vector2(384 * multiplier, 176 * multiplier)), 'sprites/Levels/level2.png')
# объект кнопки
# button = Base.Button(lambda: print("clicked!!"), 'background', None, 'bg', Base.Transform(Base.Vector2(200, 200)), 'sprites/button.png')
ceil = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 240)), 'sprites/1.png')
floor = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 640), Base.Vector2(1600, 450)), 'sprites/1.png')
level_objects = [ceil, floor]
while game:
    background.paint(screen)
    # pygame.draw.rect(screen, (0, 255, 255), background.rect)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     button.on_click()
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    player.move(keys)
    # реакции на нажатия клавиш
    # rectangle.paint(screen)
    a = [False, False, False, False]
    for level_object in level_objects:
        a = player.check_collision(level_object, a)
        player.collisions = a
    # pygame.draw.rect(screen, (255, 0, 0), ceil.rect)
    # pygame.draw.rect(screen, (0, 0, 255), floor.rect)
    # pygame.draw.rect(screen, (0, 0, 255), player.rect)
    player.paint(screen)
    # button.paint(screen)
    print(player.collisions)
    pygame.display.update()
    clock.tick(60)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        pygame.exit()
        break

pygame.quit()
exit()