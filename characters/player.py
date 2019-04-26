import pygame
from characters._base_character import _BaseCharacter


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
        super(Player, self).__init__()
        # Speed is vector with dx/dt, dy/dt, and d-angle/dt
        self.speed = [0, 0, 0]
        self.angle = angle
        self.screen = screen
        self.x = x
        self.y = y
        self.img = pygame.image.load('assets/images/testcraft.png').convert()
        self.img = pygame.transform.scale(self.img, (25, 50))
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def rotate(self, d_ang):
        self.angle += d_ang
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def controls(self, key_state):
        if key_state[pygame.K_LEFT]:
            self.speed[0] -= .01
        elif key_state[pygame.K_RIGHT]:
            self.speed[0] += .01
        if key_state[pygame.K_UP]:
            self.speed[1] -= .01
        elif key_state[pygame.K_DOWN]:
            self.speed[1] += .01
        if key_state[pygame.K_a]:
            self.speed[2] -= .01
        elif key_state[pygame.K_d]:
            self.speed[2] += .01

    def update(self, key_state):
        self.controls(key_state)
        self.rotate(self.speed[2])
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.center = (round(self.x), round(self.y))


    def draw(self):
        self.screen.blit(self.image, self.rect)
