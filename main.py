import methlib.PyMeth as pymeth
from methlib.PyMeth import *


def square(x):
    return 2*x

X = np.array(range(10))

print(NumericalMeth.integral(square,0,5,1000))


y,x = sp.symbols("y x")

y = 2*x

print(SymbolicMeth.integral(y=y,wi=x))
    