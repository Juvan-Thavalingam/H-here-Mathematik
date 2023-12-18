# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:23:33 2023

@author: tjuva
"""

import numpy as np

f1 = lambda x : np.e ** (x**2)+x**(-3)-10

f2 = lambda x: (-1/3)*np.pi*(x**3)+5*np.pi*(x**2)-471


def sek(f, x0, x1, tol):
    x_prev = x0
    x = x1
    counter = 0
    while np.abs(x + x_prev) >= tol and counter < 10:
        x_next = (x - ((x-x_prev)/f(x)-f(x_prev))*f(x))
        x_prev = x
        x = x_next
        counter += 1
    return x


print(sek(f1,-1.0, -1.2, 0.001))
print(sek(f2, 9.0, 8.0, 0.001))