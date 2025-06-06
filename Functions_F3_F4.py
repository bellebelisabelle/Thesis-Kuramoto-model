''' This script contains F3, F4, and their derivatives. 
These functions are important for the uniform field in cardinal directions.'''
import numpy as np
import scipy

i1 = scipy.special.i1
i0 = np.i0
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

def g(z):
    g = i1(2*np.sqrt(z))/(np.sqrt(z)*i0(2*np.sqrt(z)))
    return g

def gder(z):
    gder = (i0(2*np.sqrt(z))*iv(2,2*np.sqrt(z))-i1(2*np.sqrt(z))**2)/(z*i0(2*np.sqrt(z))**2)
    return gder

def gder2(z):
    I0 = i0(2*np.sqrt(z))
    I1 = i1(2*np.sqrt(z))
    I2 = iv(2,2*np.sqrt(z))
    I3 = iv(3,2*np.sqrt(z))
    gder2 = 1/(2*z*np.sqrt(z)*I0)*(I3-I1)\
        -1/(z**2*I0**4)*(I0*I2-I1**2)*(I0**2+2*np.sqrt(z)*I0*I1)
    return gder2

def gder3(z): #CHECKED
    I0 = i0(2*np.sqrt(z))
    I1 = i1(2*np.sqrt(z))
    I2 = iv(2,2*np.sqrt(z))
    I3 = iv(3,2*np.sqrt(z))
    I4 = iv(4,2*np.sqrt(z))
    part1 = I1*I2+1/2*I0*(I1+I3)-I1*(I0+I2)
    part2 = np.sqrt(z)*z*I0**2
    dpart1 = 1/np.sqrt(z)*(1/2*(I0+I2)*I2 + 1/2*I1*(I1+I3)\
          +1/2*I1*(I1+I3)+1/4*I0*(I0+2*I2+I4)\
              -(I0+I2)**2/2 - I1*(I1+1/2*(I1+I3)))
    dpart2 = 3/2*np.sqrt(z)*I0**2 + 2*z*I0*I1
    
    part3 = (I0*I2-I1**2)*(I0**2+2*np.sqrt(z)*I0*I1)
    dpart3 = 1/np.sqrt(z)*(I0*I2-I1**2)*\
        (3*I0*I1+2*np.sqrt(z)*I1**2+np.sqrt(z)*I0*(I0+I2))\
            +1/np.sqrt(z)*(I0**2+2*np.sqrt(z)*I0*I1)*(I1*I2+1/2*I0*(I1+I3)-I1*(I0+I2))
    part4 = (z**2*I0**4)
    dpart4 = 2*z*I0**4+4*z*np.sqrt(z)*I1*I0**3
    
    gder3 = 1/(part2**2) * (dpart1 * part2 - part1 * dpart2)\
        - 1/part4**2 * (dpart3 * part4 - part3 * dpart4)
    return gder3

def F3(r,theta,h):
    w = h**2+theta**2*r**2
    F0 = F2(r,theta,h)/2 + theta*r/2*g(w)
    return F0
    
def F3der(r,theta,h):
    w = h**2+theta**2*r**2
    wder = 2*theta**2*r
    F0der = 1/2 * F2der(r,theta,h) + theta/2*g(w) + theta*r/2*wder*gder(w)
    return F0der
    
def F3der2(r,theta,h):
    w = h**2+theta**2*r**2
    wder = 2*theta**2*r
    wder2 = 2*theta**2
    F0der2 = 1/2 * F2der2(r,theta,h) + theta*wder*gder(w) \
        + theta * r / 2 * wder2 * gder(w) + theta * r * wder**2 / 2 * gder2(w)
    return F0der2

def F3der3(r,theta,h):
    w = h**2+theta**2*r**2
    wder = 2*theta**2*r
    wder2 = 2*theta**2
    F0der3 = 1/2 * F2der3(r,theta,h) \
        + theta * wder2 * gder(w) + theta * wder**2 * gder2(w)\
        + theta/2*wder2*gder(w) + theta*r/2 * wder2 * wder * gder2(w)\
        + theta * wder**2 / 2 * gder2(w) + theta * r * 2 * wder2 * wder / 2 * gder2(w)\
            + theta * r * wder**3 / 2 * gder3(w)
    return F0der3

def F4(r,theta,h):
    c_pos = h**2 + theta**2 * r**2 + np.sqrt(2) * theta * r * h 
    c_neg = h**2 + theta**2 * r**2 - np.sqrt(2) * theta * r * h
    F0 = theta*r/2 * (g(c_pos)+g(c_neg))+h*np.sqrt(2)/4*(g(c_pos)-g(c_neg))
    return F0
    
def F4der(r,theta,h):
    c_pos = h**2 + theta**2 * r**2 + np.sqrt(2) * theta * r * h 
    c_neg = h**2 + theta**2 * r**2 - np.sqrt(2) * theta * r * h
    dc_pos = 2 * theta**2 * r + np.sqrt(2) * theta * h 
    dc_neg = 2 * theta**2 * r - np.sqrt(2) * theta * h 
    F4der = theta*r/2 * (dc_pos*gder(c_pos)+dc_neg*gder(c_neg))\
        + h*np.sqrt(2)/4 * (dc_pos*gder(c_pos)-dc_neg*gder(c_neg))\
        + theta/2*(g(c_pos)+g(c_neg))
    return F4der

def F4der2(r,theta,h):
    c_pos = h**2 + theta**2 * r**2 + np.sqrt(2) * theta * r * h 
    c_neg = h**2 + theta**2 * r**2 - np.sqrt(2) * theta * r * h
    dc_pos = 2 * theta**2 * r + np.sqrt(2) * theta * h 
    dc_neg = 2 * theta**2 * r - np.sqrt(2) * theta * h 
    d2c = 2 * theta**2
    F4der2 = theta**2*(3*theta*r+3/np.sqrt(2)*h)*gder(c_pos)\
        + theta**2*(3*theta*r-3/np.sqrt(2)*h)*gder(c_neg)\
            + 1/4*theta**2*(2*theta*r+h*np.sqrt(2))**3*gder2(c_pos)\
                + 1/4*theta**2*(2*theta*r-h*np.sqrt(2))**3*gder2(c_neg)
    return F4der2

def F4der3(r,theta,h):
    c_pos = h**2 + theta**2 * r**2 + np.sqrt(2) * theta * r * h 
    c_neg = h**2 + theta**2 * r**2 - np.sqrt(2) * theta * r * h
    dc_pos = 2 * theta**2 * r + np.sqrt(2) * theta * h 
    dc_neg = 2 * theta**2 * r - np.sqrt(2) * theta * h 
    d2c = 2 * theta**2  
    F4der2 = theta/2 * (d2c*gder(c_pos)+d2c*gder(c_neg))\
        + theta/2 * (dc_pos**2*gder2(c_pos)+dc_neg**2*gder2(c_neg))\
            \
        + theta/2 * (dc_pos**2*gder2(c_pos)+dc_neg**2*gder2(c_neg))\
        + theta*r/2 * (2*d2c*dc_pos*gder2(c_pos)+2*d2c*dc_neg*gder2(c_neg))\
        + theta*r/2 * (dc_pos**3*gder3(c_pos)+dc_neg**3*gder3(c_neg))\
            \
        + theta/2 * (d2c*gder(c_pos)+d2c*gder(c_neg))\
        + theta*r/2 * (d2c*dc_pos*gder2(c_pos)+d2c*dc_neg*gder2(c_neg))\
            \
        + h*np.sqrt(2)/4 * (2*d2c*dc_pos*gder2(c_pos)-2*d2c*dc_neg*gder2(c_neg))\
        + h*np.sqrt(2)/4 * (dc_pos**3*gder3(c_pos)-dc_neg**3*gder3(c_neg))\
            \
        + h*np.sqrt(2)/4 * (d2c*dc_pos*gder2(c_pos)-d2c*dc_neg*gder2(c_neg))\
            \
        + theta/2*(d2c*gder(c_pos)+d2c*gder(c_neg))\
        + theta/2*(dc_pos**2*gder2(c_pos)+dc_neg**2*gder2(c_neg))
    return F4der2



