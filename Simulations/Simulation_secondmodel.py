''' This script contains the simulations done on the bi-modal non-uniform 
external field. We compare p = 0.35 and p = 0.65. '''
import numpy as np
from Function_Simulation import Simulation, create_phi
import matplotlib.pyplot as plt

hs = np.array([6,6,6,5.2,3.7,1.5])  # Values of parameter h
thetas = np.array([4,7,8.2,9,9,9]) # Values of parameter theta

for i in range(0,6):
    h = hs[i]
    theta = thetas[i]
    
    X0 = np.random.uniform(0,2*np.pi,2000)
    phi35 = create_phi(0.35,2000)
    phi65 = (phi35+np.pi)%(2*np.pi)

    PosizioneX35, r35, psi35 = Simulation(0.35, h, theta, X = X0, phi = phi35)
    PosizioneX65, r65, psi65 = Simulation(0.65, h, theta, X = X0, phi = phi65)
    np.savetxt(f'Data Simulations/PosizioneX_p0.35_h{h}_theta{theta}.txt', PosizioneX35)
    np.savetxt(f'Data Simulations/PosizioneX_p0.65_h{h}_theta{theta}.txt', PosizioneX65)
    Iter = len(PosizioneX35)

    plt.figure()
    plt.plot(r35,'.',color='tab:cyan',markersize=1)
    plt.plot(r65,'.',color='tab:green',markersize=1)
    plt.plot(-1,-1,'.',color='tab:cyan',label=r'$p=0.35$')
    plt.plot(-1,-1,'.',color='tab:green',label=r'$p=0.65$')
    plt.ylabel(r'$r$')
    plt.xlabel('Iteration')
    plt.xlim([0,Iter])
    plt.ylim([0,1])
    plt.legend(loc='upper right')
    plt.savefig(f"Time Evolution/TimeEvolutionR_p0.35_h{h}_theta{theta}.pdf",dpi=300,bbox_inches='tight')
    plt.show()
    
    plt.figure()
    plt.plot(psi35,'.',color='tab:orange',markersize=1)
    plt.plot(psi65,'.',color='tab:red',markersize=1)
    plt.plot(-1,-1,'.',color='tab:orange',label=r'$p=0.35$')
    plt.plot(-1,-1,'.',color='tab:red',label=r'$p=0.65$')
    plt.ylabel(r'$\psi$')
    plt.xlabel('Iteration')
    plt.xlim([0,Iter])
    plt.ylim([0,2*np.pi])
    plt.yticks([0,np.pi/2,np.pi,3*np.pi/2, 2*np.pi],['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
    plt.legend(loc='upper right')
    plt.savefig(f"Time Evolution/TimeEvolutionPsi_p0.35_h{h}_theta{theta}.pdf",dpi=300,bbox_inches='tight')
    plt.show()