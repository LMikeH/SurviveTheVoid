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
        class_type_data = {}
        types = set([x.split('_')[0] for x in list(self.level_config['characters'].keys())])
        loaded_types = set()
        with self.level_config['objects'] as objects:
            for key in objects:
                if objects[key]['type'] == 'character' and object[key].split('_')[0] not in loaded_types:
                    loaded_types.add(object[key].split('_')[0])
                    file = open(key.split('_')[0] + '.yaml')
                    character_data = yaml.safe_load(file)
                    file.close()

                    for key in character_data['ship']:
                        if 'weapon' in key:
                            class_type_data[]




    def load_weapon_data(self, weapon):
        file = open(self.weapons_path)
        weapon_data = yaml.safe_load(file)
        file.close()

        return weapon_data[weapon]

