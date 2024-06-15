import numpy as np
import sympy as sp
from sympy.abc import x
class SymbolicMeth():
    def derivative(y):
        return sp.diff(y)
    
    def integral(y,wi,a = 0,b = 0):
        if a == 0 and b == 0:
            return sp.integrate(y,wi)
        else:
            return sp.integrate(y,(wi,a,b))