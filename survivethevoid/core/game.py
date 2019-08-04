import pygame
from survivethevoid.characters.player import Player
from survivethevoid.environment.asteroids import Asteroid
from survivethevoid.core.world import World
# from survivethevoid.core.world import World
import time
import numpy as np
import random
import sys
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
        self.clock = pygame.time.Clock()
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
        """
        This method checks world object dictionary to see if characters and
        environment props are within sphere of influence to initialize objects.

        Also checks camera.

        """
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
                                    .4 * np.random.random(3) - .2
                                    )
                self.world.objects[obj]['object'] = asteroid
                self.asteroids.add(asteroid)
        self.world.check_camera([self.characters,
                                 self.projectiles,
                                 self.asteroids],
                                self.camera_group)

    def start_level(self):
        """
        Initialize groups, add objects within player's influence to
        the game.

        """
        self.characters = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.camera_group = pygame.sprite.Group()
        self.check_world_objects()

    def run(self):
        """
        This is the game loop

        """
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
        self.characters.update(keys, self.projectiles)
        self.world.update()
        self.check_world_objects()
        self.asteroids.update()
        self.projectiles.update()
        self.collision_check()

    def draw(self):
        """
        This function draws all of the groups.

        Returns
        -------

        """
        myfont = pygame.font.SysFont('monospace', 15)
        label1 = myfont.render("Coordinates: {} {} ".format('%.2f' % self.player.x, '%.2f' % self.player.y), 1, (255, 0, 0))
        label2 = myfont.render("Velocity:    {} {}".format('%.2f' % self.player.v[0], '%.2f' % self.player.v[1]), 1, (255, 0, 0))
        self.clock.tick(60)
        label3 = myfont.render("FPS: " + str(self.clock.get_fps()),  1, (255, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.camera_group.draw(self.screen)
        self.screen.blit(label1, (50, 50))
        self.screen.blit(label2, (50, 65))
        self.screen.blit(label3, (50, 80))

    # TODO: Add collisions between asteroids, create callback function to avoid collisions with self
    def collision_check(self):
        """
        Checks for collisions based on mask.

        """
        def collide_callback(obj1, obj2):
            if obj1 is not obj2:
                tmp = pygame.sprite.Group()
                tmp.add(obj2)
                if pygame.sprite.spritecollide(obj1, tmp, False, pygame.sprite.collide_rect):
                    return pygame.sprite.spritecollide(obj1, tmp, False, pygame.sprite.collide_mask)
                else:
                    return False
            else:
                return False

        groups = [self.characters, self.projectiles, self.asteroids]
        for g, groupi in enumerate(groups):
            for groupj in groups[g:]:
                pygame.sprite.groupcollide(groupi, groupj, True, True, collide_callback)

    # TODO: Add Pause Capability
    def handle_events(self):
        """
        Currently this just quits the game upon pressing escape.

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()