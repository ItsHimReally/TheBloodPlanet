from Editor import Base
import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
pygame.mouse.set_visible(True)
pygame.display.set_caption('The Blood Planet')

# all_sprites = pygame.sprite.Group()
# platform_sprites = pygame.sprite.Group()
# enemy_sprites = pygame.sprite.Group()
# player_sprite = pygame.sprite.Sprite()
# дабл ять суккка как сделать эти коллизии несчастные какой же я дебил жить тяжело и неуютно


game = True
# объект игрока
player = Base.Player('player', None, 'player', Base.Transform(), 'sprites/main.png')
# объект заднего фона
background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'sprites/background.png')
# объект кнопки
# button = Base.Button(lambda: print("clicked!!"), 'background', None, 'bg', Base.Transform(Base.Vector2(200, 200)), 'sprites/button.png')
platform = Base.Platform('platform', None, 'platform', Base.Transform(Base.Vector2(500, 500)), 'sprites/platform.png')

while game:
    background.paint(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
    player.move(keys)
    # реакции на нажатия клавиш
    player.paint(screen)
    platform.paint(screen)
    pygame.display.update()
    clock.tick(144)

pygame.quit()