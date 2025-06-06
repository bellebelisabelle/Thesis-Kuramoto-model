''' This script creates the plots of theta* and the phase plane for the 
bi-modal uniform external field. '''
from Functions_Theta import theta1, theta2
import numpy as np
import matplotlib.pyplot as plt

h = np.arange(0, 2, 0.01)
hbar = 0.5144428 # See script Determining_hbar_hhat.py

theta1_arr = theta1(h)
theta2_arr = theta2(h)

thetastar = np.genfromtxt(fname='Data (txt files)/Thetastar.txt')

# Plot theta*
plt.figure()
plt.plot(thetastar[:,0], thetastar[:,1], '.')
plt.xlabel(r'$h$')
plt.xticks([hbar, 2, 4, 6, 8, 10], [r'$\overline{h}\approx0.514$', 2, 4, 6, 8, 10])
plt.ylabel(r'$\theta^*$')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.savefig("Figures/Plot_thetastar.pdf", dpi=300, bbox_inches='tight')
plt.show()

# Define locations of labels of regions.
hs = [1.5, 1.5, 1.5, 0.5]
thetas = [1, 2.35, 4.5, 4.5]
labels = ['0(0)', '2(2)', '6(2)', '4(2)']

# Plot phase plane
plt.figure()
plt.plot(h, theta1_arr, color='tab:orange', label=r'$\theta_1$')
plt.plot(thetastar[:,0], thetastar[:,1], '--', color='tab:blue', label=r'$\theta^*$')
plt.plot(h, theta2_arr, color='tab:green', label=r'$\theta_2$')
for i in range(0,len(hs)):
    plt.text(hs[i], thetas[i], labels[i], ha = 'center', va = 'center',size = 12)
plt.xlabel(r'$h$')
plt.xticks([0, hbar, 1, 1.5, 2],[0, r'$\overline{h}\approx0.514$', 1, 1.5, 2])
plt.plot([hbar, hbar], [0, theta2(hbar)], 'k--', linewidth = 1)
plt.ylabel(r'$\theta$')
plt.legend()
plt.xlim([0, 2])
plt.ylim([0, 7])
plt.savefig("Figures/Plot_thetas.pdf", dpi=300, bbox_inches='tight')
plt.show()