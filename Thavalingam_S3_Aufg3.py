# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:37:51 2023

@author: tjuva
"""

import numpy as np
from matplotlib import pyplot as plt 

#(i)

def fi(x):
    return 5 / (2*x**2)**(1/3)

x = np.arange(-10, 10, 0.1)
y = fi(x)

plt.plot(x, y)
plt.semilogy()
plt.show()


###############################################################################


#(ii)
import numpy as np
from matplotlib import pyplot as plt 

def fii(x):
    return 10 ** 5 * ((2 * np.e) ** (-1/100)) ** x

x = np.arange(-10, 10, 0.1)
y = fii(x)

print('Steigung: ' + str((np.log(fii(5))-np.log(fii(0)))/5))
print('Steigung(errechnet): ' + str(np.log((2*np.e) ** (-1/100))))
print('Y-Achsenabschnitt: ' + str(fii(0)))

plt.plot(x, y)
plt.semilogy()
plt.show()


###############################################################################


#(iii)

def fiii(x):
    return (10**(2*x) / 10**(5*x)) ** 2

x = np.arange(-10, 10, 0.1)
y = fiii(x)

print('Steigung: ' + str((np.log(fiii(5))-np.log(fiii(0)))/5))
print('Steigung(errechnet): ' + str(np.log((2*np.e) ** (-1/100))))
print('Y-Achsenabschnitt: ' + str(fiii(0)))

plt.plot(x, y)
plt.semilogy()
plt.show()