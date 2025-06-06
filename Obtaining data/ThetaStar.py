''' This script determines for each h from 0.51 the value of theta such that 
there exists a r with F2(r) = r and F2'(r) = 1 on [0.1, 1]. '''
import numpy as np
from Functions_F2 import F2, F2der

# Set the stepsize.
dt, dtheta, dh = 0.01, 0.01, 0.01
Niter, N0iter, Nhiter = 91, 1001, 950

thetastar = []

# Given a r, compute if there exists a pair (h,theta) satisfying our condition.
def compute_zeros(x):
    results = []
    h_values = np.arange(Nhiter) * dh + 0.51
    theta_values = np.arange(N0iter) * dtheta
    
    for h in h_values:
        val0 = F2(x, theta_values, h) - x
        val1 = F2der(x, theta_values, h) - 1
        mask = (np.abs(val0) <= 0.001) & (np.abs(val1) <= 0.002)
        results.extend([(h, theta) for theta in theta_values[mask]])
    return results

for i in range(Niter):
    x = dt * i + 0.1
    thetastar.extend(compute_zeros(x))
    print(i)

thetastar = np.array(thetastar)
np.savetxt('Data (txt files)/Thetastar.txt', thetastar)






