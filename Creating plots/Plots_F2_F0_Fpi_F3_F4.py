''' This script creates plots with different behaviors of F2, F0, Fpi, F3 and F4. '''
from Functions_F2 import F2
from Functions_F0_Fpi import F0, Fpi
from Functions_F3_F4 import F3, F4
from Functions_Theta import theta2
import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0, 1.01, 0.01)

#%% F2
hs = np.array([0.4, 1.5, 1.5, 1.5])
thetas = np.array([1, 2.6, 3.5, 5.5])
plt.figure()
for i in range(0, len(hs)):
    h = hs[i]
    theta = thetas[i]
    plt.plot(r, F2(r, theta, h), label=fr'$(h,\theta)=({h},{theta})$')
plt.plot(r, F2(r, theta2(1.5), 1.5), label=r'$(h,\theta)=(\theta_2,1.5)$')
plt.plot(r, r, '--', label='$r$')
plt.legend()
plt.xlabel(r'$r$')
plt.ylabel('$F_2(r)$')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.savefig("Figures/SituationF2.pdf", dpi=300, bbox_inches='tight')
plt.show()

#%% Fpi for p = 0.35
p = 0.35
hs = [0.1, 4.0, 4.0, 4.0, 4.0]
thetas = [1.3, 4.0, 5.2, 6.5, 8.5]

plt.figure()
for i in range(0,len(hs)):
    h = hs[i]
    theta = thetas[i]
    plt.plot(r, Fpi(r,theta,h,p), label=fr'$(h,\theta)=({h},{theta})$')
plt.plot(r, r, '--', label='$r$')
plt.xlabel(r'$r$')
plt.ylabel(r'$F_\pi(r)$')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.legend()
plt.savefig("Figures/Plot_Fpi_p.pdf", dpi=300, bbox_inches='tight')
plt.show()

#%% F0 for p = 0.35
h = 1.0
thetas = np.array([0.9, 2, 2.47, 3])

plt.figure()
for theta in thetas:
    plt.plot(r, F0(r, theta, h, p), label=fr'$(h,\theta)=({h},{theta})$')
plt.plot(r, r, '--', label='$r$')
plt.legend()
plt.xlabel(r'$r$')
plt.ylabel(r'$F_0(r)$')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.savefig("Figures/Plot_F0_p.pdf", dpi=300, bbox_inches='tight')
plt.show()

#%% F3
h = 5
thetas = np.array([7, 9, 11, 13])  

plt.figure()
for theta in thetas:
    plt.plot(r, F3(r, theta, h), label=fr'$(h,\theta)=({h},{theta})$')
plt.plot(r, r, '--', label='$r$')
plt.legend()
plt.xlabel(r'$r$')
plt.ylabel(r'$F_3(r)$')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.savefig("Figures/Plot_F3_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

#%% F4
hs = [7.0, 7.0, 7.0, 7.0, 0.8]
thetas = [4.0, 6.0, 12, 16, 3.0] 

plt.figure()
for i in range(0,len(hs)):
    h = hs[i]
    theta = thetas[i]
    plt.plot(r, F4(r,theta,h), label=fr'$(h,\theta)=({h},{theta})$')
plt.plot(r, r, '--', label='$r$')
plt.legend()
plt.xlabel(r'$r$')
plt.ylabel(r'$F_4(r)$')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.savefig("Figures/Plot_F4_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

