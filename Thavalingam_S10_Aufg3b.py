# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:35:33 2023

@author: tjuva
"""

import numpy as np
import timeit

import os
import matplotlib.pyplot as plt

import Thavalingam_S10_Aufg3a as tsa


def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        sum = 0
    for i in range(width):
        m = []
        for j in range(1, width):
            buff = []
            for k in range(width):
                if k != i:
                    buff.append(matrix[j][k])
            m.append(buff)
        sign *= -1
        sum += mul * determinant(m, sign * matrix[0][i])
    return sum

#######################################
def gauss(A, b):
    A = A.astype(float)
    b = b.astype(float)

    anzahlAnZeilen = A.shape[0]

    Ab = np.append(A, b, axis=1)  

    for i in range(anzahlAnZeilen):
        if A[i][i] == 0:  
            j = checkForDiv0(i, Ab)
            if j == -99:
                raise Exception("Es gab eine Division durch 0!!!")
            else:
                Ab = zeilenTausch(Ab, i, j)
            alleInSpalteWerte0en(Ab, i)  
        Ab = alleInSpalteWerte0en(Ab, i)
    return [Ab[0:anzahlAnZeilen, 0:anzahlAnZeilen], getDeterminante(Ab), rueckwaertsEinsetzenXErhalten(Ab)]


def checkForDiv0(i, A):
    anzahlSpalten = A.shape[0]
    for j in range(i + 1,anzahlSpalten):  
        if A[j][i] != 0:
            return j
    return -99

def zeilenTausch(Ab, i, j):
    AbGetauscht = np.copy(Ab)  
    anzahlAnZeilen = Ab.shape[0]
    for k in range(anzahlAnZeilen + 1):
        AbGetauscht[i][k] = Ab[j][k]  
        AbGetauscht[j][k] = Ab[i][k]
    return AbGetauscht


def alleInSpalteWerte0en(Ab, i):
    anzahlAnZeilen = Ab.shape[0]
    ATempForEdit = np.copy(Ab)  
    for j in range(i + 1,anzahlAnZeilen):  
        lambdaWert = -ATempForEdit[j][i] / Ab[i][i]  
        ATempForEdit[j, :] = Ab[i, :] * lambdaWert + Ab[j,:]  
    return ATempForEdit


def getDeterminante(Ab):
    determinante = 1  
    anzahlAnZeilen = Ab.shape[0]
    for j in range(anzahlAnZeilen):
        determinante = determinante * Ab[j][j]  
    return determinante


def rueckwaertsEinsetzenXErhalten(Ab):
    anzahlAnZeilen = Ab.shape[0]  
    x = np.zeros(anzahlAnZeilen, np.float64)  
    i = anzahlAnZeilen - 1  
    while i >= 0:
        summe = 0
        for j in range(anzahlAnZeilen):
            summe = summe + Ab[i][j] * x[j]  
        x[i] = 1 / Ab[i][i] * (Ab[i][anzahlAnZeilen] - summe)  
        i = i - 1
    return x[:, np.newaxis]
########################################


dim = 30
A = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))
dum1 = np.arange(1,int(dim/2+1),dtype=np.float64).reshape((int(dim/2),1))
dum2 = np.arange(int(dim/2),0,-1,dtype=np.float64).reshape((int(dim/2),1))
x=np.append(dum1,dum2,axis=0)
b = A@x
x0 = np.zeros((dim,1))
tol = 1e-4


# Jacobi
t_start = timeit.default_timer()
[jacobi_xn, jacobi_n, jacobi_n2] = tsa.Thavalingam_S10_Aufg3a(A, b, x0, tol, "jacobi")
t_end = timeit.default_timer()
print ('jacobi:', 'xn = ', jacobi_xn, ', n = ', jacobi_n, ', n2 = ', jacobi_n2, ', time = ', t_end - t_start)


# Gauss Seidel
t_start = timeit.default_timer()
[gauss_seidel_xn, gauss_seidel_n, gauss_seidel_n2] = tsa.Thavalingam_S10_Aufg3a(A, b, x0, tol, "Seidel")
t_end = timeit.default_timer()
print ('gauss_seidel:', 'xn = ', gauss_seidel_xn, ', n = ', gauss_seidel_n, ', n2 = ', gauss_seidel_n2, ', time = ', t_end - t_start)


# Gauss-Verfahren
t_start = timeit.default_timer()
[gauss_A_triangle, gauss_detA, gauss_x] = gauss(A, b)
t_end = timeit.default_timer()
print ('gauss:', 'x = ', gauss_x, ', time = ', t_end - t_start)


# numpy.linalg.solve
t_start = timeit.default_timer()
np_xn = np.linalg.solve(A, b)
t_end = timeit.default_timer()
print("np.linalg.solve: xn = ", np_xn, ', time = ', t_end - t_start)

abs_err_jacobi = np.abs(x - jacobi_xn)
abs_err_gauss_seidel = np.abs(x - gauss_seidel_xn)
abs_err_gauss = np.abs(x - gauss_x)

figure, axis = plt.subplots()

i = np.arange(1, dim + 1)
plt.semilogy(i, abs_err_jacobi)
plt.semilogy(i, abs_err_gauss_seidel)
plt.semilogy(i, abs_err_gauss)

plt.xlabel("Vektorelement")
plt.ylabel("Abs Fehler")
plt.title("Vergleich abs. Fehler")
plt.legend(["Jacobi", "Gauss-Seidel", "Gauss"])

plt.savefig(os.path.splitext(os.path.basename(__file__))[0] + ".svg")
