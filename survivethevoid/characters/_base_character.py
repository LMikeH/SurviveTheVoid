
import pygame

class _BaseCharacter(pygame.sprite.Sprite):
    def __init__(self, name, screen, location):
        self.name = name
        self.x = location[0]
        self.y = location[1]
        self.angle = location[2]
        self.screen = screen

