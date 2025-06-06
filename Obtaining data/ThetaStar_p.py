''' This script determines for each h the value of theta such that 
there exists a r with F3(r) = r and F3'(r) = 1 on [0, 1],
and with F4(r) = r and F4'(r) = 1 on [0, 1]. '''
import numpy as np
from Functions_F0_Fpi_p import F0, F0der, Fpi, Fpider

dt, dtheta, dh = 0.01, 0.01, 0.01
Niter, N0iter, Nhiter = 100, 1000, 1000
p = 0.35

#%% Determining thetastar0.
thetastar0 = []

# Given a r, compute if there exists a pair (h,theta) satisfying our condition.
def compute_zeros(x, p):
    results = []
    h_values = np.arange(Nhiter) * dh
    theta_values = np.arange(N0iter) * dtheta
    
    for h in h_values:
        val0 = F0(x, theta_values, h, p) - x
        val1 = F0der(x, theta_values, h, p) - 1
        mask = (np.abs(val0) <= 0.001) & (np.abs(val1) <= 0.002)
        results.extend([(h, theta) for theta in theta_values[mask]])
    return results

for i in range(Niter):
    x = dt * i
    thetastar0.extend(compute_zeros(x, p))
    print(i)

thetastar0 = np.array(thetastar0)
np.savetxt(f'Data (txt files)/Thetastar0_p{p}.txt', thetastar0)

#%% Determining thetastarpi.
thetastarpi = []

def compute_zeros(x, p):
    results = []
    h_values = np.arange(Nhiter) * dh
    theta_values = np.arange(N0iter) * dtheta
    
    for h in h_values:
        val0 = Fpi(x, theta_values, h, p) - x
        val1 = Fpider(x, theta_values, h, p) - 1
        mask = (np.abs(val0) <= 0.001) & (np.abs(val1) <= 0.002)
        results.extend([(h, theta) for theta in theta_values[mask]])
    return results

for i in range(Niter):
    x = dt * i
    thetastarpi.extend(compute_zeros(x, p))
    print(i)

thetastarpi = np.array(thetastarpi)
np.savetxt(f'Data (txt files)/Thetastarpi_p{p}.txt', thetastarpi)



