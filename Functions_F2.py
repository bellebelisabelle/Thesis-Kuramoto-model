''' This script contains F1, and F2 and its derivatives. 
These functions are important for the bi-modal uniform field.'''
import numpy as np
import scipy
i0 = np.i0
i1 = scipy.special.i1
iv = scipy.special.iv

def F2(r,theta,h):
    F2 = 0
    for eta in np.array([-1,1]):
        x = 2* (theta * r + h * eta)
        F2 += i1(x) / i0(x)
    return 1/2*F2

def F2der(r,theta,h):
    F2der = 0
    for eta in np.array([-1,1]):
        x = 2* (theta * r + h * eta)
        F2der += 2 * theta * (1/2 + 1/2 * iv(2,x) / i0(x) - (i1(x)/i0(x))**2)
    return 1/2*F2der

def F2der2(r,theta,h):
    F2der2 = 0
    for eta in np.array([-1,1]):
        x = 2* (theta * r + h * eta)
        I0 = i0(x)
        I1 = i1(x)
        I2 = iv(2,x)
        I3 = iv(3,x)
        F2der2 += 4 * theta**2* (1/I0 * (I3/4 - 3*I1/4) - 3/2 * I1*I2 / I0**2 + 2 * I1**3 / I0**3)
    return 1/2*F2der2

def F2der3(r,theta,h):
    F2der3 = 0
    for eta in np.array([-1,1]):
        x = 2* (theta * r + h * eta)
        I0 = i0(x)
        I1 = i1(x)
        I2 = iv(2,x)
        I3 = iv(3,x)
        I4 = iv(4,x)
        term0 = -3/8
        term1 = (-I2 + I4/8)
        term2 = -I1*I3 - 3 / 4 * I2**2 + 3 * I1**2
        term3 = 6 * I1**2 * I2
        term4 = -6*I1**4
        F2der3 += 8*theta**3*(term0 + term1/I0 + term2/I0**2 + term3/I0**3 + term4/I0**4)
    return 1/2*F2der3
