import pygame.draw


class snowbeing:
    def __init__(self, surface):
        self.mainsurface = surface
        pygame.init()

    def body(self):
        pygame.draw.circle(self.mainsurface, (255, 255, 255), (300, 320), 80)
        pygame.draw.circle(self.mainsurface, (255, 255, 255), (300, 200), 60)
        pygame.draw.circle(self.mainsurface, (255, 255, 255), (300, 110), 40)
        pygame.display.update()

    def hat(self):
        pygame.draw.rect(self.mainsurface, (0, 0, 0), (270, 5, 60, 60))
        pygame.draw.rect(self.mainsurface, (0, 0, 0), (250, 60, 100, 20))
        pygame.display.update()
