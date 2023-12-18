# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:01:40 2023

@author: tjuva
"""

def f(x, n):
    print(x)
    while  n > 0:
        n-=1
        x = (230*x**4+18*x**3+9*x**2-9)/221
        print(x)
    return x

#f(1, 4)
#f(0, 4)

def banasch(x, n):
    b = f(x, n)
    print('Banasch: ', b)

banasch(-0.5, 1)