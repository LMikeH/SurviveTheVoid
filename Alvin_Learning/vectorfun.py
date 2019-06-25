import numpy as np
import matplotlib.pyplot as plt


# initial conditions
v = [0, 0]      # Velocity Vector
s = [0, 0]       # Displacement Vector
theta = 0        # Angle
omega = 0       # dtheta/dt or angular velocity


# Constant Accelerations
a = [1.0, 1.0]  # Acceleration Vector
alpha = 1.0       # domega/dt angular acceleration

# Random control input from buttons (0 is off, 1 is on)
command_a = np.random.randint(-1, 2, (100, 2))
command_theta = np.random.randint(-1, 2, 100)

# Loop through updating time steps
for i, com in enumerate(command_a):
    # Update Angle
    omega += alpha*command_theta[i]
    theta += omega

    # Rotation Matrix :>(
    rad_angle = (theta)*np.pi/180  # Convert degrees to radians
    rot_mat = np.array([[np.cos(rad_angle), -np.sin(rad_angle)],
                        [np.sin(rad_angle), np.cos(rad_angle)]])

    # Update Velocity
    v += np.dot(rot_mat, a*command_a[i])

    # update Position
    s += v

    # Plot position
    plt.scatter(s[0], s[1], facecolor='blue')
    # plt.scatter(v[0], v[1], facecolor='red')

plt.show()