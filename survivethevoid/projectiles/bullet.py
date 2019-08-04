import pygame
from survivethevoid.utils.math_func import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen, x, y, angle, v):
        super(Bullet, self).__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle

        self.img = pygame.image.load('assets/images/bullet.png').convert()
        self.img = pygame.transform.scale(self.img, (5, 10))
        self.image = pygame.transform.rotate(self.img,
                                             self.angle)  # Pygame takes angle as degrees, while numpy as radians

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        radians = np.pi*(angle+90)/180.0
        self.v = np.array([self.speed*np.cos(radians), self.speed*np.sin(radians)]) + v
        self.start = pygame.time.get_ticks()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.v[0]
        self.y += self.v[1]
        now = pygame.time.get_ticks()

        if now - self.start > 60*50.0:
            self.kill()



