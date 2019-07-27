import pygame
from survivethevoid.characters.player import Player
from survivethevoid.environment.asteroids import Asteroid
from survivethevoid.core.game import Game

def main():
    """
    This is the main loop.

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
