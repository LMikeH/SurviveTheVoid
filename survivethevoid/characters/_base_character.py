import pygame


class _BaseCharacter(pygame.sprite.Sprite):
    def __init__(self, name, screen, location, **kwargs):
        self.name = name
        self.x = location[0]
        self.y = location[1]
        self.angle = location[2]
        self.screen = screen
        self.__dict__.update(kwargs)


if __name__ == '__main__':
    import yaml
    file = open('../../assets/characters/player.yaml')
    config = yaml.safe_load(file)
    file.close()

    player = _BaseCharacter('player', None, [1, 2, 3], **config)
    print(player.ship['weapon A'])