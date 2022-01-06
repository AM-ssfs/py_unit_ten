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

    def draw_snowflake(self, pos):

        x = pos[0]
        y = pos[1]
        w = 15
        width = 3
        white = (255, 255, 255)
        pygame.draw.line(self.mainsurface, white, (x, y), (x + w, y + w), width)
        pygame.draw.line(self.mainsurface, white, (x + w/2, y), (x + w/2, y + w), width)
        pygame.draw.line(self.mainsurface, white, (x + w, y), (x, y + w), width)
        pygame.draw.line(self.mainsurface, white, (x, y + w/2), (x + w, y + w/2), width)


