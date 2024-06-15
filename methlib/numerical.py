import numpy as np
from numpy.linalg import *

"""solving problems numerically, like derivatives and definite integrals instead of solving it symbolically"""
class NumericalMeth():

    def derivative(f:callable,x, delta_x = 0.001, rounding=3):
        # calculate the derivative at any point x
        d = (f(x+delta_x)-f(x))/delta_x
        return np.round(d,rounding)
    
    def integral(f:callable,a,b,number_of_bars:float, rounding=3):
        delta_x = (b-a)/number_of_bars
        sum = 0
        for k in range(number_of_bars):
            sum = sum + f(a + k*delta_x)*delta_x

        return np.round(sum,rounding)

    

