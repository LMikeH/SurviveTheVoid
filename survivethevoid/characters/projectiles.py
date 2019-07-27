import pygame
from survivethevoid.utils.__main__ import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 5
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x,self.y), self.radius)

    
    def update(self, key_state):
        if key_state[pygame.K_SPACE]

