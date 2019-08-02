
import pygame
import numpy as np


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, name, screen,
                 location,
                 size,
                 v):
        super(Asteroid, self).__init__()
        self.name = name
        self.screen = screen
        self.x = location[0]
        self.y = location[1]
        self.v = v
        self.angle = 0
        self.size = size
        self.img = pygame.image.load(
            'survivethevoid/assets/images/asteroid_2.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

    def rotate(self, d_ang):
        self.angle += d_ang

        # Reinstantiate rotated image so that recurrent transformations don't warp object over time due to
        # floating point precision limitations.
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, *args):
        self.rotate(self.v[2])

        # True floating point positions.
        self.x += self.v[0]
        self.y += self.v[1]

        # The new center position is rounded because pygame can only take integers as positions.
        # self.rect.center = (round(self.x), round(self.y))

    def set_rect_center(self, location):
        self.rect.center = tuple(location)
        print(self.rect.center)

    def draw(self):
        self.screen.blit(self.image, self.rect)
