from math import sin
import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return -x**3 + sin(t)

a = 0.0           # Start of the interval
b = 10.0          # End of the interval
N = 1000          # Number of steps
h = (b-a)/N       # Size of a single step
x = 0.0           # Initial condition

tpoints = np.arange(a,b,h)
xpoints = np.zeros(N)
xpoints[0] = x

for i in range(0,N-1):
    xpoints[i+1] = xpoints[i] + h * f(xpoints[i], tpoints[i])

plt.plot(tpoints,xpoints)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()
