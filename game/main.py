from Editor import Base
import pygame


pygame.init()
screen = pygame.display.set_mode()
pygame.mouse.set_visible(0)
pygame.display.set_caption('')

game = True
player = Base.SpriteObject('player', None, 'player', Base.Transform(), 'C:/Users\Danya/RedPlanet-Game/sprites/main.png')

while game:
    screen.fill([0, 0, 0])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    player.transform.translate(2)
    player.paint(screen)
    pygame.display.update()
pygame.quit()
exit()

