# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:24:41 2023

@author: tjuva
"""

import numpy as np
from Thavalingam_S9_Aufg2 import *
import matplotlib.pyplot as plt

all_dxmax = np.array([])
all_dxobs = np.array([])
dxmax_dxobs = np.array([])
index = np.arange(0,1000,1)

for i in range(1000):
    A = np.random.rand(100,100)
    b = np.random.rand(100,1)
    A_disturb = A + np.random.rand(100,100)/1e5
    b_disturb = b + np.random.rand(100,1)/1e5
    [x, x_disturb, dxmax, dxobs] = S9_solution(A, A_disturb, b, b_disturb)
    all_dxmax = np.append(all_dxmax, [dxmax], axis=0)
    all_dxobs = np.append(all_dxobs, [dxobs], axis=0)
    dxmax_dxobs = np.append(dxmax_dxobs, [dxmax/dxobs], axis=0)


plt.figure(1)
plt.semilogy(all_dxmax)
plt.semilogy(all_dxobs)
plt.semilogy(dxmax_dxobs)
plt.legend(["dxmax", "dxob", "dxmax/dxobs"])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Aufgabe 3 Serie 9")
plt.show()

#Die obere Schranke "dxmax" liegt immer über "dxobs", deswegen ist das Resultat realistisch! 
#Obere Schranke liegt etwa 10^(-3) über "dxobs"!