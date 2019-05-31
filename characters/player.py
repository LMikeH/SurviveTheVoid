import pygame
from characters._base_character import _BaseCharacter


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
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
        # Speed is vector with dx/dt, dy/dt, and d-angle/dt
        self.speed = [0, 0, 0]
        self.angle = angle
        self.screen = screen
        self.x = x
        self.y = y
        self.img = pygame.image.load('assets/images/testcraft.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (50, 100))
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def rotate(self, d_ang):
        """
        This funtion changes the angle by a small amount for the update

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

        # Cartesian positions
        if key_state[pygame.K_LEFT]:
            self.speed[0] -= .01
        elif key_state[pygame.K_RIGHT]:
            self.speed[0] += .01
        if key_state[pygame.K_UP]:
            self.speed[1] -= .01
        elif key_state[pygame.K_DOWN]:
            self.speed[1] += .01

        # Angles
        if key_state[pygame.K_a]:
            self.speed[2] -= .01
        elif key_state[pygame.K_d]:
            self.speed[2] += .01

    def update(self, key_state):
        """
        This function updates teh player object.

        Parameters
        ----------
        key_state: pygame keystate enum object
        This is the signal processed by pygame specifying which key was pressed.

        Returns
        -------

        """
        self.controls(key_state)
        self.rotate(self.speed[2])

        # True floating point positions.
        self.x += self.speed[0]
        self.y += self.speed[1]

        # The new center position is rounded because pygame can only take integers as positions.
        self.rect.center = (round(self.x), round(self.y))


    def draw(self):
        """
        Draws player object

        Returns
        -------

        """
        self.screen.blit(self.image, self.rect)
