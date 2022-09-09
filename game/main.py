from Editor import Base
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))
pygame.mouse.set_visible(True)
pygame.display.set_caption('')

game = True
player = Base.Player('player', None, 'player', Base.Transform(Base.Vector2(300, 800), Base.Vector2(100, 60)),
                     ['sprites\Slime\Idle\idle_0.png', 'sprites\Slime\Idle\idle_1.png', 'sprites\Slime\Idle\idle_2.png',
                      'sprites\Slime\Idle\idle_3.png', 'sprites\Slime\Idle\idle_4.png'])
background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'sprites/background.png')

platform = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(0, 700), Base.Vector2(272, 249)),
                              'sprites/1.png')
platform1 = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(1000, 700), Base.Vector2(272, 249)),
                              'sprites/1.png')
platform2 = Base.SpriteObject('testObject', None, 'to', Base.Transform(Base.Vector2(500, 400), Base.Vector2(272, 249)),
                              'sprites/1.png')

while game:
    background.paint(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.check_collision(platform)
    player.check_collision(platform1)
    player.check_collision(platform2)
    platform.paint(screen)
    platform1.paint(screen)
    platform2.paint(screen)
    player.paint(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
