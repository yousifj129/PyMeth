import methlib.PyMeth as pymeth
from methlib.PyMeth import *

def square(x):
    return x**2

X = np.array(range(10))

print(NumericalMeth.derivative(square,x=X,rounding=1))

