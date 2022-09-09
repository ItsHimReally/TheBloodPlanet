import game
import settings
import pygame
import pygame_menu


def start_game():
    game.start(screen)


def start_settings():
    settings.start(screen)


def start_menu():
    global screen
    screen = pygame.display.set_mode()
    menu = pygame_menu.Menu('Welcome', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Play', start_game)
    menu.add.button('Settings', start_settings)
    menu.add.button('Quit', end_session)

    menu.mainloop(screen)


def end_session():
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mouse.set_visible(1)
    pygame.display.set_caption('')
    start_menu()
