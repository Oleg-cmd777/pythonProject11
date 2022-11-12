# мство с языком Python (семинары)
# Урок 11. Jupyter Notebook и несколько слов об аналитике
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30  (f(x) = 5x^2 + 10x - 30
#
# Определить корни
#
# Найти интервалы, на которых функция возрастает
#
# Найти интервалы, на которых функция убывает
#
# Построить график
#
# Вычислить вершину
#
# Определить промежутки, на котором f > 0
#
# Определить промежутки, на котором f < 0
# .
# В с лучае проблем пищите в телеграм (@STONECF)


import math
from symtable import Symbol

import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-10, 10, 0.01)
# x.astype (int)
# a = -12*pow(x, 4)*math.sin(math.cos(x))
# b = 18*pow(x, 3) + 5*pow(x, 2) + 10*x
# c = 30
#
# #print(x)
#
# def func(x):
#     function = a - b - c
#     return function
# #print(func(x))
# def sqr_roots(a, b, c):
#     dscrt = b**2 - 4*a*c
#     if dscrt >0:
#         x1 = (-b + math.sqrt(dscrt)) / (2*a)
#         x2 = (-b - math.sqrt(dscrt)) / (2*a)
#         return (x1, x2)
#     elif dscrt ==0:
#         x = -b / (2*a)
#         return x
#     else:
#         return None
# #print(func(x))
#
# min_func = min(func(x))
# #print(min_func)


