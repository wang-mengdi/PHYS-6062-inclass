import numpy as np
import matplotlib.pyplot as plt

def f(r,t):
    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + np.sin(t)**2
    return np.array([fx,fy],float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
rpoints = np.zeros((N,2))
rpoints[0] = [1.0, 1.0]

for i in range(N-1):
    r,t = rpoints[i],tpoints[i]
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5*k1, t + 0.5*h)
    k3 = h * f(r + 0.5*k2, t + 0.5*h)
    k4 = h * f(r + k3, t + h)
    rpoints[i+1] = r + (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints, rpoints[:,0], label='x')
plt.plot(tpoints, rpoints[:,1], label='y')
plt.xlabel("t")
plt.ylabel("x,y")
plt.show()
