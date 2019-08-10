import pygame
import yaml


class DataLoader():
    def __init__(self, level_config):
        self.config = level_config
        self.assets_path = 'assets/'
        self.ships_path = self.assets_path + 'ships/'
        self.power_plants_path = self.ships_path + 'powerplants/'
        self.weapons_path = self.ships_path + 'weapons/'

    def generate_object_data(self):
        with self.level_config['objects'] as objects:
            for key in objects:
                if objects[key]['type'] == 'character':
                    file = open(key.split('_')[0] + '.yaml')
                    character_data = yaml.safe_load(file)
                    file.close()

    def load_weapon_data(self, weapon):

