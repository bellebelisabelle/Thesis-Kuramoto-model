''' This script determines for each h the value of theta such that 
there exists a r with F3(r) = r and F3'(r) = 1 on [0.1, 1],
and with F4(r) = r and F4'(r) = 1 on [0.1, 1], for h>= 0.81. '''
import numpy as np
from Functions_F3_F4 import F3, F3der, F4, F4der

dt, dtheta, dh = 0.01, 0.01, 0.01
Niter, N0iter, Nhiter = 91, 1000, 1000

#%% Determining thetastar3.
thetastar3 = []

# Given a r, compute if there exists a pair (h,theta) satisfying our condition.
def compute_zeros(x):
    results = []
    h_values = np.arange(Nhiter) * dh
    theta_values = np.arange(N0iter) * dtheta
    
    for h in h_values:
        val0 = F3(x, theta_values, h) - x
        val1 = F3der(x, theta_values, h) - 1
        mask = (np.abs(val0) <= 0.001) & (np.abs(val1) <= 0.002)
        results.extend([(h, theta) for theta in theta_values[mask]])
    return results

for i in range(Niter):
    x = dt * i + 0.1
    thetastar3.extend(compute_zeros(x))
    print(i)

thetastar3 = np.array(thetastar3)
np.savetxt('Data (txt files)/Thetastar3.txt', thetastar3)

#%% Determining thetastar4.
dt, dtheta, dh = 0.01, 0.01, 0.01
Niter, N0iter, Nhiter = 91, 1000, 920

thetastar4 = []

# Given a r, compute if there exists a pair (h,theta) satisfying our condition.
def compute_zeros(x):
    results = []
    h_values = np.arange(Nhiter) * dh + 0.81
    theta_values = np.arange(N0iter) * dtheta
    
    for h in h_values:
        val0 = F4(x, theta_values, h) - x
        val1 = F4der(x, theta_values, h) - 1
        mask = (np.abs(val0) <= 0.001) & (np.abs(val1) <= 0.002)
        results.extend([(h, theta) for theta in theta_values[mask]])
    return results

for i in range(Niter):
    x = dt * i + 0.1
    thetastar4.extend(compute_zeros(x))
    print(i)

thetastar4 = np.array(thetastar4)
np.savetxt('Data (txt files)/Thetastar4.txt', thetastar4)