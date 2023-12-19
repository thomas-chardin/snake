import pygame
import sys

pygame.init()

ecran = pygame.display.set_mode((300, 200))

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
        elif event.type == pygame.QUIT:
            continuer = False

    pygame.display.flip()
    pygame.display.set_caption("Snake")

pygame.quit()
sys.exit()