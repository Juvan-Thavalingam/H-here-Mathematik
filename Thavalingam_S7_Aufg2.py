# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:18:13 2023

@author: tjuva
"""

import numpy as np
from Thavalingam_S7_Aufg1 import gauss

#Aufgabe 2
x = np.array([[2,3,4], [0.8,2.2,3.6], [1.2,2,5.8]], dtype = float)
y = np.array([1, 2.4, 4], dtype = float)


print("Aufgabe 2")
print(gauss(x, y))