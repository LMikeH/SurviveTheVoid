import pygame
from survivethevoid.characters.player import Player
from survivethevoid.environment.asteroids import Asteroid
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
		self.camera = [0, 0]

        # Setup PyGame
        pygame.init()
        self.worlddimensions =
        self.world =

        # Setup Screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.world_background = pygame.Surface(worlddimensions)
        self.world_background = background.convert()
		self.world_background.fill((0, 0, 0))

        # Debug surface
		debug = pygame.Surface(worlddimensions)
		debug = debug.convert()
		debug.fill((255, 255, 255))
		background.blit(debug, (0, 0))
		screen.blit(background, (0, 0))
		pygame.display.flip()

    def start(self):
        """
        Create
        """
        # Setup Objects
        self.characters = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.hero = Player(screen, 200, 200, 0)
        self.one_asteroid = Asteroid(screen, 0, 0, [.1,.1,.1], 50)
        self.asteroids.add(self.one_asteroid)
        self.characters.add(self.hero)

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

    def update(self, keys):
        """
        This function updates everything based on events that occur.

        Parameters
        ----------
        keys

        Returns
        -------

        """
        self.hero.update(keys)
        self.asteroids.update()
        self.collision_check()

    def draw(self):
        """
        This function draws all of the groups.

        Returns
        -------

        """
        self.characters.draw(self.screen)
        self.asteroids.draw(self.screen)

    def collision_check(self):
        col = pygame.sprite.spritecollide(self.hero, self.asteroids, False, pygame.sprite.collide_mask)

        if col != []:
            self.hero.kill()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
