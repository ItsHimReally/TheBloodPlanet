from Editor import Base
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(1)
pygame.display.set_caption('')

game = True

# Анимации

soilder_anim_walk = ['sprites/solider without parasite/shooter walk/1.png',
                     'sprites/solider without parasite/shooter walk/2.png',
                     'sprites/solider without parasite/shooter walk/3.png',
                     'sprites/solider without parasite/shooter walk/4.png',
                     'sprites/solider without parasite/shooter walk/5.png']

soilder_anim_die = ['sprites/solider without parasite/shooter die/1.png',
                    'sprites/solider without parasite/shooter die/2.png',
                    'sprites/solider without parasite/shooter die/3.png',
                    'sprites/solider without parasite/shooter die/4.png',
                    'sprites/solider without parasite/shooter die/5.png',
                    'sprites/solider without parasite/shooter die/6.png']

scientist_anim_walk = ['sprites/Scientist/Walk/1.png',
                       'sprites/Scientist/Walk/2.png',
                       'sprites/Scientist/Walk/3.png',
                       'sprites/Scientist/Walk/4.png',
                       'sprites/Scientist/Walk/5.png', ]

scientist_anim_die = ['sprites/Scientist/Die/1.png',
                      'sprites/Scientist/Die/2.png',
                      'sprites/Scientist/Die/3.png',
                      'sprites/Scientist/Die/4.png',
                      'sprites/Scientist/Die/5.png',
                      'sprites/Scientist/Die/6.png',
                      'sprites/Scientist/Die/7.png',
                      'sprites/Scientist/Die/8.png',
                      'sprites/Scientist/Die/9.png',
                      'sprites/Scientist/Die/10.png',
                      'sprites/Scientist/Die/11.png',
                      'sprites/Scientist/Die/12.png', ]

# объект игрока
multiplier = 5
player = Base.Player('player', None, 'player',
                     Base.Transform(Base.Vector2(600, 600), Base.Vector2(20 * multiplier, 17 * multiplier)),
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

pygame.mixer.music.load('audio/elementals.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.07)

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

room1 = Base.Room(background=background1, colliders=colliders1)

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
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 167), Base.Vector2(10, 100))),
]

enemy2 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(500, 800), Base.Vector2(70, 150)),
                    soilder_anim_walk,
                    enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(300, 546),
                    finish_vector=Base.Vector2(600, 555), enemy_animation_name='walk')

enemy2_1 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(500, 800), Base.Vector2(70, 150)),
                      soilder_anim_walk,
                      enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(900, 546),
                      finish_vector=Base.Vector2(1200, 555), enemy_animation_name='walk')

enemy1 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(800, 800), Base.Vector2(70, 150)),
                    soilder_anim_walk,
                    enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(800, 600),
                    finish_vector=Base.Vector2(1200, 600), enemy_animation_name='walk')

enemy2.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy2.add_animation('Die', soilder_anim_die, animation_delay=100, x_scale=200)

enemy2_1.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy2_1.add_animation('Die', soilder_anim_die, animation_delay=100, x_scale=200)

room2 = Base.Room(background2, [enemy2, enemy2_1], colliders=colliders2)

multiplier = 4

background3 = Base.SpriteObject('background', None, 'bg',
                                Base.Transform(Base.Vector2(0, 0), Base.Vector2(416 * multiplier, 232 * multiplier)),
                                'sprites/Levels/Level_2.png')

colliders3 = [
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1595, 65), Base.Vector2(4, 194))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 863), Base.Vector2(726, 34))),
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(704, 775), Base.Vector2(895, 130))),
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

multiplier = 3
enemy3 = Base.Enemy('Enemy', None, 'Enemy',
                    Base.Transform(Base.Vector2(500, 500), Base.Vector2(32 * multiplier, 48 * multiplier)),
                    scientist_anim_walk,
                    enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(500, 237),
                    finish_vector=Base.Vector2(300, 237), enemy_animation_name='walk', enemy_type='scientist')
enemy3.add_animation('idle', ['sprites/Scientist/idle.png'], 150, False)
enemy3.add_animation('Die', scientist_anim_die, animation_delay=100, x_scale=200)

enemy3_1 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(800, 230), Base.Vector2(70, 150)),
                      soilder_anim_walk,
                      enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(700, 230),
                      finish_vector=Base.Vector2(1000, 230), enemy_animation_name='walk')

enemy3_2 = Base.Enemy('Enemy', None, 'Enemy', Base.Transform(Base.Vector2(800, 640), Base.Vector2(70, 150)),
                      soilder_anim_walk,
                      enemy_obj_velocity_x=2, enemy_obj_velocity_y=0, start_vector=Base.Vector2(700, 640),
                      finish_vector=Base.Vector2(1000, 640), enemy_animation_name='walk')

enemy3_1.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy3_1.add_animation('Die', soilder_anim_die, animation_delay=100, x_scale=200)

enemy3_2.add_animation('idle', ['sprites/solider without parasite/sidle.png'], 150, False)
enemy3_2.add_animation('Die', soilder_anim_die, animation_delay=100, x_scale=200)

room3 = Base.Room(background3, [enemy3, enemy3_1, enemy3_2], colliders=colliders3)

colliders4 = [
    Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 899), Base.Vector2(1600, 10))),
]
multiplier = 6
background4 = Base.SpriteObject('background', None, 'bg',
                                Base.Transform(Base.Vector2(0, 0), Base.Vector2(315 * multiplier, 136 * multiplier)),
                                'sprites/Levels/Level_3.png')

room4 = Base.Room(background=background4, colliders=colliders4)

exit1 = [Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1599, 172), Base.Vector2(10, 80))),
         room2, (3, 169)]
exit2 = [Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1596, 279), Base.Vector2(10, 400))),
         room3, (1500, 150)]
exit3 = [Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1257, 535), Base.Vector2(274, 180))),
         room4, (800, 800)]
room1.set_exit(exit1)
room2.set_exit(exit2)
room3.set_exit(exit3)
room4.set_exit(exit1)

level1 = Base.Level([room1, room2, room3])
level1.current_room = room1

a = 0
b = 0

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

text_surface = my_font.render('You are a loh', False, (0, 0, 0))

while game:
    screen.fill((77, 74, 92))

    if not player.is_alive:
        screen.blit(text_surface, (600, 400))
        pygame.display.update()
        clock.tick(200)
        continue

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