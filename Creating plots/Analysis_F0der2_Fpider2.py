''' This script performs an analysis on F0''(r) and Fpi''(r).
We check for different (h,theta) how many zeros they have in (0,1].
For F0''(r) this turns out to be at most 1.
For Fpi''(r) this turns out to be at most 2. '''

from Functions_F0_Fpi import F0der2, Fpider2
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
r = np.arange(0, 1.01, dt)
ps = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45])

# We count the number of zeros by looking where there the sign differs by 2.
# We perform the analysis on every p.

#%% Fpi''(r)
def an_Fpi(p):
    dtheta = 0.1
    dh = 0.1
    analysis = np.zeros((301*301*len(r), 3))
    w = 0
    for i in range(1, 301):
        thetai = dtheta * i
        for j in range(1, 301):
            hj = dh * j
            sign = np.sign(Fpider2(r, thetai, hj, p))
            diff = np.abs(np.diff(sign))
            zeros = np.count_nonzero(diff == 2)
            if zeros > 0:
                analysis[w,:] = np.array([thetai, hj, zeros])
                w += 1
    return analysis

# We do this for every p
for p in ps:
    an = an_Fpi(p)

    mask_onezero = (an[:,2] == 1)
    mask_twozero = (an[:,2] == 2)
    mask_morezero = (an[:,2] > 2)
    
    
    # Plot of all pairs (h,theta) such that Fpi''(r) has one or two zeros.
    plt.figure()
    plt.plot(an[mask_onezero,1], an[mask_onezero,0], '.', markersize = 0.5)
    plt.plot(an[mask_twozero,1], an[mask_twozero,0], '.', markersize = 0.5)
    plt.plot([], [], '.', color='tab:blue', label='1 zero', markersize = 10)
    plt.plot([], [], '.', color='tab:orange', label='2 zeros', markersize = 10)
    plt.legend(loc = 4)
    plt.xlim([0, 30])
    plt.ylim([0, 30])
    plt.xlabel(r'$h$')
    plt.ylabel(r'$\theta$')
    plt.savefig(f"Figures/Analysis_Fpider2_p{p}.pdf", dpi=300, bbox_inches='tight')
    plt.plot()

#%% F0''(r)
def an_F0(p):
    dtheta = 0.1
    dh = 0.1
    analysis = np.zeros((301*301*len(r), 3))
    w = 0
    for i in range(1, 301):
        thetai = dtheta * i
        for j in range(1, 301):
            hj = dh * j
            sign = np.sign(F0der2(r, thetai, hj, p))
            diff = np.abs(np.diff(sign))
            zeros = np.count_nonzero(diff == 2)
            if zeros > 0:
                analysis[w,:] = np.array([thetai, hj, zeros])
                w += 1
    return analysis

for p in ps:
    an = an_F0(p)

    mask_onezero = (an[:,2] == 1)
    mask_twozero = (an[:,2] > 1)
        
    # Plot of all pairs (h,theta) such that F0''(r) has one zero.
    plt.figure()
    plt.plot(an[mask_onezero,1], an[mask_onezero,0], '.', markersize = 0.5)
    plt.plot([], [], '.', color='tab:blue', label='1 zero', markersize = 10)
    plt.legend(loc = 4)
    plt.xlim([0, 30])
    plt.ylim([0, 30])
    plt.xlabel(r'$h$')
    plt.ylabel(r'$\theta$')
    plt.savefig(f"Figures/Analysis_F0der2_p{p}.pdf", dpi=300, bbox_inches='tight')
    plt.plot()
    
