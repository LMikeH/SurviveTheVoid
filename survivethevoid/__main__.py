import pygame
from survivethevoid.characters.player import Player
from survivethevoid.environment.asteroids import Asteroid
# from survivethevoid.environment.Camera import Camera


class Game(object):
    def __init__(self, screen):
        """
        This is the overall game class which controls events, players, and non-players.

        Parameters
        ----------
        screen: pygame display object
        passes in the display so sprites can be drawn.

        """
        self.screen = screen
        self.characters = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.hero = Player(screen, 200, 200, 30)
        self.one_asteroid = Asteroid(screen, 0, 0, [.1,.1,.1], 50)
        self.asteroids.add(self.one_asteroid)
        self.characters.add(self.hero)
        # self.camera = Camera(self.screen.width, self.screen.height)

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

def main():
    """
    This is the main loop.

    """


    """
    Alvin's First Task:
    -------------------
    
    a.) Make game full screen.
        -commit and push code to github.
        -put in pull request.
    
    b.) Make camera follow rocket.
        - make new branch
        - implement
        - commit
        - pull request
    
    """

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    done = False
    game = Game(screen)
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    pygame.display.update()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(background, (0, 0))

        game.update(pygame.key.get_pressed())
        game.draw()

        pygame.display.flip()


if __name__ == "__main__":
    main()

