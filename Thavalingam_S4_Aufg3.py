# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:25:03 2023

@author: tjuva
"""

import numpy as np

#Aufgabe 3b

def f(x): 
    return np.sin(x)+0.5*np.pi

point = 0

for i in range(0,50):
    value = f(point)
    print(i, value)
    point = value
    
# Kovergierend 2.3098814