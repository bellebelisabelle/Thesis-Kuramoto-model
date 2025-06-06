''' This script contains the simulations done to study region B of the 
bi-modal non-uniform external field. '''
import numpy as np
import matplotlib.pyplot as plt
import random
import time

t = time.time()

def angle(x,y):
    if x <= 0:
        psi = np.arctan(y/x)+np.pi 
    else:
        psi = np.arctan(y/x)
        psi = psi % (2*np.pi)
    return psi  

def r_psi(xi):
    repsi = 1/len(xi)*np.e**(1j*xi)
    repsi = np.sum(repsi)
    r = abs(repsi)
    normalization = repsi / r
    psi = angle(np.real(normalization),np.imag(normalization))
    return r, psi  

def f(x, m, e, n, matrix=False):
    if matrix:
        S = np.sum(np.sin(x[:, None] - x[None, :]), axis=0)
    else:
        S = np.zeros(len(x))
        for i in range(len(x)):
            S += np.sin(x[i] - x)
    #t2 = time.time()
    #print('loop: ', time.time() - t2)
    #t2 = time.time()
    #print('matrix: ', time.time()-t2)
    y = x + (S * theta / m + h * np.sin(e-x)) * dt + n
    return y % (2 * np.pi)

def give_eta(num):
    eta = random.choices([0, np.pi/2, np.pi, 3*np.pi/2],weights = [1,1,1,1],k=num)
    return np.array(eta)

def give_time(t):
    secs = t % 60
    t = int((t - secs) / 60)
    mins = t % 60
    t = int((t - mins) / 60)
    return(str(t) + ' hr, ' + str(mins) + ' min, ' + str(secs) + ' sec')

print(time.asctime(time.localtime()))

M = 3000
Iter = 10000

print(M, Iter)

dt = 0.01
theta = 4.16
h = 2.5

t1 = time.time()

for k in range(0,20):
    X_U = np.random.uniform(0,2*np.pi, M)
    X_VM = np.random.vonmises(np.pi/4,2,size=M)%(2*np.pi)
    
    eta_U = give_eta(M)
    eta_VM = give_eta(M)
    r_eta_U, psi_eta_U = r_psi(eta_U)
    r_eta_VM, psi_eta_VM = r_psi(eta_VM)
    
    r_U, r_VM, psi_U, psi_VM = np.zeros((4, Iter))
    
    for i in range(0,Iter):
        noise_U = np.random.normal(0, np.sqrt(dt), M)
        noise_VM = np.random.normal(0, np.sqrt(dt), M)
        
        Y_U = f(X_U, M, eta_U, noise_U)
        Y_VM = f(X_VM, M, eta_VM, noise_VM)
        
        r_U[i], psi_U[i] = r_psi(Y_U)
        r_VM[i], psi_VM[i] = r_psi(Y_VM)
        
        X_U = Y_U
        X_VM = Y_VM
        
        #if i % 100 == 0: print(i / 100)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
    l1, = ax1.plot([0, Iter], [r_eta_U, r_eta_U], '--', color='tab:cyan', alpha=0.7, label=r'$r\ (\varphi_U)$')
    l2, = ax1.plot([0, Iter], [r_eta_VM, r_eta_VM], '--', color='tab:green', alpha=0.7, label=r'$r\ (\varphi_{VM})}$')
    ax1.plot(r_U,'.',color='tab:cyan',markersize=1)
    ax1.plot(r_VM,'.',color='tab:green',markersize=1)
    ax1.set_ylabel(r'$r$')
    l3, = ax1.plot(-1,-1,'.',color='tab:cyan',label=r'Uniform')
    l4, = ax1.plot(-1,-1,'.',color='tab:green',label=r'Von Mises')
    ax1.set_xlabel('Iteration')
    fl1 = ax1.legend(handles=[l1,l2], loc ='upper left')
    ax1.legend(handles=[l3,l4], loc ='upper right')
    ax1.add_artist(fl1)
    #ax1.title.set_text('M='+str(M))
    ax1.set_xlim([0,Iter])
    ax1.set_ylim([0,1])

    l5, = ax2.plot([0, Iter], [psi_eta_U, psi_eta_U], '--', color = 'tab:orange', alpha=0.7, label=r'$\psi\ (\varphi_U)$')
    l6, = ax2.plot([0, Iter], [psi_eta_VM, psi_eta_VM], '--', color = 'tab:red', alpha=0.7, label=r'$\psi\ (\varphi_{VM})}$')
    ax2.plot(psi_U,'.',color='tab:orange',markersize=1)
    ax2.plot(psi_VM,'.',color='tab:red',markersize=1)
    l7, = ax2.plot(-1,-1,'.',color='tab:orange',label=r'Uniform')
    l8, = ax2.plot(-1,-1,'.',color='tab:red',label=r'Von Mises')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel(r'$\psi$')
    fl2 = ax2.legend(handles=[l5,l6], loc ='upper left')
    ax2.legend(handles=[l7,l8], loc ='upper right')
    ax2.add_artist(fl2)
    ax2.set_xlim([0,Iter])
    ax2.set_ylim([0,2*np.pi])
    #ax2.title.set_text('M='+str(M))
    ax2.set_yticks([0,np.pi/2,np.pi,3*np.pi/2, 2*np.pi],['0',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
    plt.savefig(f'Time Evolution/TE for weird region/M{M}/sim5_M{M}_I{Iter}_{k}.png',dpi=300,bbox_inches='tight')
    plt.show()
    print(give_time(round(time.time() - t1)))
    t1 = time.time()
    
print('total: ' + give_time(round(time.time() - t)))


