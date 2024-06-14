import numpy as np
from numpy.linalg import *

"""solving problems numerically, like derivatives and definite integrals instead of solving it symbolically"""
class NumericalMeth():

    def derivative(f:callable,x, delta_x = 0.001, rounding=3):
        # calculate the derivative at any point x
        d = (f(x+delta_x)-f(x))/delta_x
        
        return np.round(d,rounding)

    

