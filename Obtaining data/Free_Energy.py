''' This script makes the array for the free energy landscape for the bi-modal
external fields. '''
import numpy as np
from scipy.integrate import quad

# The following functions define the total free energy.
def Q(x, phi, theta, h, r, psi):
    z = theta**2 * r**2 + h**2 + 2 * h * r * theta * np.cos(phi - psi)
    denom = 2 * np.pi * np.i0(2 * np.sqrt(z))
    numer = np.exp(2 * theta * r * np.cos(psi - x) + 2 * h * np.cos(phi - x))
    return numer / denom

def cosq(x, w, T, h, r, p):
    return np.cos(x) * Q(x, w, T, h, r, p)

def sinq(x, w, T, h, r, p):
    return np.sin(x) * Q(x, w, T, h, r, p)

def sumcos(q, T, h, r, p):
    integral_0, _ = quad(cosq, 0, 2 * np.pi, args=(0, T, h, r, p))
    integral_pi, _ = quad(cosq, 0, 2 * np.pi, args=(np.pi, T, h, r, p))
    return (q * integral_0 + (1-q) * integral_pi)

def sumsin(q, T, h, r, p):
    integral_0, _ = quad(sinq, 0, 2 * np.pi, args=(0, T, h, r, p))
    integral_pi, _ = quad(sinq, 0, 2 * np.pi, args=(np.pi, T, h, r, p))
    return (q * integral_0 + (1-q) * integral_pi)

def intcos(x, q, T, h, r, p, sumcos_val, sumsin_val):
    term_common = -T / 2 * (np.cos(x) * sumcos_val + np.sin(x) * sumsin_val)
    return q * (term_common - h * np.cos(x)) * Q(x, 0, T, h, r, p) + \
           (1-q) * (term_common + h * np.cos(x)) * Q(x, np.pi, T, h, r, p)

def intlong(q, T, h, r, p):
    sumcos_val = sumcos(q, T, h, r, p)
    sumsin_val = sumsin(q, T, h, r, p)
    integral, _ = quad(intcos, 0, 2 * np.pi, args=(q, T, h, r, p, sumcos_val, sumsin_val))
    return integral

def logterm(x, w, T, h, r, p):
    logterm = Q(x, w, T, h, r, p)*np.log(2*np.pi*Q(x, w, T, h, r, p))
    return logterm

def intlog(q, T, h, r, p):
    intlog_0, _ =  quad(logterm, 0, 2 * np.pi, args=(0, T, h, r, p))
    intlog_pi, _ = quad(logterm, 0, 2 * np.pi, args=(np.pi, T, h, r, p))
    return (q * intlog_0 + (1-q) * intlog_pi)

def total(q, T, h, r, p):
    total = intlog(q, T, h, r, p) / 2 + intlong(q, T, h, r, p)
    return total

psi = np.linspace(0, 2*np.pi, 101)
r = np.linspace(0, 1, 101)

R, PSI = np.meshgrid(r, psi)

#%% Bi-modal uniform external field
p = 0.5
h = 1
thetas = [1.0, 1.7, 2.5, 4]

for theta in thetas:
    Fplot = np.zeros((len(psi), len(r)))
    for j in range(0, len(r)):
        for i in range(0, len(psi)):
            Fplot[i,j] = total(p, theta, h, r[j], psi[i])
        print(j)
    np.savetxt(f'Data (txt files)/Free Energy (txt files)/FreeEnergy_p{p}_h{h}_theta{theta}.txt', Fplot)

#%% Bi-modal non-uniform external field
ps = [0.35, 0.65]
hs = [1.5, 3.7, 5.2, 6.0, 6.0, 6.0]
thetas = [9.0, 9.0, 9.0, 4.0, 7.0, 8.2]

for p in ps:
    for k in range(0, len(hs)):
        theta = thetas[k]
        h = hs[k]
        Fplot = np.zeros((len(psi), len(r)))
        for j in range(0, len(r)):
            for i in range(0, len(psi)):
                Fplot[i,j] = total(p, theta, h, r[j], psi[i])
            print(j)
        np.savetxt(f'Data (txt files)/Free Energy (txt files)/FreeEnergy_p{p}_h{h}_theta{theta}.txt', Fplot)




