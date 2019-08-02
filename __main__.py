import pygame
from survivethevoid.characters.player import Player
from survivethevoid.environment.asteroids import Asteroid
from survivethevoid.core.game import Game

def main():
    game = Game()
    game.start_level()
    game.run()


if __name__ == "__main__":
    main()
