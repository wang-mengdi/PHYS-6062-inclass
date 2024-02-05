import numpy as np
from numpy.random import random

# Constants
Z = 79
e = 1.602e-19
E = 7.7e6*e
epsilon0 = 8.854e-12
a0 = 5.292e-11
sigma = a0/100
N = 100000

# Complete in-class
# Function to generate two Gaussian random numbers
# Optional: Use array arithmetic to speed-up
def gaussian(N):
    z = random(N)
    r = np.sqrt(-2*sigma**2*np.log(1-z))
    return r

r_arr = gaussian(N)
theta_arr = 2 * np.arctan(Z*e**2/(2*np.pi*epsilon0*E*r_arr))
count = np.sum(theta_arr > np.pi/2)

print("%d particles were reflected out of %d" % (count,N))
