import yaml
from survivethevoid.core.camera import Camera
import numpy as np


# TODO: Setup game saving capability
class World():
    def __init__(self, height, width, screen, influence_radius):
        """
        This class loads the level and handles what gets loaded as an object
        in the game. It also handles the camera.

        Parameters
        ----------
        height: int
        pixel height of the level

        width: int
        pixel width of the level

        screen: pygame display object

        influence_radius: float/int
        radius objects are spawned/allowed in memory.

        """
        self.height = height
        self.width = width
        self.influence_radius = influence_radius
        file = open('assets/levels/example_level.yaml')
        self.inpdict = yaml.safe_load(file)
        file.close()
        self.objects = self.inpdict['objects']
        self.camera = Camera(self.objects['player']['location'],
                             screen.get_width(),
                             screen.get_height())

    def check_influence(self):
        """
        Checks if character/environment object is within player's sphere
        of influence.

        Returns
        -------
        List of names for objects to be initialized.

        """
        init_list = []
        a = np.array(self.camera.location[:2])
        for obj in self.objects.keys():
            b = np.array(self.objects[obj]['location'][:2])
            if np.linalg.norm(a - b) <= self.influence_radius and self.objects[obj]['object'] is None:
                init_list.append(obj)
        return init_list

    def check_camera(self, groups, camera_group):
        """
        Checks to see if objects are on screen. Then passes relative screen
        coordinates for drawing.

        Parameters
        ----------
        groups: sprite groups
        All sprite groups besides camera group

        camera_group: sprite group
        contains objects to be drawn.

        """
        for group in groups:
            for sprite in group:
                if self.camera.check_contains(sprite) is True:
                    camera_group.add(sprite)

    def update(self):
        self.camera.update()
