import pygame
import yaml


class World():
    def __init__(self, height, width, screen):
        self.height = height
        self.width = width
        file = open('survivethevoid/assets/levels/example_level.yaml')
        self.inpdict = yaml.safe_load(file)
        self.objects = self.inpdict['objects']
        self.screen_location = 1000, 1000

    def get_objects(self):
        return self.objects

    def set_object_locations(self, **obj_dict):
        for obj in obj_dict.keys():
            self.objects[obj]['location'] = obj_dict[obj]['location']

    def

