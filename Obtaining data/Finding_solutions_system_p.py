''' This scripts looks if there are solutions for the system of the bi-modal
non-uniform external field. This system is given in another script. '''
from Functions_System_to_solve_p import sys_eq1, sys_eq2
from Functions_F0_Fpi import F0, Fpi
import numpy as np

values_r = np.arange(0, 1.01, 0.01)
values_psi = np.arange(0, 2*np.pi + 0.01, 0.01)

r, psi = np.meshgrid(values_r, values_psi)

thetas = np.linspace(0.1, 10, 100)
hs = np.linspace(0.1, 10, 100)
ps = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45])

# We first exclude psi = 0 and psi = pi. We have to satisfy two equations.
for p in ps:
    solutions = []
    for theta in thetas:
        for h in hs:
            eq1_arr = sys_eq1(p, r, psi, theta, h)
            eq2_arr = sys_eq2(p, r, psi, theta, h)

            mask = (np.abs(eq1_arr) < 0.001) & (np.abs(eq2_arr) < 0.001)
            valid_r = r[mask]
            valid_psi = psi[mask]

            for i in range(len(valid_r)):
                solutions.append([p, valid_r[i], valid_psi[i], theta, h])

    solutions = np.array(solutions)
    np.savetxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psiexcluded.txt', solutions)

# We now look for solutions with F0(r) = r.
for p in ps:
    solutions_list = []
    for h in hs:
        for theta in thetas:
            zero = 0
            F0_arr = np.sign(F0(values_r, theta, h, p) - values_r)
            
            zero_count = np.sum(np.abs(np.diff(F0_arr)) == 2)
            
            if zero_count > 0:
                solutions_list.append([p, values_r[0], theta, h, zero_count])

    solutions = np.array(solutions_list) if solutions_list else np.empty((0, 5))
    np.savetxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psi0.txt', solutions)

# We now look for solutions with Fpi(r) = r.
for p in ps:
    solutions_list = [] 
    for h in hs:
        for theta in thetas:
            zero = 0
            Fpi_arr = np.sign(Fpi(values_r, theta, h, p) - values_r)
            
            zero_count = np.sum(np.abs(np.diff(Fpi_arr)) == 2)
            
            if zero_count > 0:
                solutions_list.append([p, values_r[0], theta, h, zero_count])

    solutions = np.array(solutions_list) if solutions_list else np.empty((0, 5))
    ones, threes = [solutions[solutions[:, 4] == i] for i in [1, 3]]
    np.savetxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psipi_1.txt', ones)
    np.savetxt(f'Data (txt files)/Solutions bi-modal non-uniform field/Solutions_p{p}_psipi_3.txt', threes)






