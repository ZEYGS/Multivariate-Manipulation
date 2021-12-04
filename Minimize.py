import sympy as sym
from sympy import diff
from sympy.solvers import solve
from scipy.optimize import minimize_scalar
from scipy.optimize import minimize
import numpy as np



#Computing critical value of of  p(x)  by solving  p(x)=0  using SymPy.
x = sym.Symbol('x')
expr = 9*x**2 - 6*x + 2
expr.subs(x,0)

#Using scipy.optimize.minimize_scalar function to compute the minimum of p(x)
def f(x):
    return (9*x**2 - 6*x + 2)

res = minimize_scalar(f)
res.x

#Computing the minimum of the Rosenbrock function
def rosenbrock(x):
    return (1 - x[0])**2 + 100*((x[1] - x[0]**2)**2)

x0 = np.array([0.0, 0.0])
minimum = minimize(rosenbrock, x0)
print(minimum)