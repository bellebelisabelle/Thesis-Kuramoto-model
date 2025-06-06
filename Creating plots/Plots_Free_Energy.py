''' This script plots the free energy landscape for given p, h and theta. 
Note that p = 4 corresponds with the four-modal uniform external field. '''
import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot the free energy landscape
def Plots_Energy(p, h, theta):
    psi = np.linspace(0, 2*np.pi, 101)
    r = np.linspace(0, 1, 101)
    R, PSI = np.meshgrid(r, psi)
    
    Fplot = np.genfromtxt(f'Data (txt files)/Free Energy (txt files)/FreeEnergy_p{p}_h{h}_theta{theta}.txt')    
    fig = plt.figure(figsize=(12, 5))
    
    labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
    
    # Contour plot, including colorbar
    ax1 = fig.add_subplot(121)
    contour = ax1.contourf(Fplot, cmap = 'plasma')
    cbar = fig.colorbar(contour, ax = ax1)
    
    # Determine place with minimal energy and plot it when r > 0.
    [row, col] = np.where(Fplot < np.min(Fplot) + 10**(-12))
    if col[0]>0:
        ax1.plot(col, row, '*', color = 'limegreen', markersize = 10)
    
    ax1.set_xlabel(r'$r$')
    ax1.set_ylabel(r'$\psi$')
    ax1.set_xticks([0, 25, 50, 75, 100], [0, 0.25, 0.5, 0.75, 1])
    ax1.set_yticks([0, 25, 50, 75, 100], labels)
    
    # Surface plot
    ax2 = fig.add_subplot(122, projection = '3d')
    surf = ax2.plot_surface(R, PSI, Fplot, cmap = 'plasma', alpha = 0.9)
    
    ax2.set_xlabel(r'$r$')
    ax2.set_ylabel(r'$\psi$')
    ax2.set_zlabel(r'$\mathcal{F}\ (r,\psi)$', labelpad = -11)
    places = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    ax2.set_yticks(places, labels)
    ax2.set_zticklabels([])
    ax2.tick_params(axis='z', colors='k') 
    ax2.set_zlabel(r'$\mathcal{F}\ (r,\psi)$')
    
    plt.subplots_adjust(wspace=-0.1, hspace=0)
    plt.savefig(f'Free Energy/FreeEnergy_p{p}_h{h}_theta{theta}.pdf', dpi=300, bbox_inches='tight')

    plt.show()

#%% Bi-modal uniform external field
p = 0.5
h = 1
thetas = [1.0, 1.7, 2.5, 4.0]
for theta in thetas:
    Plots_Energy(p, h, theta)

#%% Bi-modal non-uniform external field
ps = [0.35, 0.65]
hs = [6.0, 6.0, 6.0, 5.2, 3.7, 1.5]
thetas = [4.0, 7.0, 8.2, 9.0, 9.0, 9.0]
for p in ps:
    for i in range(0,len(hs)):
        Plots_Energy(p, hs[i], thetas[i])

#%% Four-modal uniform external field
p = 4
hs = [4.0, 2.5, 6.0, 5.0, 4.3, 2.0]
thetas = [2.0, 4.2, 9.0, 9.0, 9.0, 9.0]
for i in range(0,len(hs)):
    Plots_Energy(p, hs[i], thetas[i])
