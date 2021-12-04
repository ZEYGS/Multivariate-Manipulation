import sympy
import scipy.integrate as integrate
from math import cos,pi

#Numeric integral computation
def f(x):
    return cos(2*pi*x)

ans,err=integrate.quad(f,(0,1))
print((ans, err))

#Finding the analytical integral of the above using sympy.integrate and compare it with the numerical solution.
def f(x):
    x = cos(2*pi*x)
    ans,err = sympy.integrate(f,(0,1))
    
print((ans, err))

#Using the scipy.integrate.dblquad function in SciPy for numeric integral computation
f = lambda y, x: x*y
area = integrate.dblquad(f, 0, 0.5, lambda x: 0, lambda x: 1-2*x)
print((area))