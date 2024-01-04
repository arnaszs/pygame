import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Super Runner')
clock = pygame.time.Clock() # Tells game that it has to run at 60fps in while loop.

sky_surface = pygame.image.load('learning/pixelart/Package/Sprites/Game Objects/Background.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))

    # draw all our elements and update everything
    pygame.display.update()
    clock.tick(60)