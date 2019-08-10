import pygame


class _BaseCharacter(pygame.sprite.Sprite):
    def __init__(self, name, screen, location, **kwargs):
        self.name = name
        self.x = location[0]
        self.y = location[1]
        self.angle = location[2]
        self.screen = screen
        self.__dict__.update(kwargs)

    # ToDo: Setup kwargs so they don't suck...
    def set_config_data(self, data_loader):
        self.image = data_loader.get_ship_image(self.ship['name'])

        self.projectile_images = {}

        # Pass in bullet/missile images
        for key in self.ship.keys():
            if 'weapon' or 'missile' in key:
                self.projectile_images[key] = data_loader.get_projectile_image(self.ship[key])

        # set power
        self.power, self.energy = data_loader.get_reactor_specs(self.ship['powerplant'])


if __name__ == '__main__':
    import yaml
    file = open('../../assets/characters/player.yaml')
    config = yaml.safe_load(file)
    file.close()

    player = _BaseCharacter('player', None, [1, 2, 3], **config)
    print(player.ship['weapon A'])