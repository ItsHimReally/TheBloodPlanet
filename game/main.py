from Editor import Base
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True

# объект игрока
multiplier = 5
player = Base.Player('player', None, 'player', Base.Transform(Base.Vector2(0, 0), Base.Vector2(20 * multiplier, 17 * multiplier)),
                     ['sprites/Slime/Idle/idle_0.png', 'sprites/Slime/Idle/idle_1.png', 'sprites/Slime/Idle/idle_2.png',
                      'sprites/Slime/Idle/idle_3.png', 'sprites/Slime/Idle/idle_4.png'])
player_jump_animation = []

for i in range(17):
    player_jump_animation.append(f'sprites/Slime/Jump/jump_{i}.png')

player.add_animation('jump', player_jump_animation, 50)

# объект заднего фона
multiplier = 5
background = Base.SpriteObject('background', None, 'bg',
                               Base.Transform(Base.Vector2(0, 0), Base.Vector2(384 * multiplier, 176 * multiplier)),
                               'sprites/Levels/level2.png')

ceil = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 240)),
                         'sprites/1.png')
floor = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 640), Base.Vector2(1600, 450)),
                          'sprites/1.png')
level_objects = [ceil, floor]

# создаем врага
enemy = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(500, 500), Base.Vector2(70, 150)),
                   ['sprites/solider without parasite/shooter walk/1.png',
                    'sprites/solider without parasite/shooter walk/2.png',
                    'sprites/solider without parasite/shooter walk/3.png',
                    'sprites/solider without parasite/shooter walk/4.png',
                    'sprites/solider without parasite/shooter walk/5.png'],
                   enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(300, 488),
                   finish_vector=Base.Vector2(500, 488), enemy_animation_name='walk')
enemy.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy.add_animation('Die', ['sprites/solider without parasite/shooter die/1.png',
                            'sprites/solider without parasite/shooter die/2.png',
                            'sprites/solider without parasite/shooter die/3.png',
                            'sprites/solider without parasite/shooter die/4.png',
                            'sprites/solider without parasite/shooter die/5.png',
                            'sprites/solider without parasite/shooter die/6.png'], animation_delay=100, x_scale=200)
enemies = [enemy]
paintable_objects = [enemy, player]
colliders = [ceil, floor]
# level1 = Base.Level(background, enemies, colliders)
# Base.Level.set_level(level1)
room1 = Base.Room(background, enemies, colliders)
level1 = Base.Level([room1])
while game:
    background.paint(screen)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player.take_control()

    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты

    # реакции на нажатия клавиш

    Base.Level.get_level().current_room.logic(screen, player, keys)

    pygame.display.update()
    clock.tick(60)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
        break

pygame.quit()
exit()


# while game:
#     background.paint(screen)
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             game = False
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_e:
#                 if player.host is None:
#                     for enemy in enemies:
#                         if player.check_collision(enemy) and not enemy.dead:
#                             player.host = enemy
#                             enemy.infected = True
#                             player.activeSelf = False
#                             enemy.transform.velocity_x = player.transform.velocity_x
#                 else:
#                     player.activeSelf = True
#                     player.host.infected = False
#                     player.host.die()
#                     player.transform.translate(player.host.transform.position.x - player.transform.position.x,
#                                                player.host.transform.position.y - player.transform.position.y)
#                     player.host = None
#
#
#     keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
#     player.logic(keys)
#     enemy.move(keys)
#
#     # реакции на нажатия клавиш
#
#     a = [False, False, False, False]
#     b = [False, False, False, False]
#     for level_object in level_objects:
#         if player.host is None:
#             a = player.process_collision(level_object, a)
#             player.collisions = a
#         else:
#             a = player.host.process_collision(level_object, a)
#             player.host.collisions = a
#
#
#     for item in paintable_objects:
#         item.paint(screen)
#     pygame.display.update()
#     clock.tick(60)
#     if keys[pygame.K_ESCAPE]:
#         pygame.quit()
#         pygame.exit()
#         break
#
# pygame.quit()
# exit()