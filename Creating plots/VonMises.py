''' This script plots the behavior of the Von Mises distribution for different
values of the parameters. '''
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.01)
def VM(x,phi,k):
    VM = np.exp(-k*np.cos(x-phi+np.pi))/(2*np.pi*np.i0(k))
    return VM % (2*np.pi)

ks = np.array([0.5, 1, 2, 4])
phis = np.array([np.pi/2, np.pi, 3*np.pi/2])
labels = np.array([r'\frac{\pi}{2}', r'\pi', r'\frac{3\pi}{2}'])

# Fix k, plot different phi
k = 2
plt.figure()
for i in range(0, len(phis)):
    plt.plot(x, VM(x, phis[i], k), label = rf'$(\kappa,\phi)=({k},{labels[i]})$')
plt.legend()
plt.xlim([0, 2*np.pi])
plt.ylim([0, 0.8])
plt.xlabel(r'$x$')
plt.ylabel(r'$\rho(x)$')
plt.savefig('Figures/VM_fixedk.pdf', dpi=300, bbox_inches='tight')
plt.plot()

# Fix phi, plot different k
phi = np.pi
plt.figure()
for k in ks:
    plt.plot(x, VM(x, phi, k), label = rf'$(\kappa,\phi)=({k},\pi$)')
plt.legend()
plt.xlim([0, 2*np.pi])
plt.ylim([0, 0.8])
plt.xlabel(r'$x$')
plt.ylabel(r'$\rho(x)$')
plt.savefig('Figures/VM_fixedphi.pdf', dpi=300, bbox_inches='tight')
plt.plot()