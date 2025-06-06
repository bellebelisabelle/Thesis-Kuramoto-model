''' This script contains the system we want to solve for the non-uniform field
in two directions. 
The system consists of eq1(r,psi) = r and eq2(r,psi) = 0.
We find that psi = 0 and psi = pi always satisfy and with that, we can rewrite
this system a little different. '''

import numpy as np
import scipy

i0 = np.i0
i1 = scipy.special.i1
iv = scipy.special.iv

def g(z):
    g = i1(2*np.sqrt(z))/(np.sqrt(z)*i0(2*np.sqrt(z)))
    return g

# This equation needs to be equal to r.
def eq1(p,r,psi,theta,h):
    zmin = h**2 + theta**2 * r**2 - 2 * theta * h * r * np.cos(psi)
    zplus = h**2 + theta**2 * r**2 + 2 * theta * h * r * np.cos(psi)
    eq1 = p * g(zplus) * (h * np.cos(psi) + theta * r) \
        - (1-p) * g(zmin) * (h * np.cos(psi) - theta * r)
    return eq1

# This equation needs to be equal to 0.
def eq2(p,r,psi,theta,h):
    zmin = h**2 + theta**2 * r**2 - 2 * theta * h * r * np.cos(psi)
    zplus = h**2 +  theta**2 * r**2 + 2 * theta * h * r * np.cos(psi)
    eq2 = -h * np.sin(psi) * (p * g(zplus) - (1-p) * g(zmin))
    return eq2

# Suppose that psi = 0 or psi = pi. Then the system of the two equations above 
# can be rewritten as the following, where both equations need to be 0.
def sys_eq1(p,r,psi,theta,h):
    zplus = h**2 + theta**2 * r**2 + 2 * theta * h * r * np.cos(psi)
    sys_eq1 = g(zplus) - 1 / (2 * theta * p)
    return sys_eq1

def sys_eq2(p,r,psi,theta,h):
    zmin = h**2 + theta**2 * r**2 - 2 * theta * h * r * np.cos(psi)
    sys_eq2 = g(zmin) - 1 / (2 * theta * (1-p))
    return sys_eq2

    