# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:37:09 2023

@author: tjuva
"""

import matplotlib.pyplot as plt
import numpy as np

#import matplotlib as mpl

x = np.arange(-10, 10.01, 0.01, dtype = 'float64' )

f = x**5-5*x**4-30*x**3+110*x**2+29*x-105
f_Diff = 5*x**4-20*x**3-90*x**2+220*x+29
f_Int = np.divide(x * ((x**5) - (6 * x**4) - (45 * x**3) + (220 * x**2) + (87 * x) - 630), 6)


plt.plot(x, f, label ='f(x)')
plt.plot(x, f_Diff, label = 'f`(x)')
plt.plot(x, f_Int, label = 'F(x)')
plt.xlim(-8, 8)
plt.ylim(-1500, 1500)
plt.legend('Polynom f(x)', 'Ableitung')
plt.title('Darstellung eines Polynoms', 'Abl')
plt.xlabel('Label', 'xLabel')
plt.ylabel('Label', 'yLabel')
plt.subplots_adjust(bottom=.10, left=.15)


plt.legend()
plt.show()
