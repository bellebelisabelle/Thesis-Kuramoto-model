''' This script determines hbar and hhat. It also plots K and K4. '''
from Functions_F2 import F2der3
from Functions_F3_F4 import F4der3
import matplotlib.pyplot as plt
import numpy as np

#%% Determine hbar
def K(h):
    K = F2der3(0, 1, h)
    return K

# Determine where K has the lowest absolute value, that is hhat.
h = np.arange(0.51, 0.52, 0.0000001)
K_arr = K(h)
K_abs = abs(K(h))
h_bar = h[np.argmin(K_abs)]
print(h_bar)

# Plot the function with hbar.
h = np.arange(0, 2.001, 0.001)
plt.figure()
plt.plot([0,2],[0,0], 'black', linewidth=0.8)
plt.plot(h, K(h), 'tab:orange')
plt.plot(h_bar-0.005, 0, '.', color='tab:blue', markersize=10)
plt.text(h_bar-0.005, 0.03, r'$\overline{h}$', ha = 'right', va = 'baseline')
plt.xlabel(r'$h$')
plt.ylabel(r'$K(h)$')
plt.xlim((0,2))
plt.savefig("Figures/Kh_hbar.pdf", dpi=300, bbox_inches='tight')
plt.show()

#%% Determine hhat

def K4(h):
    K4 = F4der3(0, 1, h)
    return K4

h = np.arange(0.81,0.82,0.0000001)
# Determine where K4 has the lowest absolute value, that is hhat.
K_arr = K4(h)
K_abs = abs(K4(h))
h_hat = h[np.argmin(K_abs)]
print(h_hat)

# Plot the function with hhat.
h = np.arange(0.00001, 2.001, 0.001)
plt.figure()
plt.plot([0,2], [0,0], 'black', linewidth=0.8)
plt.plot(h, K4(h), 'tab:orange')
plt.plot(h_hat-0.005, 0, '.', color='tab:blue', markersize=10)
plt.text(h_hat-0.005, 0.03, r'$\hat{h}$', ha = 'right', va = 'baseline')
plt.xlabel(r'$h$')
plt.ylabel(r'$K_4(h)$')
plt.xlim([0, 2])
plt.savefig("Figures/Kh_hbar_4.pdf", dpi=300, bbox_inches='tight')
plt.show()