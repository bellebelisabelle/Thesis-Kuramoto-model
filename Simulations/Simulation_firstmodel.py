''' This script contains the simulations done on the bi-modal uniform external
field. '''
import numpy as np
from Function_Simulation import Simulation, create_phi
import matplotlib.pyplot as plt

p = 0.5
h = 1
thetas = np.array([1,1.7,2.5,4]) # Values of parameter theta

for theta in thetas:
    PosizioneX, r, psi = Simulation(p, h, theta)
    np.savetxt(f'Data Simulations/PosizioneX_h{h}_theta{theta}_4.txt', PosizioneX)
    Iter = len(PosizioneX)

    fig, ax1 = plt.subplots()
    ax1.plot(r,'.',markersize=1)
    ax2 = ax1.twinx()
    ax2.plot(psi,'.',color='tab:orange',markersize=1)
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel(r'r')
    ax2.set_ylabel(r'$\psi$')
    ax1.plot(-1,-1,'.',color='#1f77b4',label=r'$r$')
    ax1.plot(-1,-1,'.',color='#ff7f0e',label=r'$\psi$')
    ax1.set_xticks([0,500,1000,1500,2000])
    ax2.set_yticks([0,np.pi/2,np.pi,3*np.pi/2, 2*np.pi],['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
    ax1.set_xlim([0,Iter])
    ax1.set_ylim([0,1])
    ax2.set_ylim([0,2*np.pi])
    ax1.legend()
    fig.savefig(f"Time Evolution/TimeEvolution_p{p}_h{h}_theta{theta}.png",dpi=300,bbox_inches='tight')
    plt.show()
    
#%%

p = 0.5 # Value of p
h = 1 # Value of parameter h
thetas = np.array([1.7,2.5,4]) # Values of parameter theta
N = 2000

for theta in thetas:
    X00 = np.random.vonmises(0,4,N)
    X0pi4 = np.random.vonmises(np.pi/4,4,N)
    X0pi2 = np.random.vonmises(np.pi/2,4,N)
    phi = create_phi(p,N)
    
    _, r0, psi0 = Simulation(0.35, h, theta, X = X00, phi = phi, phist = False)
    _, rpi4, psipi4 = Simulation(0.65, h, theta, X = X0pi4, phi = phi, phist = False)
    _, rpi2, psipi2 = Simulation(0.35, h, theta, X = X0pi2, phi = phi, phist = False)
    
    Iter = len(r0)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14,5))
    ax1.plot(r0,'.',color='tab:cyan',markersize=1)
    ax1.plot(rpi4,'.',color='tab:green',markersize=1)
    ax1.plot(rpi2,'.',color='tab:purple',markersize=1)
    ax1.plot(-1,-1,'.',color='tab:cyan',label=r'$\phi=0$')
    ax1.plot(-1,-1,'.',color='tab:green',label=r'$\phi=\frac{\pi}{2}$')
    ax1.plot(-1,-1,'.',color='tab:purple',label=r'$\phi=\frac{\pi}{2}$')
    ax1.set_ylabel(r'$r$')
    ax1.set_xlabel('Iteration')
    ax1.set_xticks([0,500,1000,1500,2000])
    ax1.set_xlim([0,Iter])
    ax1.set_ylim([0,1])
    ax1.legend()

    ax2.plot(psi0,'.',color='tab:orange',markersize=1)
    ax2.plot(psipi4,'.',color='tab:red',markersize=1)
    ax2.plot(psipi2,'.',color='tab:pink',markersize=1)
    ax2.plot(-1,-1,'.',color='tab:orange',label=r'$\phi=0$')
    ax2.plot(-1,-1,'.',color='tab:red',label=r'$\phi=\frac{\pi}{2}$')
    ax2.plot(-1,-1,'.',color='tab:pink',label=r'$\phi=\frac{\pi}{2}$')
    ax2.set_ylabel(r'$\psi$')
    ax2.set_xlabel('Iteration')
    ax2.set_xlim([0,Iter])
    ax2.set_ylim([0,2*np.pi])
    ax2.set_xticks([0,500,1000,1500,2000])
    ax2.set_yticks([0,np.pi/2,np.pi,3*np.pi/2, 2*np.pi],['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
    ax2.legend()
    plt.savefig(f"Figures/Convergence_p{p}_h{h}_theta{theta}.png",dpi=300,bbox_inches='tight')
    plt.show()




