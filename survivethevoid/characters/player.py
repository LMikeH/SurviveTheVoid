import pygame
import numpy as np
from survivethevoid.utils.math_func import *

class Player(pygame.sprite.Sprite):
    def __init__(self, name, screen, location):
        """
        This is the player class. It handles the assets for the player. It also controls the keys and functionality
        of the player.

        Parameters
        ----------
        screen: pygame display object
        this display allows for player object to be drawn.

        x: int
        x cartesian position

        y: int
        y cartesian position

        angle: float
        angle in degrees.


        """
        super(Player, self).__init__()
        self.name = name
        # Speed is vector with dx/dt, dy/dt, and d-angle/dt
        self.v = np.array([0.0, 0.0])
        self.omega = 0
        self.angle = location[2]-90
        self.screen = screen
        self.x = location[0]
        self.y = location[1]
        self.img = pygame.image.load('survivethevoid/assets/images/testcraft.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (50, 100))
        self.image = pygame.transform.rotate(self.img, self.angle-90)  # Pygame takes angle as degrees, while numpy as radians
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, screen.get_height()/2)

    def rotate(self, d_ang):
        """
        This function changes the angle by a small amount for the update

        Parameters
        ----------
        d_ang: float
        Change to be added to self.angle causing rotation

        """
        self.angle += d_ang

        # Reinstantiate rotated image so that recurrent transformations don't warp object over time due to
        # floating point precision limitations.
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def controls(self, key_state):
        """
        This function gives simple key controls to move the player object

        Parameters
        ----------
        key_state: pygame keystate enum object
        This is the signal processed by pygame specifying which key was pressed.

        Returns
        -------

        """
        self.a = np.array([0.0, 0.0])
        # Cartesian positions
        if key_state[pygame.K_a]:
            self.a[0] = .01
        elif key_state[pygame.K_d]:
            self.a[0] = -.01
        if key_state[pygame.K_w]:
            self.a[1] = .01
        elif key_state[pygame.K_s]:
            self.a[1] = -.01

        # Angles
        if key_state[pygame.K_q]:
            self.omega += .01
        elif key_state[pygame.K_e]:
            self.omega -= .01

    def update(self, key_state):
        """
        This function updates teh player object.
. m
        Parameters
        ----------
        key_state: pygame keystate enum object
        This is the signal processed by pygame specifying which key was pressed.

        Returns
        -------

        """
        self.controls(key_state)
        self.rotate(self.omega)
        new_a = np.dot(R(-self.angle), -self.a)
        # self.v += np.array([self.a[0]*np.sin(self.angle*np.pi/180)*-1, self.a[1]*np.cos(self.angle*np.pi/180)*-1])
        self.v += new_a
        # True floating point positions.
        self.x += self.v[0]  # s1 = s0 + dels, dels = v
        self.y += self.v[1]

        # The new center position is rounded because pygame can only take integers as positions.
        # self.rect.center = (round(self.x), round(self.y))

    def draw(self):
        """
        Draws player object

        Returns
        ------jl-

        """
        self.screen.blit(self.image, self.rect)
