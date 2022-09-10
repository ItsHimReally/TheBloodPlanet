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
player = Base.Player('player', None, 'player', Base.Transform(Base.Vector2(1400, 170), Base.Vector2(20 * multiplier, 17 * multiplier)),
                     ['sprites/Slime/Idle/idle_0.png', 'sprites/Slime/Idle/idle_1.png', 'sprites/Slime/Idle/idle_2.png',
                      'sprites/Slime/Idle/idle_3.png', 'sprites/Slime/Idle/idle_4.png'])
player_jump_animation = []

for i in range(17):
    player_jump_animation.append(f'sprites/Slime/Jump/jump_{i}.png')

player.add_animation('jump', player_jump_animation, 50)

# объект заднего фона
multiplier = 5
background1 = Base.SpriteObject('background', None, 'bg',
                               Base.Transform(Base.Vector2(29, 100), Base.Vector2(315 * multiplier, 136 * multiplier)),
                               'sprites/Levels/Level_0.png')

# ceil = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 170)))
# floor = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 700), Base.Vector2(1600, 450)))
# floor_vent = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(180, 257), Base.Vector2(1437, 42)))
# left_wall = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 170), Base.Vector2(82, 699)))
# right_wall = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1520, 257), Base.Vector2(81, 447)))
# box_right = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1364, 620), Base.Vector2(85, 81)))
# capsule_right = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1444, 539), Base.Vector2(77, 159)))
# создаем врага
enemy1 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(500, 500), Base.Vector2(70, 150)),
                   ['sprites/solider without parasite/shooter walk/1.png',
                    'sprites/solider without parasite/shooter walk/2.png',
                    'sprites/solider without parasite/shooter walk/3.png',
                    'sprites/solider without parasite/shooter walk/4.png',
                    'sprites/solider without parasite/shooter walk/5.png'],
                   enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(300, 225),
                   finish_vector=Base.Vector2(500, 488), enemy_animation_name='walk')
enemy1.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy1.add_animation('Die', ['sprites/solider without parasite/shooter die/1.png',
                            'sprites/solider without parasite/shooter die/2.png',
                            'sprites/solider without parasite/shooter die/3.png',
                            'sprites/solider without parasite/shooter die/4.png',
                            'sprites/solider without parasite/shooter die/5.png',
                            'sprites/solider without parasite/shooter die/6.png'], animation_delay=100, x_scale=200)
# colliders = [floor, ceil, left_wall, right_wall, floor_vent, box_right]
colliders1 = [
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 170))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 700), Base.Vector2(1600, 450))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(180, 257), Base.Vector2(1437, 42))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 170), Base.Vector2(82, 699))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1520, 300), Base.Vector2(81, 447))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1364, 620), Base.Vector2(85, 81))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1444, 539), Base.Vector2(77, 161))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(82, 460), Base.Vector2(82, 240))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(163, 620), Base.Vector2(161, 80))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(183, 544), Base.Vector2(81, 76))),
]

room1 = Base.Room(background1, [enemy1], colliders=colliders1)

multiplier = 5
background2 = Base.SpriteObject('background', None, 'bg',
                               Base.Transform(Base.Vector2(0, 100), Base.Vector2(416 * multiplier, 136 * multiplier)),
                               'sprites/Levels/Level_1.png')

colliders2 = [
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(520, 164))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(498, 0), Base.Vector2(1120, 275))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 256), Base.Vector2(398, 41))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 297), Base.Vector2(68, 433))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(61, 698), Base.Vector2(1540, 58))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(80, 544), Base.Vector2(80, 80))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(80, 619), Base.Vector2(160, 90))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1515, 620), Base.Vector2(90, 100))),
]

enemy2 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(500, 500), Base.Vector2(70, 150)),
                   ['sprites/solider without parasite/shooter walk/1.png',
                    'sprites/solider without parasite/shooter walk/2.png',
                    'sprites/solider without parasite/shooter walk/3.png',
                    'sprites/solider without parasite/shooter walk/4.png',
                    'sprites/solider without parasite/shooter walk/5.png'],
                   enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(300, 225),
                   finish_vector=Base.Vector2(500, 488), enemy_animation_name='walk')
enemy2.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy2.add_animation('Die', ['sprites/solider without parasite/shooter die/1.png',
                            'sprites/solider without parasite/shooter die/2.png',
                            'sprites/solider without parasite/shooter die/3.png',
                            'sprites/solider without parasite/shooter die/4.png',
                            'sprites/solider without parasite/shooter die/5.png',
                            'sprites/solider without parasite/shooter die/6.png'], animation_delay=100, x_scale=200)
# colliders = [floor, ceil, left_wall, right_wall, floor_vent, box_right]
colliders1 = [
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 170))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 700), Base.Vector2(1600, 450))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(180, 257), Base.Vector2(1437, 42))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 170), Base.Vector2(82, 699))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1520, 300), Base.Vector2(81, 447))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1364, 620), Base.Vector2(85, 81))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1444, 539), Base.Vector2(77, 161))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(82, 460), Base.Vector2(82, 240))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(163, 620), Base.Vector2(161, 80))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(183, 544), Base.Vector2(81, 76))),
]

room2 = Base.Room(background2, [enemy2], colliders=colliders2)

multiplier = 4

background3 = Base.SpriteObject('background', None, 'bg',
                               Base.Transform(Base.Vector2(0, 0), Base.Vector2(416 * multiplier, 232 * multiplier)),
                               'sprites/Levels/Level_2.png')

colliders3 = [
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 863), Base.Vector2(726, 34))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(704, 769), Base.Vector2(895, 130))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 768), Base.Vector2(639, 22))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(61, 770))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 0), Base.Vector2(1600, 63))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(257, 384), Base.Vector2(1345, 64))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(40, 507), Base.Vector2(88, 270))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(120, 635), Base.Vector2(75, 150))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(194, 704), Base.Vector2(62, 65))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1536, 256), Base.Vector2(66, 130))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1471, 320), Base.Vector2(66, 64))),
]

room3 = Base.Room(background3, [enemy1], colliders=colliders3)

exit1 = [Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1599, 172), Base.Vector2(10, 80))), room2, (3, 169)]
room1.set_exit(exit1)
room2.set_exit(exit1)

level1 = Base.Level([room1, room2, room3])
level1.current_room = room1
# room2 =
# room3 =

a = 0
b = 0
while game:
    screen.fill((77, 74, 92))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player.take_control()

        if event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()[0] - a
            b = pygame.mouse.get_pos()[1] - b
            print(f'({a}, {b})')


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