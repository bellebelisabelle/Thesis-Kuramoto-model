''' This script compares for the bi-modal non-uniform field the analytically 
obtained phase plane with the numerical one for p = 0.35.'''
import numpy as np
import matplotlib.pyplot as plt
from Functions_Theta import thetap1, thetap2

ploth = np.arange(0, 10, 0.01)
p = 0.35
hs = np.array([6, 6, 6, 5.2, 3.7, 1.5])
thetas = np.array([4, 7, 8.2, 9, 9, 9])
sols = np.array([1, 3, 5, 7, 5, 3])

theta1_arr = thetap1(ploth)
theta2_arr = thetap2(ploth, p)

# Determine where thetap1 and thetap2 start.
hind = (thetap1(ploth)-thetap2(ploth,p)<0)

# Load theta*.
thetastar350 = np.genfromtxt('Data (txt files)/Thetastar_0_p0.35.txt')
thetastar35pi = np.genfromtxt('Data (txt files)/Thetastar_pi_p0.35.txt')
thetastar35pi = thetastar35pi[np.nonzero(thetastar35pi[:,0])]

# Split thetapi* in upper and lower part
part_l = (thetastar35pi[:,1] <= thetastar35pi[:,0] * 1.5 + 0.28)
part_u = (thetastar35pi[:,1] > thetastar35pi[:,0] * 1.5 + 0.28)

alpha = 0.1 

# Load solutions of the system obtained numerically.
psi_0 = np.loadtxt(f'Data (txt files)/Solutions_p{p}_psi0.txt')
psi_pi1 = np.loadtxt(f'Data (txt files)/Solutions_p{p}_psipi_1.txt')
psi_pi3 = np.loadtxt(f'Data (txt files)/Solutions_p{p}_psipi_3.txt')
psi_excluded = np.loadtxt(f'Data (txt files)/Solutions_p{p}_psiexcluded.txt')
psi_excluded = np.unique(psi_excluded[:, 3:], axis=0)

# Plot everything together
plt.figure()
plt.plot(ploth[hind], theta1_arr[hind], color='tab:orange', label=r'$\theta_{p1}$')
plt.plot(ploth[hind], theta2_arr[hind],'--', color='tab:orange', label=r'$\theta_{p2}$')

plt.plot(thetastar350[:,0], thetastar350[:,1], '--', color='tab:blue', label=r'$\theta_0^*$')
plt.plot(thetastar35pi[part_l,0], thetastar35pi[part_l,1], color='tab:green', label=r'$\theta_{\pi,l}^*$')
plt.plot(thetastar35pi[part_u,0], thetastar35pi[part_u,1], '--', color='tab:green', label=r'$\theta_{\pi,u}^*$')

plt.plot(psi_excluded[:,1], psi_excluded[:,0], 'r.', alpha=alpha)
plt.plot(psi_0[:,3], psi_0[:,2], 'b.', alpha = alpha)
plt.plot(psi_pi1[:,3], psi_pi1[:,2], 'y.', alpha = alpha)
if len(psi_pi3) != 0:
    plt.plot(psi_pi3[:,3], psi_pi3[:,2], 'y.', alpha=3*alpha)
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.legend(loc = 4)
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.savefig("Figures/Plot_thetas_compare_p.pdf", dpi=300, bbox_inches='tight')
plt.show()