# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:12:57 2023

@author: tjuva
"""

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


def p(a, xmin, xmax):
    x = np.arange(-10, 10.01, 0.01, dtype='float64')
    p = 0  # Polyom
    dp = 0  # Ableitung
    pint = 0  # Integral

    for f_i, coeffi in enumerate(a):
        exp = len(a) - f_i - 1
        p += coeffi * x ** exp

    for pint_i, coeffi in enumerate(a):
        exp = len(a) - pint_i - 1
        pint += (coeffi / (exp + 1)) * x ** (exp + 1)

    for dp_i, coeffi in enumerate(a):
        exp = len(a) - dp_i - 1
        dp += exp * coeffi * x ** (exp - 1)

    return x, p, dp, pint
