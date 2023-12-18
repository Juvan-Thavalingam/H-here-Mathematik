# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix            
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]]) 
        [Q,R]=Serie8_Aufg2(A)

@author: knaa
"""

import numpy as np

def Serie8_Aufg2(A):
    
    A = np.copy(A)                       #necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')              #change to float
    
    n = np.shape(A)[0]
    
    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square') 
    
    Q = np.eye(n)
    R = A
    
    for j in np.arange(0,n-1):
        a = np.copy(R[j:, j]).reshape(n-j,1)       
        e = np.eye(n - j)[:,0].reshape(n-j,1)   
        length_a = np.linalg.norm(a)
        if a[0] >= 0: sig = 1  
        else: sig = -1 
        v = a + sig * length_a * e
        u = (1 / np.linalg.norm(v)) * v
        H = np.eye(n - j) - 2 * u @ u.T
        Qi = np.eye(n)
        Qi[j:,j:] = H[:, :]
        R = Qi @ R
        Q = Q @ Qi.T
        
    return(Q,R)

def check_QR_Decomposition(A, Q, R):
    (expectedQ, expectedR) = Serie8_Aufg2(A)

    if not np.allclose(expectedQ, Q, rtol=0, atol=10 ** (-3)):
        print('expected array Q is not equal to actual Q')
        print('expected Q: ', expectedQ)
        print('actual Q: ', Q)
        return False

    if not np.allclose(expectedR, R, rtol=0, atol=10 ** (-3)):
        print('expected array R is not equal to actual R')
        print('expected R: ', expectedR)
        print('actual R: ', R)
        return False

    return True

# 2b

print('\n')
print('Aufgabe 2b')
print('============================')
print()

# A = np.array([[3, 9, 12, 12],
#               [-2, -5, 7, 2],
#               [6, 12, 18, 6],
#               [3, 7, 38, 14]])
# (Q, R) = Serie8_Aufg2(A)

A = np.array([[1, 2, -1],
              [4, -2, 6],
              [3, 1, 0]])

Q = np.array([[-0.1961, 0.7191, -0.6667],
              [-0.7845, -0.5230, -0.3333],
              [-0.5883, 0.4576, 0.6667]])

R = np.array([[-5.0990, 0.5883, -4.5107],
              [0, 2.9417, -3.8570],
              [0, 0, -1.3333]])

print('is decomposition successful? ', check_QR_Decomposition(A, Q, R))


# 2c

print('\n')
print('Aufgabe 2c')
print('============================')
print()

import timeit

t1 = timeit.repeat("Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100)
t2 = timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)

avg_t1 = np.average(t1) / 100
avg_t2 = np.average(t2) / 100

print('avg_t1', avg_t1)
print('avg_t2', avg_t2)


# 2d
print('\n')
print('Aufgabe 2d')
print('============================')
print()

Test = np.random.rand(100, 100)

t1 = timeit.repeat("Serie8_Aufg2(Test)", "from __main__ import Serie8_Aufg2, Test", number=100)
t2 = timeit.repeat("np.linalg.qr(Test)", "from __main__ import np, Test", number=100)

avg_t1 = np.average(t1) / 100
avg_t2 = np.average(t2) / 100

print('avg_t1', avg_t1)
print('avg_t2', avg_t2)

# Die manuelle Zerlegung mehr Zeit benötigt als die QR Zerlegung von NumPy
