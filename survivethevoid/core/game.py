import pygame
from survivethevoid.characters.player import Player
from survivethevoid.environment.asteroids import Asteroid
from survivethevoid.core.world import World
# from survivethevoid.core.world import World
import time
import numpy as np
import random
# from survivethevoid.environment.Camera import Camera

# Setup
corerandom = random.Random()


class Game(object):
    def __init__(self):
        """
        This is the overall game class which controls events, players, and non-players.

        Parameters
        ----------
        screen: pygame display object
        passes in the display so sprites can be drawn.

        """
        # Setup Variables
        self.time = time.time()
        self.clock = 0
        self.ticks = 0

        # Setup PyGame
        pygame.init()

        # Setup Screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.background = pygame.Surface((pygame.display.Info().current_w, pygame.display.Info().current_h))
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        pygame.display.update()

        # Setup World
        self.world = World(10000, 10000, self.screen, self.screen.get_width()*3)

    def check_world_objects(self):
        start_objects = self.world.check_influence()
        for obj in start_objects:
            if obj == 'player':
                self.player = Player(obj, self.screen, self.world.objects[obj]['location'])
                self.characters.add(self.player)
                self.world.camera.player = self.player
                self.world.objects[obj]['object'] = self.player
            elif 'asteroid' in obj:
                asteroid = Asteroid(obj, self.screen,
                                    self.world.objects[obj]['location'],
                                    np.random.randint(50, 200),
                                    .2 * np.random.random(3) - .1
                                    )
                self.world.objects[obj]['object'] = asteroid
                self.asteroids.add(asteroid)
        self.world.check_camera([self.characters, self.projectiles, self.asteroids], self.camera_group)

    def start_level(self):
        """
        Create
        """
        # Setup Objects
        self.characters = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.camera_group = pygame.sprite.Group()
        self.check_world_objects()

    def run(self):
        """
        This is the game loop

        """
        # Time
        clock = pygame.time.Clock()

        # Game Loop
        done = False
        while not done:
            self.handle_events()
            self.update(pygame.key.get_pressed())
            self.draw()
            pygame.display.flip()

    def update(self, keys):
        """
        This function updates everything based on events that occur.

        Parameters
        ----------
        keys

        Returns
        -------

        """
        self.camera_group.empty()
        self.characters.update(keys)
        self.world.update()
        self.check_world_objects()
        print(self.camera_group)
        self.asteroids.update()
        self.projectiles.update()
        self.collision_check()

    def draw(self):
        """
        This function draws all of the groups.

        Returns
        -------

        """
        self.screen.blit(self.background, (0, 0))
        self.camera_group.draw(self.screen)

    def collision_check(self):
        col = pygame.sprite.groupcollide(self.characters, self.asteroids, True, False, pygame.sprite.collide_mask)
        if col != []:
            for obj in col:
                del self.world.objects[obj.name]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
