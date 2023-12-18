# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:14:01 2023

@author: tjuva
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.99, 2.01, 0.02/500, dtype = 'float64' )

#Aufgabe_2a

def f1(x):
    return (x**7) - (14*x**6)+ (84*x**5)-(280*x**4)+(560*x**3)-(672*x**2)+(448*x)-128

def f2(x):
    return (x-2)**7


plt.grid()

plt.plot(x, f1(x), label ='f1')
plt.plot(x, f2(x), label = 'f2')
plt.legend()

plt.title('Darstellung eines Polynoms', 'Abl')



#Aufgabe_2b

limit = 1e-14
stepwidth = 1e-17
x = np.arange(-limit, limit, stepwidth)
g = x/(np.sin(1+x)-np.sin(1))
plt.figure(2)
#plt.plot(x, g), plt.xlabel('x'),plt.ylabel('y')



#Aufgabe_2c

g_new = x/(2*np.cos(1+x/2)*np.sin(x/2))
plt.figure(3)
plt.plot(x, g, x, g_new), plt.xlabel('x'),plt.ylabel('g_{new}(x)'),plt.legend()
plt.show()

