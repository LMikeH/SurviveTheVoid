import pygame
from characters.player import Player


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
        self.characters.add(self.hero)

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

    def draw(self):
        """
        This function draws all of the groups.

        Returns
        -------

        """
        self.characters.draw(self.screen)

def main():
    """
    This is the main loop.

    """
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    done = False
    game = Game(screen)
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

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

