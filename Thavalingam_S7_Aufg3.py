# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:17:01 2023

@author: tjuva
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import lu


#Aufgabe 3
A = np.array([[8,4,2,1], [729,81,9,1], [2197,169,13,1], [0,0,0,1]], dtype = float)
b = np.array([104,172,152, 150], dtype = float)

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
    
xp = np.asarray(gauss(A,b))
def polynom(i):
    return np.polyval(xp, i)

x = []
y = []

for i in np.arange(0,13, 0.1):
    x.append(i + 1997) #0+1997
    y.append(polynom(i))

plt.plot(x, y, label="Polynom")
plt.xlabel("Jahr")
plt.ylabel("UV indikator")

#Aufgabe B
print("Aufgabe 3b")
print("Polynom:")
print("2003 = " + str(polynom(6)))
print("2004 = " + str(polynom(7)))

#Aufgabe C

x = np.array([1997,1999,2006,2010])
y = np.array([150,104,172,152])

z = np.polyfit(x, y, 3)
p = np.poly1d(z)

plt.plot(x,y, label="Werte")

x = []
y = []

for i in np.arange(1997,2010, 0.25):
    x.append(i)
    y.append(p(i))

print("\nAufgabe 3c")
print("Polyfit:")
print("2003 = " + str(p(2003)))
print("2004 = " + str(p(2004)))

plt.plot(x,y, ".", label="Polyfit")
plt.legend()

