import numpy
import numpy as np
def circumference (radius):
    a = 2*np.pi*radius
    return a
def surface(radius):
    b = np.pi*radius^2
    return b
radius = 2
print("The surface is", circumference(radius))
print("The circumference is",surface(radius))