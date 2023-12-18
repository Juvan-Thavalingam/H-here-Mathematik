# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:07:25 2023

@author: tjuva
"""


import numpy as np
import numpy.linalg

def calc_q_r(A, A_disturb, b, b_disturb):
    Q, R = numpy.linalg.qr(A)
    x = np.linalg.solve(R, np.transpose(Q)@b)

    Q_disturb, R_disturb = numpy.linalg.qr(A_disturb)

    x_disturb = np.linalg.solve(R_disturb, np.transpose(Q_disturb)@b_disturb)

    return x, x_disturb

def dx_max(A, A_disturb, b, b_disturb):
    cond_A = numpy.linalg.cond(A, np.inf)

    A_norm = numpy.linalg.norm(A, np.inf)
    A_minus_A_disturb_norm = numpy.linalg.norm(A - A_disturb, np.inf)

    b_norm = numpy.linalg.norm(b, np.inf)
    b_minus_b_disturb_norm = numpy.linalg.norm(b - b_disturb, np.inf)

    norm_A_fraction = A_minus_A_disturb_norm / A_norm
    norm_b_fraction = b_minus_b_disturb_norm / b_norm

    error_condition = cond_A * norm_A_fraction

    if error_condition < 1:
        return (cond_A / (1 - cond_A * norm_A_fraction)) * (norm_A_fraction + norm_b_fraction)
    else:
        return numpy.nan


def norm(x, x_disturb):
    x_norm = numpy.linalg.norm(x, np.inf)
    x_minus_x_disturb_norm = numpy.linalg.norm(x - x_disturb, np.inf)

    return x_minus_x_disturb_norm / x_norm


def S9_solution(A, A_disturb, b, b_disturb):
    x, x_disturb = calc_q_r(A, A_disturb, b, b_disturb)

    max_rel_error = dx_max(A, A_disturb, b, b_disturb)

    real_rel_error = norm(x, x_disturb)

    return x, x_disturb, max_rel_error, real_rel_error

A = np.array([[20, 30, 10],
              [10, 17, 6],
              [2, 3, 2]])
b = np.array([[5720],
              [3300],
              [836]])

A_disturb = A-0.1

b_disturb = b+100

x, x_disturb, max_rel, real_rel = S9_solution(A, A_disturb, b, b_disturb)

print("x: " , x)

print("x-disturb: ", x_disturb)

print("Max relative error: " , max_rel)

print("Real relative error: ", real_rel)
