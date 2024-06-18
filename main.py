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

mysettings = animationSettings(1280,720,1,0,100,100)
myAnim = methanimator(f,mysettings)