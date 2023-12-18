# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:08:47 2023

@author: tjuva
"""
import numpy as np
import matplotlib.pyplot as plt



x = np.arange(-3, 3.01, 0.01, dtype = 'float64' )

fx = np.exp(x**2)+x**(-3)-10

plt.xlim(-2, 2)
plt.ylim(-10, 10)

plt.plot(x, fx, label = 'function')
plt.legend()
plt.show()

def f(x):
    return np.exp(x**2)+x**(-3)-10

def newton(x):
    return x - ((np.exp(x**2)+x**(-3)-10)/(2*x*np.exp(x**2)+(-3*x**(-4))))

def newtonVereinfacht(x):
    x0 = 0.5
    return x - ((np.exp(x**2)+x**(-3)-10)/(2*x0*np.exp(x0**2)+(-3*x0**(-4))))

def sekanten(xn,xn2):
    return xn - ((xn - xn2)/(f(xn)-f(xn2)))*f(xn)

x = 2
for i in range(4):
    x = newton(x)
    print(x)
    
print('\n')

x = 0.5
for i in range(4):
    x = newtonVereinfacht(x)
    print(x)

xn = -1
xn2 = -1.2
print('\n', xn)
print(xn2)
for i in range(4):
    x1 = sekanten(xn, xn2)
    xn = xn2
    print(x1)
    xn2 = x1
