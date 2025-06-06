''' This script plots the convergence to r for fixed h and varying theta. 
The results are obtained from the script Theta_vs_r.py. '''
from Functions_Theta import theta1, thetap1, thetap2, theta4
import matplotlib.pyplot as plt
import numpy as np

#%% Bi-modal uniform external field.
p = 0.5
h = 1

thetas = np.arange(0.05, 5.05, 0.05)
R = np.genfromtxt(f'Data (txt files)/Theta_vs_r_p{p}_h{h}.txt')

plt.figure()
plt.plot(thetas, R, '.')
plt.xticks([0, 1, theta1(h), 2, 3, 4, 5], [0, 1, r'$\theta_1$(1)', 2, 3, 4, 5])
plt.ylabel(r'$r$')
plt.xlabel(r'$\theta$')
plt.xlim([0, 5])
plt.ylim([0, 1])
plt.savefig(f"Figures/Theta_vs_r_p{p}_h{h}.pdf", dpi=300, bbox_inches='tight')

#%% Bi-modal non-uniform external field for p = 0.35 and p = 0.65.
p = 0.35

for h in [1, 3]:
    theta1h = thetap1(h)
    theta2h = thetap2(h, 0.35)
    
    if h == 1:
        thetas = np.arange(0.05, 5.05, 0.05)
        positions = [0, 1, theta1h, 2, 3, theta2h, 4, 5]
        labels = [0, 1, r'$\theta_{p1}$(1)', 2, 3, r'$\theta_{p2}$(1)', 4, 5]
    if h == 3:  
        thetas = np.arange(0.1, 10.1, 0.1)
        positions = [0, 2, 4, 6, 8, theta1h, theta2h]
        labels = [0, 2, 4, 6, 8, r'$\theta_{p1}$(3)', r'$\theta_{p2}$(3)']

    R1 = np.genfromtxt(f'Data (txt files)/Theta_vs_r_p0.35_h{h}.txt')
    R2 = np.genfromtxt(f'Data (txt files)/Theta_vs_r_p0.65_h{h}.txt')
    
    PSI1 = np.genfromtxt(f'Data (txt files)/Theta_vs_psi_p0.35_h{h}.txt')
    PSI2 = np.genfromtxt(f'Data (txt files)/Theta_vs_psi_p0.65_h{h}.txt')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14,5))
    ax1.plot(thetas, R1, '.', color='tab:cyan', label = r'$p=0.35$')
    ax1.plot(thetas, R2, '.', color='tab:green', label = r'$p=0.65$')
    ax1.set_ylabel(r'$r$')
    ax1.set_xlabel(r'$\theta$')
    ax1.set_xlim([0, 5])
    ax1.set_xticks(positions, labels)
    ax1.set_ylim([0, 1])
    ax1.legend(loc='upper left')
    
    ax2.plot(thetas, PSI1, '.', color='tab:orange', label = r'$p=0.35$')
    ax2.plot(thetas, PSI2, '.', color='tab:red', label = r'$p=0.65$')
    ax2.set_ylabel(r'$\psi$')
    ax2.set_xlabel(r'$\theta$')
    ax2.set_xlim([0, 5])
    ax2.set_ylim([0, 2*np.pi])
    ax2.set_xticks(positions, labels)
    ax2.set_yticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    ax2.legend(loc='upper right')
    plt.savefig(f"Figures/Theta_vs_rpsi_p{p}_h{h}.pdf", dpi=300, bbox_inches='tight')
    plt.show()    

#%% Four-modal uniform external field.
p = 4
for h in [2.5,4]:
    thetas = np.arange(0.1, 10.1, 0.1)
    R = np.genfromtxt(f'Data (txt files)/Theta_vs_r_p{p}_h{h}.txt')
    
    plt.figure()
    plt.plot(thetas, R, '.')
    if h == 2.5:
        plt.xticks([0, 2, 4, 6, 8, 10, theta4(h)], [0, 2, 4, 6, 8, 10, rf'$\theta_4({h})$'])
    if h == 4:
        plt.xticks([0, 2, 4, 6, 10, theta4(h)], [0, 2, 4, 6, 10, rf'$\theta_4({h})$'])
    plt.ylabel(r'$r$')
    plt.xlabel(r'$\theta$')
    plt.xlim([0, 10])
    plt.ylim([0, 1])
    plt.savefig(f"Figures/Theta_vs_r_p{p}_h{h}.pdf", dpi=300, bbox_inches='tight')