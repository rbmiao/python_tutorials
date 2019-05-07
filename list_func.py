#!/usr/bin/python

from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     print(functions)
     for func in functions:
         print(x, func, func(x))
         res.append(func(x))
     print(res)
     print("Rongbing")
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

antetokounmpo