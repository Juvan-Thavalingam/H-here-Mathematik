# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:24:20 2023

@author: tjuva
"""
import numpy as np
import math

def eps():
    eps = 1
    while 1:
        if(eps + 1) ==1:
            return eps * 2
        eps /= 2
   
print("Calculated eps: ", eps())
print("Given eps by the system: ", np.finfo(float).eps)
# Die Mantisse hat 16 stellen was 2^4 entspricht, deshalb arbeitet er im Dualsystem
print(np.finfo(float).dtype)    
   
def biggest_number():
    test_number = 1.0
    reference = 1.0
    multiplication_factor = 2.0
    # calculates roughly the biggest number
    while test_number != math.inf:
        reference = test_number
        test_number = test_number * multiplication_factor
    # calculates exact (regarding of how many correct digits desired) the biggest number
    correct_digits = 7
    exponent = round(math.log10(reference), 1) - correct_digits
    addition_factor = 10 ** exponent
    test_number = reference
    while test_number != math.inf:
        reference = test_number
        test_number = test_number + addition_factor
    return reference


print("Calculated biggest number: ", biggest_number())
print("Biggest number by the system: ", np.finfo(float).max)