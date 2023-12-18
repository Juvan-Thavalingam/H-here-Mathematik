# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:59:05 2023

@author: tjuva
"""

import numpy as np


d = 10
v = 471
#•vf = (np.pi*h**2)/6*(3*d-2*h)

def fixpunkt(y):
    return((3*d*np.pi-(6*v/y**2))/2*np.pi)

def newton(n):
    return n - ((-1/3)*np.pi*(n**3)+5*np.pi*(n**2)-471)/((-n)**2*np.pi+(10*np.pi)*n)

def vol(x):
    return ((np.pi*x**2)/6*(3*d-(2*x)))

h = 9
iterate = 0
while vol(h) > (v + 10**-3) or vol(h) < v - (10**-3):
    print(h)
    h = newton(h)
    iterate = iterate + 1

print(h, 'n: ', iterate)