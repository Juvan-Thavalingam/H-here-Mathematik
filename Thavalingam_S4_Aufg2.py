# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:06:58 2023

@author: tjuva
"""
import numpy as np
import matplotlib.pyplot as plt

start = 0.1
nit = 100000
amin = 0.25
amax = 4.0
step = 0.25
fig = 1

k = np.zeros(nit+1)
alpha = np.arange(amin, amax+0.25, 0.25)

for a in alpha:
    k[0] = start
    for j in np.arange(0,nit):
        k[j+1] = a * k[j]*(1-k[j])
    plt.figure(fig)
    plt.semilogx(k)
    plt.title('Alpha ='+str(a))
    plt.xlabel('Number of Iterations ')
    plt.ylabel('Iteration Value')
    fig = fig + 1
 
#0.1: anziehend 2: abstossend