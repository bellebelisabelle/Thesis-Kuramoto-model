''' This script makes the array for the free energy landscape for the four-modal
external field. '''
import numpy as np
from scipy.integrate import quad

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

psi = np.linspace(0, 2*np.pi, 101)
r = np.linspace(0, 1, 101)

R, PSI = np.meshgrid(r, psi)

#%% Four-modal uniform external field
p = 4
hs = [4.0, 2.5, 6.0, 5.0, 4.3, 2.0]
thetas = [2.0, 4.2, 9.0, 9.0, 9.0, 9.0]

for k in range(0, len(hs)):
    h = hs[k]
    theta = thetas[k]
    Fplot = np.zeros((len(psi), len(r)))
    for j in range(0, len(r)):
        for i in range(0, len(psi)):
            Fplot[i,j] = total(thetas[k], hs[k], r[j], psi[i])
        print(j)
    np.savetxt(f'Data (txt files)/Free Energy (txt files)/FreeEnergy_p{p}_h{h}_theta{theta}.txt', Fplot)
