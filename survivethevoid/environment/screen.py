
import pygame

class screen:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.size = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def draw(self):
        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))

    def update(self):
