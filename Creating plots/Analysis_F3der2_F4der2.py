''' This script performs an analysis on F3''(r) and F4''(r).
We check for (h,theta) in a certain region how many zeros they have in (0,1).
For F3''(r), it turns out to be at most two, and therefore we check if it starts
positive or negative.
For F4''(r), it turns out to be at most one, and therefore we check the first and 
last value to see if it stays positive or negative, or how it changes sign. '''

from Functions_F3_F4 import F3der2, F4der2
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
dtheta = 0.1
dh = 0.1
r = np.arange(0, 1.01, dt)

# We count the number of zeros by looking where there the sign differs by 2.

#%% F3''(r)
analysis = np.zeros((301*301*len(r), 3))
neg = np.array([[],[]])
pos = np.array([[],[]])
w = 0
for i in range(0, 301):
    thetai = dtheta * i
    for j in range(0, 301):
        hj = dh * j
        sign = np.sign(F3der2(r, thetai, hj))
        diff = np.abs(np.diff(sign))
        zeros = np.count_nonzero(diff == 2)
        if zeros > 0:
            analysis[w,:] = np.array([thetai, hj, zeros])
            w += 1
            
        if sign[1] == -1:
            neg = np.concatenate((neg, np.array([[thetai],[hj]])), axis = 1)
        
        if sign[1] == 1:
            pos = np.concatenate((pos, np.array([[thetai],[hj]])), axis = 1)

# Counts how many pairs there are with 1, 2 or more zeros
mask_onezero = (analysis[:,2] == 1)
mask_twozero = (analysis[:,2] == 2)
mask_morezero = (analysis[:,2] > 2)

# Plot of all pairs (h,theta) such that F3''(r) has one or two zeros.
plt.figure()
plt.plot(analysis[mask_onezero,1], analysis[mask_onezero,0], '.', markersize = 0.5)
plt.plot(analysis[mask_twozero,1], analysis[mask_twozero,0], '.', markersize = 0.5)
plt.plot([], [], '.', label='1 zero', color='#1f77b4', markersize = 10)
plt.plot([], [], '.', label='2 zeros', color='#ff7f0e', markersize = 10)
plt.legend()
plt.xlim([0, 30])
plt.ylim([0, 30])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.savefig("Figures/Analysis_F3der2z_4.pdf", dpi=300, bbox_inches='tight')
plt.plot()

# Plot of all pairs with (h,theta) such that F3''(r) starts negative (which are all).
plt.figure()
plt.plot(neg[1,:], neg[0,:], '.', markersize = 0.5)
plt.plot([],[],'.',label='starts negative', color='#1f77b4', markersize = 10)
plt.legend(loc = 4)
plt.xlim([0, 30])
plt.ylim([0, 30])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.savefig("Figures/Analysis_F3der2v_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

#%% F4''(r)
analysis = np.zeros((301*301*len(r), 3))
# The arrays below show the change of sign of F4''(r).
alw_neg = np.array([[],[]])
alw_pos = np.array([[],[]])
neg_to_pos = np.array([[],[]])
pos_to_neg = np.array([[],[]])
w = 0
for i in range(0,301):
    thetai = dtheta * i
    for j in range(0,301):
        hj = dh * j
        sign = np.sign(F4der2(r,thetai,hj))
        diff = np.abs(np.diff(sign))
        zeros = np.count_nonzero(diff==2)
        if zeros > 0:
            analysis[w,:] = np.array([thetai,hj,zeros])
            w += 1
        
        if sign[1] == -1 and sign[len(sign)-1] == -1:
            alw_neg = np.concatenate((alw_neg, np.array([[thetai],[hj]])), axis = 1)
            
        if sign[1] == 1 and sign[len(sign)-1] == 1:
            alw_pos = np.concatenate((alw_pos, np.array([[thetai],[hj]])), axis = 1)
            
        if sign[1] == -1 and sign[len(sign)-1] == 1:
            neg_to_pos = np.concatenate((neg_to_pos, np.array([[thetai],[hj]])), axis = 1)
            
        if sign[1] == 1 and sign[len(sign)-1] == -1:
            pos_to_neg = np.concatenate((pos_to_neg, np.array([[thetai],[hj]])), axis = 1)

# Counts how many pairs there are with one or more zeros.
mask_onezero = (analysis[:,2] == 1)
mask_morezero = (analysis[:,2] > 1)

# Plot of all pairs (h,theta) such that F4''(r) has one zero.
plt.figure()
plt.plot(analysis[mask_onezero,1], analysis[mask_onezero,0], '.', markersize = 0.5)
plt.plot([], [], '.', label='1 zero', color='tab:blue', markersize = 10)
plt.legend()
plt.xlim([0,30])
plt.ylim([0,30])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.savefig("Figures/Analysis_F4der2z_4.pdf", dpi=300, bbox_inches='tight')
plt.plot()

# Plot of all pairs with the different behaviors (staying positive/negative or changing sign).
plt.figure()
plt.plot(alw_pos[1,:], alw_pos[0,:], '.', markersize = 0.5)
plt.plot(alw_neg[1,:], alw_neg[0,:], '.', markersize = 0.5)
plt.plot(pos_to_neg[1,:], pos_to_neg[0,:], '.', markersize=0.5)
plt.plot([], [], '.', color='tab:blue', label='always positive', markersize=10)
plt.plot([], [], '.', color='tab:orange', label='always negative', markersize=10)
plt.plot([], [], '.', color='tab:green', label='positive to negative', markersize=10)
plt.legend(loc = 4)
plt.xlim([0, 30])
plt.ylim([0, 30])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.savefig("Figures/Analysis_F4der2v_4.pdf", dpi=300, bbox_inches='tight')
plt.show()

