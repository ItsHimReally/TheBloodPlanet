from Editor import Base
import pygame
import menu


def is_clicked(click_rect, button_obj):
    if button_obj.sprite.get_rect()[2] + button_obj.sprite.get_rect()[2] >= click_rect[0] and \
                    click_rect[0] >= button_obj.sprite.get_rect()[2] and \
                    button_obj.transform.position.x + button_obj.sprite.get_rect()[3] >= click_rect[1] and \
                    click_rect[1] >= button_obj.transform.position.y:
        button_obj.on_click()


def start(screen):
    game = True
    # объект игрока
    player = Base.SpriteObject('player', None, 'player', Base.Transform(), 'sprites/main.png')
    # объект заднего фона
    background = Base.SpriteObject('background', None, 'bg', Base.Transform(), 'sprites/background.png')
    # объект кнопки
    button = Base.Button(is_clicked, 'background', None, 'bg', Base.Transform(Base.Vector2(500, 500)),
                         'sprites/button.png')

    platform = Base.SpriteObject('platform', None, 'platform', Base.Transform(Base.Vector2(200, 500)),
                                 'sprites/platform.png')

    while game:
        background.paint(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        pressed = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()  # клавиши, которые были нажаты
        # реакции на нажатия клавиш

        if pressed:
            is_clicked(pos, button)
        elif keys[pygame.K_a]:
            player.transform.translate(-2)
        elif keys[pygame.K_d]:
            player.transform.translate(2)
        elif keys[pygame.K_w]:
            player.transform.translate(0, -2)
        elif keys[pygame.K_ESCAPE]:
            menu.start_menu()
        player.transform.translate(0, 1)
        player.paint(screen)
        button.paint(screen)

        pygame.display.update()
    pygame.quit()
