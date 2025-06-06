''' In the thesis, some functions theta are given. 
The equations of them are given in this script. '''
import numpy as np
import scipy
i0 = np.i0
i1 = scipy.special.i1
iv = scipy.special.iv

# For the uniform field in two opposite directions:
def theta1(h):
    theta1 = i0(2*h)/(i0(2*h)-iv(2,2*h))
    return theta1

def theta2(h):
    theta2 = i0(2*h)**2/(i0(2*h)**2+i0(2*h)*iv(2,2*h)-2*i1(2*h)**2)
    return theta2

# For the non-uniform field in two opposite directions:
def thetap1(h): # = theta1(h)
    theta1 = i0(2*h)/(i0(2*h)-iv(2,2*h)) 
    return theta1

def thetap2(h, p):
    if p < 0.5:
        theta2 = h/(1-2*p)
    else:
        theta2 = h/(2*p-1)
    return theta2

# For the uniform field in cardinal directions:
def theta4(h):
    theta3 = i0(2*h)**2/(i0(2*h)**2-i1(2*h)**2)
    return theta3


