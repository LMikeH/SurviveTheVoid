import numpy as np

def R(angle):
    rad_angle = (angle)*np.pi/180
    return np.array([[np.cos(rad_angle), -np.sin(rad_angle)],
                     [np.sin(rad_angle), np.cos(rad_angle)]])

if __name__ == "__main__":
    a = np.array([0, 1])
    print(np.dot(R(180), a))
