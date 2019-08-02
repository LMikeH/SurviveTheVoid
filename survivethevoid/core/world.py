import pygame
import yaml
from scipy.spatial.distance import euclidean
from survivethevoid.core.camera import Camera
import numpy as np


class World():
    def __init__(self, height, width, screen, influence_radius):
        self.height = height
        self.width = width
        self.influence_radius = influence_radius
        file = open('survivethevoid/assets/levels/example_level.yaml')
        self.inpdict = yaml.safe_load(file)
        file.close()
        self.objects = self.inpdict['objects']
        self.camera = Camera(self.objects['player']['location'],
                             screen.get_width(),
                             screen.get_height())

    def get_objects(self):
        return self.objects

    def set_object_locations(self, **obj_dict):
        for obj in obj_dict.keys():
            self.objects[obj]['location'] = obj_dict[obj]['location']

    def check_influence(self):
        init_list = []
        a = np.array(self.camera.location[:2])
        for obj in self.objects.keys():
            b = np.array(self.objects[obj]['location'][:2])
            if euclidean(a, b) <= self.influence_radius and self.objects[obj]['object'] is None:
                init_list.append(obj)
        return init_list

    def check_camera(self, groups, camera_group):
        for group in groups:
            for sprite in group:
                if self.camera.check_contains(sprite):
                    camera_group.add(sprite)

    def update(self):
        self.camera.update()
