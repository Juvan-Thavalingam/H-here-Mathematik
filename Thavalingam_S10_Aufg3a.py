# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:22:49 2023

@author: tjuva
"""

import numpy as np


def jacobi(A, b, x0, tol):

    L = np.tril(A, -1)
    D_inv = np.diag(1/np.diag(A))
    R = np.triu(A, 1)
    B = np.matmul(-D_inv, (L+R))

    x_old = x0
    iter = 0
    calc = True
    while (calc):
        x_comp = np.matmul(np.matmul(-D_inv, (L + R)), x_old) + np.matmul(D_inv, b)
        if ((np.linalg.norm(B, np.inf)/(1-np.linalg.norm(B, np.inf))*np.linalg.norm((x_comp - x_old), np.inf)) < tol):
            calc = False
        x_old = x_comp
        iter = iter + 1

    apriori = np.ceil((np.log((tol*(1-np.linalg.norm(B, np.inf)))/(np.linalg.norm((np.matmul(np.matmul(-D_inv, (L + R)), x0) + np.matmul(D_inv, b)-x0), np.inf))))/np.log(np.linalg.norm(B, np.inf)))

    return [x_old, iter, apriori]

def seidel(A, b, x0, tol):

    L = np.tril(A, -1)
    D = np.diag(np.diag(A))
    R = np.triu(A, 1)
    B = np.matmul(-np.linalg.inv(D+L), R)

    x_old = x0
    iter = 0
    calc = True
    while (calc):
        x_comp = np.matmul(np.matmul(-np.linalg.inv(D+L), R), x_old) + np.matmul(np.linalg.inv(D+L), b)
        if ((np.linalg.norm(B, np.inf)/(1-np.linalg.norm(B, np.inf))*np.linalg.norm((x_comp - x_old), np.inf)) < tol):
            calc = False
        x_old = x_comp
        iter = iter + 1

    apriori = np.ceil((np.log((tol*(1-np.linalg.norm(B, np.inf)))/(np.linalg.norm((np.matmul(np.matmul(-np.linalg.inv(D+L), R), x_old) + np.matmul(np.linalg.inv(D+L), b) -x0), np.inf))))/np.log(np.linalg.norm(B, np.inf)))
    return [x_old, iter, apriori]

def Thavalingam_S10_Aufg3a(A, b, x0, tol, opt):

    if (opt == "jacobi"):
        return jacobi(A, b, x0, tol)
    else:
        return seidel(A, b, x0, tol)



A = np.array([[8, 5, 2],
              [5, 9, 1],
              [4, 2, 7]])

x0 = np.array([[1],
               [-1],
               [3]])

b = np.array([[19],
              [5],
              [34]])               

print(Thavalingam_S10_Aufg3a(A, b, x0, 10**-4, "jacobi"))
print(Thavalingam_S10_Aufg3a(A, b, x0, 10**-4, "seidel"))