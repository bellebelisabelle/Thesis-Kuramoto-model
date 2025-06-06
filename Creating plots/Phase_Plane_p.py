''' This script creates the plots of theta* and the phase plane for the 
bi-modal non-uniform external field, for p = 0.35. '''
import numpy as np
import matplotlib.pyplot as plt
from Functions_Theta import thetap1, thetap2

ploth = np.arange(0, 10, 0.01)
p = 0.35

# Create the arrays for the phase plane
theta1_arr = thetap1(ploth)
theta2_arr = thetap2(ploth, p)

thetastar350 = np.genfromtxt('Data (txt files)/Thetastar0_p0.35.txt')
thetastar35pi = np.genfromtxt('Data (txt files)/Thetastarpi_p0.35.txt')
thetastar35pi = thetastar35pi[np.nonzero(thetastar35pi[:,0])]

# Let thetap1 and thetap2 begin at the right place.
hind = (thetap1(ploth) - thetap2(ploth, p) < 0)

# Sererate the upper and lower part of theta*pi.
part_l = (thetastar35pi[:,1] <= thetastar35pi[:,0] * 1.5 + 0.28)
part_u = (thetastar35pi[:,1] > thetastar35pi[:,0] * 1.5 + 0.28)

# Plot theta*pi
plt.figure()
plt.plot(thetastar35pi[part_l,0], thetastar35pi[part_l,1], '.', label=r'$\theta_{\pi,l}^*$')
plt.plot(thetastar35pi[part_u,0], thetastar35pi[part_u,1], '.', label=r'$\theta_{\pi,l}^*$')
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta_\pi^*$')
plt.legend(loc = 2)
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.savefig("Figures/Plot_thetastar_pi.pdf", dpi=300, bbox_inches='tight')
plt.show()

# Plot theta*0
plt.figure()
plt.plot(thetastar350[:,0], thetastar350[:,1], '.')
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta_0^*$')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.savefig("Figures/Plot_thetastar_0.pdf", dpi=300, bbox_inches='tight')
plt.show()

# Define locations of labels of regions.
labels = np.array(['A:1(1)', 'B:3(2)', 'C:5(2)', 'D:7(2)', 'E:5(2)', 'F:3(1)'])
hs = [3.6, 3.6, 3.6, 3.6, 2.5, 1]
thetas = [2,4.4,5.4,6.2,6.2,6.2]

# Plot phase plane
plt.figure()
plt.plot(ploth[hind], theta1_arr[hind], color = 'tab:orange', label=r'$\theta_{p1}$')
plt.plot(ploth[hind], theta2_arr[hind], '--', color = 'tab:orange', label=r'$\theta_{p2}$')
plt.plot(thetastar350[:,0], thetastar350[:,1], '--', color='tab:blue', label=r'$\theta_0^*$')
plt.plot(thetastar35pi[part_l,0], thetastar35pi[part_l,1], color='tab:green', label=r'$\theta_{\pi,l}^*$')
plt.plot(thetastar35pi[part_u,0], thetastar35pi[part_u,1], '--', color='tab:green', label=r'$\theta_{\pi,u}^*$')
for i in range(0,len(hs)):
    plt.text(hs[i], thetas[i], labels[i], ha = 'center', va = 'center',size = 12)
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.legend(loc = 4)
plt.xlim([0, 5])
plt.ylim([0, 7])
plt.savefig("Figures/Plot_thetas_p.pdf", dpi=300, bbox_inches='tight')
plt.show()