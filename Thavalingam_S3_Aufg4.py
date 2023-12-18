# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:36:08 2023

@author: tjuva
"""
#4a
import numpy as np
from matplotlib import pyplot as plt 

def h(x):
    return np.sqrt(100*x**2-200*x+99)

x = np.linspace(0.75, 1.25, 100)
y = h(x)

plt.plot(x, y)
plt.show()


###############################################################################





###############################################################################

#4c
# Die Kondition geht bei 1.1 gegen unendlich. Deshalb gibt es keine bessere Umformung ohne Auslöschung.