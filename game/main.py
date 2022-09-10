from Editor import Base
import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True

# объект игрока
player = Base.Player('player', None, 'player', Base.Transform(Base.Vector2(0, 0), Base.Vector2(100, 85)), ['sprites/Slime/Idle/idle_0.png', 'sprites/Slime/Idle/idle_1.png', 'sprites/Slime/Idle/idle_2.png', 'sprites/Slime/Idle/idle_3.png', 'sprites/Slime/Idle/idle_4.png'])
player_jump_animation = []

for i in range(17):
    player_jump_animation.append(f'sprites/Slime/Jump/jump_{i}.png')

player.add_animation('jump', player_jump_animation, 50)

# объект заднего фона
multiplier = 5
background = Base.SpriteObject('background', None, 'bg', Base.Transform(Base.Vector2(0, 0), Base.Vector2(384 * multiplier, 176 * multiplier)), 'sprites/Levels/level2.png')

ceil = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 240)), 'sprites/1.png')
floor = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 640), Base.Vector2(1600, 450)), 'sprites/1.png')
level_objects = [ceil, floor]

# создаем врага
enemy = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(500, 500), Base.Vector2(70, 150)),
                   ['sprites/solider without parasite/shooter walk/1.png', 'sprites/solider without parasite/shooter walk/2.png',
                    'sprites/solider without parasite/shooter walk/3.png', 'sprites/solider without parasite/shooter walk/4.png',
                    'sprites/solider without parasite/shooter walk/5.png'],
                   enemy_obj_velocity_x=10, enemy_obj_velocity_y=0, start_vector=Base.Vector2(300, 488),
                   finish_vector=Base.Vector2(500, 488))


painted_objects = [enemy, player]

while game:
    background.paint(screen)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    player.move(keys)
    enemy.move()

    # реакции на нажатия клавиш

    a = [False, False, False, False]
    for level_object in level_objects:
        a = player.process_collision(level_object, a)
        player.collisions = a
    for item in painted_objects:
        item.paint(screen)

    pygame.display.update()
    clock.tick(60)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        pygame.exit()
        break

pygame.quit()
exit()