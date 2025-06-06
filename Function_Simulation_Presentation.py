''' In this whole document, p = 4 represents the field in 4 directions,
other p represent the probability of the two direction case. '''

import numpy as np
import matplotlib.pyplot as plt
import random

''' Below is the function to calculate the order parameters r and psi. 
The output r is a measure for the degree of alignment. 
The output psi is a measure for the average direction the spins are pointing. '''

def angle(x,y):
    if x <= 0:
        psi = np.arctan(y/x)+np.pi 
    else:
        psi = np.arctan(y/x)
        psi = psi % (2*np.pi)
    return psi  

def r_psi(xi):
    repsi = 1/len(xi)*np.e**(1j*xi)
    repsi = np.sum(repsi)
    r = abs(repsi)
    normalization = repsi / r
    psi = angle(np.real(normalization),np.imag(normalization))
    return r, psi  

'''' Below, the function Q is given, which is a solution to the McKean equation. '''

def Q(x, phi, theta, h, r, psi):
    z = theta**2 * r**2 + h**2 + 2 * h * r * theta * np.cos(phi - psi)
    denom = 2 * np.pi * np.i0(2 * np.sqrt(z))
    numer = np.exp(2 * theta * r * np.cos(psi - x) + 2 * h * np.cos(phi - x))
    return numer / denom

''' This part creates phi, which is the external field. '''

def create_phi(p,M):
    if p == 4:
        eta = random.choices([0,1,2,3],weights = [1,1,1,1],k=M)
    else:
        eta = random.choices([0,2],weights = [p,1-p],k=M)
    return np.pi/2*np.array(eta)


#%% 
''' Here I create the simulation, with the following variables:
    
p represents the external field, if it is 4, it is cardinal directions,
otherwise it is the chance of pointing to 0 for the two opposite directions;

h is the strength of the external field;
theta is the strength of the interaction;

Iter is the numbero of iterations we do;
dt is the length of the timesteps;

X is the initial condition, the default is uniform on (0,2*pi) with a lenght of 2000
phi is the external field, the default is based on p with a length of 2000

phist can be true or false, if it is true it shows and saves the histograms, otherwise it doesn't. '''

def Simulation(p, h, theta, Iter = 2000, dt = 0.01, X = [], phi = [], phist = True):
    if len(X) == 0:
        X = np.random.uniform(0, 2*np.pi, 2000)
    if len(phi) == 0:
        phi = create_phi(p, 2000)
    
    N = len(X)
    Y = np.zeros(N)
    noise = np.random.normal(0, np.sqrt(dt), (Iter, N))
  
    phi_0 = [i for i, x in enumerate(phi) if x == 0]
    phi_pi2 = [i for i, x in enumerate(phi) if x == np.pi/2]
    phi_pi = [i for i, x in enumerate(phi) if x == np.pi]
    phi_3pi2 = [i for i, x in enumerate(phi) if x == 3*np.pi/2]
    
    if phist == True:
        plt.figure()
        plt.xlim([0,2*np.pi])
        plt.xlabel('Angle')
        plt.ylabel('Frequency of the spins')
        plt.xticks([0,np.pi/2,np.pi,3*np.pi/2, 2*np.pi],['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
        plt.hist(X[phi_0],bins=np.linspace(0,2*np.pi,150),color='red',alpha=0.5,label=r'$\varphi=0$',density=True)
        plt.hist(X[phi_pi],bins=np.linspace(0,2*np.pi,150),color='blue',alpha=0.5,label=r'$\varphi=\pi$',density=True)
        if p == 4:
            plt.hist(X[phi_pi2],bins=np.linspace(0,2*np.pi,150),color='gold',alpha=0.5,label=r'$\varphi=\frac{\pi}{2}$',density=True)
            plt.hist(X[phi_3pi2],bins=np.linspace(0,2*np.pi,150),color='green',alpha=0.5,label=r'$\varphi=\frac{3\pi}{2}$',density=True)
        plt.legend(loc=1)
        # plt.savefig(f"Histograms/X0_p{p}_h{h}_theta{theta}.pdf",dpi=300,bbox_inches='tight')
        plt.show()

    def f(ARR):
        ssin = np.sum(np.sin(ARR[:, None] - ARR[None, :]), axis=0)
        return ssin * theta / N + h * np.sin(phi-ARR)
    
    PosizioneX = np.zeros((Iter, N))
    r = np.zeros(Iter)
    psi = np.zeros(Iter)
    for i in range(0,Iter):
        Y = X + f(X) * dt + noise[i,:]
        Y = Y % (2*np.pi)
        PosizioneX[i,:] = Y
        r[i] = r_psi(Y)[0]
        psi[i] = r_psi(Y)[1]
        X = Y
        
    r_final = r[Iter-1]
    psi_final = psi[Iter-1]
    
    if phist == True:    
        x = np.arange(0,2*np.pi,0.01)
        plt.figure()
        plt.xlim([0,2*np.pi])
        plt.xlabel('Angle')
        plt.ylabel('Frequency of the spins')
        plt.hist(Y[phi_0],bins=np.linspace(0,2*np.pi,150),color='red',alpha=0.5,label=r'$\varphi=0$',density=True)
        plt.hist(Y[phi_pi],bins=np.linspace(0,2*np.pi,150),color='blue',alpha=0.5,label=r'$\varphi=\pi$',density=True)
        plt.plot(x,Q(x, 0, theta, h, r_final, psi_final),'red')
        plt.plot(x,Q(x, np.pi, theta, h, r_final, psi_final),'blue')
        plt.title(fr'$h={h}$, $\theta={theta}$, $N={N}$, Iter={Iter}')
        if p == 4:
            plt.hist(Y[phi_pi2],bins=np.linspace(0,2*np.pi,150),color='gold',alpha=0.5,label=r'$\varphi=\frac{\pi}{2}$',density=True)
            plt.hist(Y[phi_3pi2],bins=np.linspace(0,2*np.pi,150),color='green',alpha=0.5,label=r'$\varphi=\frac{3\pi}{2}$',density=True)
            plt.plot(x,Q(x, np.pi/2, theta, h, r_final, psi_final),'gold')
            plt.plot(x,Q(x, 3*np.pi/2, theta, h, r_final, psi_final),'green')
        plt.xticks([0,np.pi/2,np.pi,3*np.pi/2, 2*np.pi],['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
        plt.legend(loc=1)
        plt.savefig(f"Figures Presentation/Pres_p{p}_h{h}_theta{theta}.pdf",dpi=300,bbox_inches='tight')
        plt.show()
    return PosizioneX, r, psi
