''' This script creates plots showing for which pairs there is a solution 
for F3(r) = r and F4(r) = r on (0,1]. '''
import matplotlib.pyplot as plt
import numpy as np
from Functions_Theta import theta4

# Load all pairs with solutions.
F3_sols = np.genfromtxt('Data (txt files)/Solutions_F3.txt')
F4_sols = np.genfromtxt('Data (txt files)/Solutions_F4.txt')

# Determine the number of zeros per pair.
ones3 = (F3_sols[:,2] == 1)
twos3 = (F3_sols[:,2] == 2)
thre3 = (F3_sols[:,2] == 3)

ones4 = (F4_sols[:,2] == 1)
twos4 = (F4_sols[:,2] == 2)

h = np.arange(0, 10.1, 0.1)

# Plot for F3(r) = r.
plt.figure()
plt.plot(F3_sols[ones3,1], F3_sols[ones3,0], '.', label='1 zero')
plt.plot(F3_sols[twos3,1], F3_sols[twos3,0], '.', label='2 zeros')
plt.plot(F3_sols[thre3,1], F3_sols[thre3,0], '.', label='3 zeros')
plt.plot(h, theta4(h), 'k', label=r'$\theta_4(h)$')
plt.legend()
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.savefig("Figures/AnF3_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

# Plot for F4(r) = r.
plt.figure()
plt.plot(F4_sols[ones4,1], F4_sols[ones4,0], '.', label='1 zero')
plt.plot(F4_sols[twos4,1], F4_sols[twos4,0], '.', label='2 zeros')
plt.plot(h, theta4(h), 'k', label=r'$\theta_4(h)$')
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.legend()
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.savefig("Figures/AnF4_4.pdf", dpi=300, bbox_inches='tight')
plt.show()






