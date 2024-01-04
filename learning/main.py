import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption('Super Runner')
clock = pygame.time.Clock() # Tells game that it has to run at 60fps in while loop.

sky_surface = pygame.image.load('learning/pixelart/Package/Sprites/Game Objects/Background.png').convert_alpha()
ground_surface = pygame.image.load('learning/pixelart/Package/Sprites/Game Objects/Foreground.png').convert_alpha()
trap1_surface = pygame.image.load('learning/pixelart/Package/Sprites/Game Objects/Obstacle_1.png').convert_alpha()


resized_sky = pygame.transform.scale(sky_surface, (1280, 800))
resized_ground = pygame.transform.scale(ground_surface, (1280, 800))
resized_trap1 = pygame.transform.scale(trap1_surface, (100, 75))


trap1_x_pos = 1280


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(resized_sky, (0, 0))
    screen.blit(resized_ground, (0, 0))
    trap1_x_pos -= 7
    if trap1_x_pos < -100: trap1_x_pos = 1280
    screen.blit(resized_trap1, (trap1_x_pos, 600))

    # draw all our elements and update everything
    pygame.display.update()
    clock.tick(60)