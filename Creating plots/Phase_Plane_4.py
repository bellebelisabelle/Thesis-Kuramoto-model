''' This script creates the plots of theta* and the phase plane for the 
four-modal uniform external field. '''
from Functions_Theta import theta4
import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(0,10,1001)

# Import and choose the right values of theta*3 and theta*4.
thetastar3 = np.genfromtxt('Data (txt files)/Thetastar3.txt')
thetastar4 = np.genfromtxt('Data (txt files)/Thetastar4.txt')
ind = (abs(thetastar3[:,1] - theta4(thetastar3[:,0])) > 0.02)
thetastar3 = thetastar3[ind]

ind_pos = (thetastar3[:,1] > theta4(thetastar3[:,0]))
ind_neg = (thetastar3[:,1] <= theta4(thetastar3[:,0]))
thetastar3_u = thetastar3[ind_pos]
thetastar3_l = thetastar3[ind_neg]

# Make sure there is only one theta*3 per h.
ind_un_u = np.unique(thetastar3_u[:,0], return_index = True)[1]
ind_un_l = np.unique(thetastar3_l[:,0], return_index = True)[1]
thetastar3_u = thetastar3_u[ind_un_u]
thetastar3_l = thetastar3_l[ind_un_l]

# Make sure there is only one theta*4 per h.
ind_un = np.unique(thetastar4[:,0], return_index = True)[1]
thetastar4 = thetastar4[ind_un]

# Plot theta*3
plt.figure()
plt.plot(thetastar3_l[:,0], thetastar3_l[:,1], '.', label=r'$\theta_{3,u}^*$')
plt.plot(thetastar3_u[:,0], thetastar3_u[:,1], '.', label=r'$\theta_{3,l}^*$')
plt.xlim([0, 5])
plt.ylim([0, 8])
plt.legend()
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta_3^*$')
plt.savefig("Figures/Plot_thetastar3_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

# Plot theta*4
plt.figure()
plt.plot(thetastar4[:,0], thetastar4[:,1], '.')
plt.xlim([0, 5])
plt.ylim([0, 8])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta_4^*$')
plt.savefig("Figures/Plot_thetastar4_4.pdf",dpi=300,bbox_inches='tight')
plt.show()

# Define locations of labels of regions.
labels = np.array(['A:0(0)', r'$\longrightarrow$B:8(0/4)', r'$\longrightarrow$C:8(0)', 'D:16(4)', 'E:16(4)$\longleftarrow$', 'F:8(4)'])
hs = [3.5, 2, 4.55, 4.05, 3.15, 1.5]
thetas = [3, 3, 6.7, 7.2, 7.2, 6]

# Plot phase plane
plt.figure(figsize=(13, 8))
plt.plot(thetastar3_l[:,0], thetastar3_l[:,1], '--', label=r'$\theta_{3,u}^*$')
plt.plot(thetastar3_u[:,0], thetastar3_u[:,1], '--', label=r'$\theta_{3,l}^*$')
plt.plot(thetastar4[:,0], thetastar4[:,1], '--', label=r'$\theta_{4}^*$')
plt.plot(h, theta4(h), label=r'$\theta_4(h)$')
for i in range(0, len(labels)):
    plt.text(hs[i], thetas[i], labels[i], ha = 'center', va = 'center', size = 17)
plt.xticks([0, 0.815, 2, 3, 4, 5], [0, r'$\hat{h}\approx0.815$', 2, 3, 4, 5], size = 15)
plt.yticks(size = 15)
plt.plot([0.815, 0.815], [0, theta4(0.815)], 'k--', linewidth=1)
plt.xlim([0, 5])
plt.ylim([0, 8])
plt.legend(fontsize = 15)
plt.xlabel(r'$h$', fontsize = 15)
plt.ylabel(r'$\theta$', fontsize = 15)
plt.savefig("Figures/Plot_thetas_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

