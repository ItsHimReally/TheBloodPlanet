from Editor import Base
import menu
import pygame
import pygame_menu


def end_session():
    pygame.quit()


def return_to_menu():
    menu.start_menu()


def start(screen):
    menu = pygame_menu.Menu('Settings', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Return', return_to_menu)
    menu.add.button('Quit', end_session)
    menu.mainloop(screen)