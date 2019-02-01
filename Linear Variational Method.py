# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:56:40 2019

@author: chongc
"""
import numpy as np
import sympy as sp

def H_ij(i,j):
    a = np.pi**2*j**2/200
    b = (1/5)*np.sin(i*np.pi/2)*np.sin(j*np.pi/2)
    
    if i == j:
        ham_int = a+b
        
    else:
        ham_int = b
        
    return ham_int

H_mat = np.zeros((3,3))

for i in range(1,4):
    for j in range(1,4):
        H_mat[i-1][j-1] = H_ij(i, j)
        
print(H_mat)

### create an empty numpy array for the c vector
c = np.zeros(3)
### assign c vector to be (1, 0, 0)
c[0] = 1

### compute H_mat * c and store it to a new array called Hc
Hc = np.dot(H_mat,c)

### compute c^t * Hc and store it to a variable E
E = np.dot(np.transpose(c),Hc)

### print the result
print(E)
    
    