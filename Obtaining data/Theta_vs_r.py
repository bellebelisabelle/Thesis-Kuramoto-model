''' This scripts determines r after a certain amount of iterations for fixed h
and different theta. For the bi-modal non-uniform field, we compare p = 0.35 
and p = 0.65 and use the same initial conditions. '''
from Function_Simulation import Simulation, create_phi
import matplotlib.pyplot as plt
import numpy as np
import scipy

Iter = 2000

#%% Bi-modal uniform external field
p = 0.5
h = 1
R = np.array([])
thetas = np.arange(0.05, 5.05, 0.05)

for theta in thetas:
    _, r, _ = Simulation(p, h, theta, phist = False)
    R = np.append(R, r[Iter-1])
    print(theta)

np.savetxt(f'Data (txt files)/Theta_vs_r_p{p}_h{h}.txt', R)

#%% Bi-modal non-uniform external field
thetas = np.arange(0.05, 10.05, 0.05)

R35 = np.array([])
PSI35 = np.array([])    
R65 = np.array([])
PSI65 = np.array([])

for h in [1, 3]:
    if h == 1:
        thetas = np.arange(0.05, 5.05, 0.05)
    if h == 3:
        thetas = np.arange(0.1, 10.1, 0.1)
    for theta in thetas:
        X = np.random.uniform(0, 2*np.pi, 2000)
        phi35 = create_phi(0.35, len(X))
        phi65 = np.pi-phi35
        
        _, R3, PSI3  = Simulation(0.35, h, theta, X = X, phi = phi35, phist=False)
        R35 = np.append(R35, R3[Iter-1])
        PSI35 = np.append(PSI35, PSI3[Iter-1])
        
        _, R6, PSI6  = Simulation(0.65, h, theta, X = X, phi = phi65, phist=False)
        R65 = np.append(R65, R6[Iter-1])
        PSI65 = np.append(PSI65, PSI6[Iter-1])
        print(theta)
        
    np.savetxt(f'Data (txt files)/Theta_vs_r_p0.35_h{h}.txt', R35)
    np.savetxt(f'Data (txt files)/Theta_vs_psi_p0.65_h{h}.txt', PSI35)
    np.savetxt(f'Data (txt files)/Theta_vs_r_p0.35_h{h}.txt', R65)
    np.savetxt(f'Data (txt files)/Theta_vs_psi_p0.65_h{h}.txt', PSI65)
    
#%% Four-modal uniform external field
p = 4
thetas = np.arange(0.1, 10.1, 0.1)

for h in [2.5, 4]:
    R = np.array([])
    for theta in thetas:
        _, r, _ = Simulation(p, h, theta, phist = False)
        R = np.append(R, r[Iter-1])
    
    np.savetxt(f'Data (txt files)/Theta_vs_r_p{p}_h{h}.txt', R)