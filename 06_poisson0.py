import numpy as np
import matplotlib.pyplot as plt

# Constants
M = 25         # Grid squares on a side
V = 0.0         # Voltage at top wall
L = 1.0         # Side length of box
target = 3e-4   # Target accuracy
epsilon_0 = 8.85e-12
a = L / float(M) # grid point spacing

# Create arrays to hold potential values
phi = np.zeros([M+1,M+1],float)
phi[0,:] = V
phiprime = np.empty([M+1,M+1],float)

# Create surface charge density array
rho_values = [-1.0, 1.0]  # Surface charge density
charge_width = [0.2, 0.2] # Width of the charges (assuming squares)
charge_boundaries = [[0.2, 0.2], [0.6, 0.6]] # Position of origin of the charges
rho = np.zeros([M+1,M+1], float)
for i in range(len(rho_values)):
    x0,y0 = charge_boundaries[i]
    cw = charge_width[i]
    for ii in range(M+1):
        for jj in range(M+1):
            x,y = ii*a, jj*a
            if x0 <= x and x <= x0+cw and y0 <= y and y <= y0+cw:
                print(ii,jj,rho_values[i])
                rho[ii,jj] = rho_values[i]
            

# Main loop
delta = 1.0
iteration = 0
while delta>target:

    # Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or j==0 or i==M or j==M:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = (phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])/4 + a*a/(4*epsilon_0)*rho[i,j]
            #
            # Complete in-class for phiprime, the updated solution
            # Remember to keep the boundaries at zero and 
            # to include the sink/source term
            #
                                      

    # Calculate maximum fractional difference from old values
    delta = np.abs(phi-phiprime)
    nonzero = phi > 0
    if nonzero.any():
        #delta = np.max(delta[nonzero] / phi[nonzero])
        delta = np.max(delta[nonzero])
    else:
        delta = 1.0
    if iteration % 10 == 0:
        print("Iteration %3d: max. residual = %12.6g" % (iteration, delta))

    # Swap the two arrays around
    phi,phiprime = phiprime,phi
    iteration += 1

# Make a plot
plt.imshow(phi)
#plt.gray()
plt.show()
