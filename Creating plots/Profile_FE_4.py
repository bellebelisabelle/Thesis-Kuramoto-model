''' This script creates plots of the profiles of the free energy at psi = pi/4. '''
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

p = 4 # As we consider the four-modal uniform external field.

# This part calculates the free energy for given theta (T), h (h), r (r) and psi (p).
def Q(x, phi, theta, h, r, psi):
    z = theta**2 * r**2 + h**2 + 2 * h * r * theta * np.cos(phi - psi)
    denom = 2 * np.pi * np.i0(2 * np.sqrt(z))
    numer = np.exp(2 * theta * r * np.cos(psi - x) + 2 * h * np.cos(phi - x))
    return numer / denom

def cosq(x, w, T, h, r, p):
    return np.cos(x) * Q(x, w, T, h, r, p)

def sinq(x, w, T, h, r, p):
    return np.sin(x) * Q(x, w, T, h, r, p)

def sumcos(T, h, r, p):
    int_0, _ = quad(cosq, 0, 2 * np.pi, args=(0, T, h, r, p))
    int_pi, _ = quad(cosq, 0, 2 * np.pi, args=(np.pi, T, h, r, p))
    int_pi2, _ = quad(cosq, 0, 2 * np.pi, args=(np.pi/2, T, h, r, p))
    int_3pi2, _ = quad(cosq, 0, 2 * np.pi, args=(3*np.pi/2, T, h, r, p))
    return (int_0 + int_pi + int_pi2 + int_3pi2) / 4

def sumsin(T, h, r, p):
    int_0, _ = quad(sinq, 0, 2 * np.pi, args=(0, T, h, r, p))
    int_pi, _ = quad(sinq, 0, 2 * np.pi, args=(np.pi, T, h, r, p))
    int_pi2, _ = quad(sinq, 0, 2 * np.pi, args=(np.pi/2, T, h, r, p))
    int_3pi2, _ = quad(sinq, 0, 2 * np.pi, args=(3*np.pi/2, T, h, r, p))
    return (int_0 + int_pi + int_pi2 + int_3pi2) / 4

def intcos(x, T, h, r, p, sumcos_val, sumsin_val):
    term_common = -T / 2 * (np.cos(x) * sumcos_val + np.sin(x) * sumsin_val)
    return (term_common - h * np.cos(x)) * Q(x, 0, T, h, r, p) + \
           (term_common + h * np.cos(x)) * Q(x, np.pi, T, h, r, p) +\
               (term_common - h * np.sin(x)) * Q(x, np.pi/2, T, h, r, p) + \
                      (term_common + h * np.sin(x)) * Q(x, 3*np.pi/2, T, h, r, p)

def intlong(T, h, r, p):
    sumcos_val = sumcos(T, h, r, p)
    sumsin_val = sumsin(T, h, r, p)
    integral, _ = quad(intcos, 0, 2 * np.pi, args=(T, h, r, p, sumcos_val, sumsin_val))
    return integral / 4

def logterm(x, w, T, h, r, p):
    logterm = Q(x, w, T, h, r, p)*np.log(2*np.pi*Q(x, w, T, h, r, p))
    return logterm

def intlog(T, h, r, p):
    int_0, _ = quad(logterm, 0, 2 * np.pi, args=(0, T, h, r, p))
    int_pi, _ = quad(logterm, 0, 2 * np.pi, args=(np.pi, T, h, r, p))
    int_pi2, _ = quad(logterm, 0, 2 * np.pi, args=(np.pi/2, T, h, r, p))
    int_3pi2, _ = quad(logterm, 0, 2 * np.pi, args=(3*np.pi/2, T, h, r, p))
    return (int_0 + int_pi + int_pi2 + int_3pi2) / 4

def total(T, h, r, p):
    total = intlog(T, h, r, p) / 2 + intlong(T, h, r, p)
    return total

# Create the plots
psi = np.pi/4
r = np.linspace(0,1,51)

for h in [1.5, 2, 2.5]:
    if h == 1.5:
        thetas = np.array([2.68, 2.71, 2.74, 2.77])
    if h == 2:       
        thetas = np.array([3.42, 3.45, 3.48, 3.51])
    if h == 2.5:
        thetas = np.array([4.16, 4.18, 4.20, 4.22])
    Fplot = np.zeros(len(r))
    plt.figure()
    for j in range(0, len(thetas)):
        theta = thetas[j]
        for i in range(0, len(r)):
            Fplot[i] = total(theta, h, r[i], psi)
        plt.plot(r, Fplot, label = fr'$\theta={theta}$')
    plt.xlabel(r'$r$')
    plt.ylabel(r'$\mathcal{F}\ \left(0,\frac{\pi}{4}\right)$')
    plt.xlim([0, 1])
    plt.legend()
    plt.savefig(f'Free Energy/Profile_FE_p{p}_h{h}.pdf', dpi=300, bbox_inches='tight')
    plt.show()