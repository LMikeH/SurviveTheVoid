import numpy as np
import pygame


def R(angle):
    rad_angle = (angle)*np.pi/180
    return np.array([[np.cos(rad_angle), -np.sin(rad_angle)],
                     [np.sin(rad_angle), np.cos(rad_angle)]])

# def check_bounding_box(a, b):
#     if a.rect.right > b.rect.left and \



if __name__ == "__main__":
    a = np.array([0, 1])
    print(np.dot(R(180), a))
