''' This script contains the simulations done on the four-modal uniform 
external field. '''
import numpy as np
from Function_Simulation import Simulation
import matplotlib.pyplot as plt

p = 4
thetas = np.array([2,4.2,9,9,9,9])
hs = np.array([4,2.5,6,5,4.3,2])

for i in range(0,len(thetas)):
    theta = thetas[i]
    h = hs[i]
    PosizioneX, r, psi = Simulation(p, h, theta)
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
    fig.savefig(f"Time Evolution/TimeEvolution_p{p}_h{h}_theta{theta}.pdf",dpi=300,bbox_inches='tight')
    plt.show()
