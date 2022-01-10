import bounce
import pygame, sys
from pygame.locals import *


pygame.init()
main_surface = pygame.display.set_mode((400, 600), 0, 32)
main_surface.fill((255, 255, 255))
b = bounce.Bounce(main_surface)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main_surface.fill((255, 255, 255))
    b.move()
    main_surface.blit(b.image, b.rect)
    pygame.display.update()