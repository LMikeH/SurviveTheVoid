
"""
HW 2 for Alvin

You are to plot trajectories of a bullet with numpy and matplotlib

"""

import numpy as np
import matplotlib.pyplot as plt

# This is how you make a plot:
xdata = np.linspace(0, 100, 100)  # just makes linear test x data from 0 to 100
ydata = xdata
plt.figure()
plt.plot(xdata, ydata)
plt.title("This is an example plot")


# This is how you do arithmetic with vectors in numpy:
a = np.array([1, 2])
b = np.array([2, 3])
print(a)
a += b  # adding
print(a)
a -= b  # subtract
print(a)
c = np.dot(a, b)  # multiply 1 x 2 * 2 x 1 giving 1 x 1 (scalar) Also know as dot product
print(c)


# this is how you break a magintude into it's x and y components
mag = 1000
angle = 30
rads = 30*np.pi/180
xcom = 1000*np.cos(rads)
ycom = 1000*np.sin(rads)

# Then put the components in a vector
vect = np.array([xcom, ycom])


##################################################
####### The Problem #############################
################################################
"""
You just shot a bullet out of a cannon at 30 degrees above the horizon with a 
muzzle velocity of 1000 m/s. Calculate the trajectory as a function of time.
"""

## Challenge Series 1

# Part 1
# initial position
s = [0, 0]  # hint: this is a list, make it an array...
array = np.array(s)

# Part 2
# ------
# muzzle velocity magnitude
v = 1000  # m/s  # hint: break this into it's x and y components
# Angle of shot
angle = 30
rads = angle*np.pi/180
xcom = 1000*np.cos(rads)
ycom = 1000*np.sin(rads)

velocity = np.array([xcom, ycom])



# Part 3
# ------
# Make a vector for gravity...
# g=?
g = np.array([0, -9.8])

# Part 4  WARNING! Very hard problem alert!
# ------
# The timestep is .01 second
t = np.arange(0, 100, 1)  # This is t in .01 s increments.
# Calculate a matrix that gives velocity in each time step.
# has the following structure:
# v_of_t = [[vx1, vy1],
#           [vx2, vy2],
#           [vx3, vy3],
#              ...
#           [vxn, vyn]]

for i, dt in enumerate(t):
    deltaV = g*dt
    if i > 0:
        velocity = np.vstack([velocity, velocity[-1] + deltaV])
    else:
        velocity = np.vstack([velocity, velocity + deltaV])

print(velocity)
plt.plot(velocity[:, 0], velocity[:, 1])

plt.show()
# Part 5 WARNING! Very hard problem alert!
# ------
# Calculate s for every timestep t in a matrix with similar
# structure as the v_of_t matrix


# Part 6 WARNING! Very hard problem alert!
# ----
# Plot x vs y for every timestep, hint: plt.plot(s[0], s[1])


## End of Challenge Series 1

## Challenge Series 2 ## To be continued...

