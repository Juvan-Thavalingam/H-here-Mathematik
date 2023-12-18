# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 08:53:49 2023

@author: tjuva
"""

import numpy as np

x = np.array([[0.76870177], 
              [-0.59385], 
              [0.2375415]], dtype=float)

y = np.array([0.76870177 , -0.59385, 0.2375415])


sol = np.array([[0.0,0.0,0.0],
              [0.0,0.0,0.0],
              [0.0,0.0,0.0]])

for i in range(3):
    for z in range(3):
        sol[i][z]= 2 * x[i][0]*y[z]

print(sol)        
    