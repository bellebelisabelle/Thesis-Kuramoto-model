''' This script performs an analysis on F2''(r).
We check for different (h,theta) how many zeros F2''(r) has in (0,1].
This turns out to be at most one, and therefore we check the first and last
value to see if it stays positive or negative, or how it changes sign. '''

from Functions_F2 import F2der2
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
dtheta = 0.1
dh = 0.1
r = np.arange(0, 1.01, dt)

analysis = np.zeros((301*301*len(r), 3))
# The arrays below show the change of sign of F2''(r).
alw_neg = np.array([[],[]]) 
alw_pos = np.array([[],[]])
neg_to_pos = np.array([[],[]])
pos_to_neg = np.array([[],[]])
w = 0
# We count the number of zeros by looking where there the sign differs by 2.
for i in range(0, 301):
    thetai = dtheta * i
    for j in range(0, 301):
        hj = dh * j
        sign = np.sign(F2der2(r, thetai, hj))
        diff = np.abs(np.diff(sign)) 
        zeros = np.count_nonzero(diff == 2)
        if zeros > 0:
            analysis[w,:] = np.array([thetai, hj, zeros])
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

# Plot of all pairs (h,theta) such that F2''(r) has one zero.
plt.figure()
plt.plot(analysis[mask_onezero,1], analysis[mask_onezero,0], '.', markersize = 0.5)
plt.plot([], [], '.', color='tab:blue', label='1 zero', markersize = 10)
plt.legend()
plt.xlim([0, 30])
plt.ylim([0, 30])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.savefig("Figures/Analysis_F2der2z.pdf", dpi=300, bbox_inches='tight')
plt.plot()

# Plot of all pairs with the different behaviors (staying positive/negative or changing sign).
plt.figure()
plt.plot(alw_pos[1,:], alw_pos[0,:], '.', markersize = 0.5)
plt.plot(alw_neg[1,:], alw_neg[0,:], '.', markersize = 0.5)
plt.plot(pos_to_neg[1,:],pos_to_neg[0,:],'.', markersize = 0.5)
plt.plot([], [], '.', color='tab:blue', label='always positive', markersize = 10)
plt.plot([], [], '.', color='tab:orange', label='always negative', markersize = 10)
plt.plot([], [], '.', color='tab:green', label='positive to negative', markersize = 10)
plt.legend()
plt.xlim([0, 30])
plt.ylim([0, 30])
plt.xlabel(r'$h$')
plt.ylabel(r'$\theta$')
plt.savefig("Figures/Analysis_F2der2v.pdf", dpi=300, bbox_inches='tight')
plt.show()



