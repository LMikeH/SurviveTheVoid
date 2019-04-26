
import pygame

class _BaseCharacter(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
        self.x = x
        self.y = y
        self.theta = angle
        self.screen = screen