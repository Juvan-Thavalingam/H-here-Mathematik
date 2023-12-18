# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:57:00 2023

@author: tjuva
"""
import numpy as np

#Aufgabe 1
A = np.array([[20000,30000,10000], [10000,17000,6000], [2000,3000,2000]], dtype = float)
b = np.array([5200000, 3000000, 760000], dtype = float)

li = list()

def gauss(x, y):
    index = 0
    limit = len(x)-1

    while index < len(x):
        n = index + 1
        for i in range(limit):
            exp = x[n][index]/x[index][index] 
            li.append(exp)
            exp *= -1
            x[n] += x[index] * exp
            y[n] += y[index] * exp
            n+=1
            
        index+=1
        limit -= 1
        
    print("\nLösung:")
    sol = 1/x[len(x)-1][len(x)-1] * y[len(x)-1]
    z = list()
    z.append(sol)
    for i in range(len(x)-1):
        p = y[len(x)-i-2] 
        limit = len(x)-2-i
        for los in range(len(z)):
            p -= x[limit][len(x)-los-1]*z[los] 
        p /= x[limit][len(x)-2-los]
        z.append(p)
        
    z = list(reversed(z))
    return z


print("Aufgabe 1a: ", gauss(A, b))

