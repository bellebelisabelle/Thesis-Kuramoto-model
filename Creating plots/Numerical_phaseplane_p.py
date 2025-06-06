''' This script creates the numerical phase plane of the bi-modal non-uniform
external field. '''
import numpy as np
import matplotlib.pyplot as plt

ps = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45])

for p in ps:
    # Load all pairs with solutions for the system.
    psi_0 = np.loadtxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psi0.txt')
    psi_pi1 = np.loadtxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psipi_1.txt')
    psi_pi3 = np.loadtxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psipi_3.txt')
    psi_excluded = np.loadtxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psiexcluded.txt')
    psi_excluded = np.unique(psi_excluded[:, 3:], axis=0)
    
    # Create the plot.
    alpha = 0.1
    plt.figure()
    plt.plot(psi_excluded[:,1], psi_excluded[:,0], 'r.', alpha=alpha)
    plt.plot(psi_pi1[:,3], psi_pi1[:,2], 'y.', alpha=alpha)
    plt.plot(psi_0[:,3], psi_0[:,2], '.', color='b', alpha=alpha)
    if len(psi_pi3) != 0:
        plt.plot(psi_pi3[:,3], psi_pi3[:,2], 'y.', alpha=alpha)
        plt.plot(psi_pi3[:,3], psi_pi3[:,2], 'y.', alpha=alpha)
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.xlabel(r'$h$')
    plt.ylabel(r'$\theta$')
    plt.savefig(f'Figures/Phases_p{p}.pdf', dpi=300, bbox_inches='tight')
    plt.plot()
    





