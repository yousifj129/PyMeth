import methlib.PyMeth as pymeth
from methlib.PyMeth import *

def square(x):
    return x**2



print(NumericalMeth.derivative(square,2.5,0.0001))

