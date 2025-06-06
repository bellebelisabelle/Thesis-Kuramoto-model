''' This scripts looks if there are solutions for F3(r) = r and F4(r) = 4 on 
(0,1], for the four-modal uniform external field. '''
from Functions_F3_F4_4 import F3, F4, F3der, F4der
import numpy as np

r = np.arange(0, 1.01, 0.01)
thetas = np.linspace(0, 30, 301)
hs = np.linspace(0, 30, 301)

# Finding solutions for F3(r) = r
solutions_list = []
for h in hs:
    for theta in thetas:
        zero = 0
        F3_arr = np.sign(F3(r, theta, h) - r)
        
        zero_count = np.sum(np.abs(np.diff(F3_arr)) == 2)
        
        if zero_count > 0:
            solutions_list.append([theta, h, zero_count])

solutions = np.array(solutions_list)
np.savetxt('Data (txt files)/Solutions_F3.txt', solutions)

# Finding solutions for F4(r) = r
solutions_list = []
for h in hs:
    for theta in thetas:
        zero = 0
        F2_arr = np.sign(F4(r, theta, h) - r)
        
        zero_count = np.sum(np.abs(np.diff(F2_arr)) == 2)
        
        if zero_count > 0:
            solutions_list.append([theta, h, zero_count])

solutions = np.array(solutions_list)
np.savetxt('Data (txt files)/Solutions_F4.txt', solutions)



