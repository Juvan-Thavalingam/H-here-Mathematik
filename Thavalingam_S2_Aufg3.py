# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:31:51 2023

@author: tjuva
"""

import matplotlib.pyplot as plt
import numpy as np


def phi(n):
    return n*s2n(n)

def s2n(n):
    if n == 6:
        return 1
    if n >= 6:
        return np.sqrt(2 - 2 * np.sqrt(1- (s2n(n/2) ** 2 / 4)))
    
def phiB(n):
    return s2nB(n) * n

def s2nB(n):
    if n == 6:
        return 1
    if n >= 6:
        quads = s2nB(n/2)**2
        return np.sqrt(quads / (2*(1+np.sqrt(1 - quads/4))))

        
x = []
y1 = []
y2 = []

for i in range(0, 30):
    x.append(6*2**i)

for value in x:
    y1.append(phi(value))
    y2.append(phiB(value))

plt.plot(x, y1, x, y2)

plt.xlabel('number of edges')
plt.xscale("log")
plt.ylabel('2π approximation')
plt.title('Archimedes Algorithm')
plt.legend(['3a', '3b'])
plt.grid()
plt.figure()