# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:26:39 2023

@author: tjuva
"""

import numpy as np


x = np.array([[1,0,2],[0,1,0],[0.0001,0, 0.0001]], dtype = float)

y = np.linalg.inv(x)
print(y)


