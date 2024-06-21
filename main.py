import methlib.PyMeth as pymeth
from methlib.PyMeth import *

def square(x):
    return 2*x

X = np.array(range(10))

print(NumericalMeth.integral(square,0,5,1000))


y,x = sp.symbols("y x")

y = 2*x

print(SymbolicMeth.integral(y=y,wi=x))

def f(x):
    return np.sin(np.power(x,2))
def g(x):
    return np.cos(x)

def p(x):
    return NumericalMeth.derivative_func_with_func(f,g,x)

mysettings = animationSettings(1280,720,1,0,10,100)
myAnim = methanimator(f,mysettings)