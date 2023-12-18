# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:49:08 2023

@author: tjuva
"""

import numpy as np
import timeit

def fact_rec(n):
    # y = fact_rec(n) berechnet die Fakultät von n als fact_rec(n) = n * fact_rec(n -1) mit fact_rec(0) = 1
    # Fehler, falls n < 0 oder nicht ganzzahlig
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)


print(fact_rec(10))

def fact_recFor(n):
    x = 1
    for i in range(n):
            x *= i+1
    return x

print(fact_recFor(10))



t1=timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
average1 = sum(t1)/len(t1)

t2=timeit.repeat("fact_recFor(500)", "from __main__ import fact_recFor", number=100)

average2 = sum(t2)/len(t2)
print("Rekursiv: ", average1)
print("For-Loop: ", average2)


# Frage 1: Die for-Schleife ist schneller, da es viel weniger funtionsaufrufe gibt.
# Frage 2: Ganze Zahlen haben kein Limit. Reelle Zahlen haben ihr Limit zwischen fact(170) und fact(171).
