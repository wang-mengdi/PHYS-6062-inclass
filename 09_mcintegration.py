import numpy as np

def MC_Pi(N):
    x = np.random.rand(N)
    y = np.random.rand(N)
    r = np.sqrt(x**2 + y**2)
    count = np.sum(r < 1)
    return 4.0*count/N

for idx in range(1, 9):
    N = 10**idx
    print("N = %d, MC_Pi = %f" % (N, MC_Pi(N)))