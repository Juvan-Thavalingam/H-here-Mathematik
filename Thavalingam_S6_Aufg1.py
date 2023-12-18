# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:04:14 2023

@author: tjuva
"""

import numpy as np

x = np.array([[20.0,10.0,0.0], [50.0,30.0,20.0], [200.0,150.0,100.0]])
y = np.array([150.0, 470.0, 2150.0])
#y = np.array([120.0, 350.0, 1600.0])
li = list()


def gauss():

    index = 0
    limit = len(x)-1

    while index < len(x):
        n = index + 1
        for i in range(limit):
            exp = x[n][index]/x[index][index] 
            li.append(exp)
            exp *= -1
            x[n] += x[index] * exp
            y[n] += y[index] * exp
            n+=1
            
        index+=1
        limit -= 1
       
    
    print("\nDreiecksmatrix: ")
    for i in range(len(x)):
        print(x[i], y[i])
        
    print('\nZ: ', li)
        
    print("\nLösung:")
    sol = 1/x[len(x)-1][len(x)-1] * y[len(x)-1]
    z = list()
    z.append(sol)
    for i in range(len(x)-1):
        p = y[len(x)-i-2] 
        limit = len(x)-2-i
        for los in range(len(z)):
            p -= x[limit][len(x)-los-1]*z[los] 
        p /= x[limit][len(x)-2-los]
        z.append(p)
        
    print(list(reversed(z)))


#Aufgabe 3:
#x = np.array([[4.0,-1.0,-5.0], [-12.0,4.0,17.0], [32.0,-10.0,-41.0]])        
#y = np.array([-5, 19, -39])   

#x = np.array([[2.0,7.0,3.0], [-4.0,-10.0,0.0], [12.0,34.0,9.0]])        
#y = np.array([25.0, -24.0, 107.0])  

#x = np.array([[-1.0,1.0,1.0], [0.0,-2.0,-1.0], [5.0,1.0,4.0]])    
#y = np.array([0, 5, 3])    

#x = np.array([[-2.0,5.0,4.0], [-14.0,38.0,22.0], [6.0,-9.0,-27.0]])        
#y = np.array([16.0, 82.0, -120.0])     

#x = np.array([[-1.0, 2.0, 3.0, 2.0, 5.0, 4.0, 3.0, -1.0],
#              [3.0, 4.0, 2.0, 1.0, 0.0, 2.0, 3.0, 8.0],
#              [2.0, 7.0, 5.0, -1.0, 2.0, 1.0, 3.0, 5.0],
#              [3.0, 1.0, 2.0, 6.0, -3.0, 7.0, 2.0 -2.0],
#              [5.0, 2.0, 0.0, 8.0, 7.0, 6.0, 1.0, 3.0],
#              [-1.0, 3.0, 2.0, 3.0, 5.0, 3.0, 1.0, 4.0],
#              [8.0, 7.0, 3.0, 6.0, 4.0, 9.0, 7.0, 9.0],
#              [-3.0, 14.0, -2.0, 1.0, 0.0, -2.0, 10.0, 5.0]])

#y = np.array([-11, 103, 53, -20, 95, 78, 131, -26])


gauss()

print("Numpy-function: ",np.linalg.solve(x,y))

def determinante(a):
    sol = 1
    for i in range(len(x)):
        sol *= a[i][i]
    print("Determinante: ", sol)    
    
determinante(x)
        
        
    