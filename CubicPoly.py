import sympy
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Using sympy to find symbolic expressions for three roots in a cubic polynomial
x = sympy.symbols('x')
roots = sympy.roots(816*x**3 - 3835*x**2 + 6000*x - 3125)
print(roots)
xroots = [sympy.N(r) for r in roots] 
print(xroots)
print(np.roots([816.0, -3835.0, 6000.0, -3125]))


#Plotting P(x) for 1.43≤𝑥≤1.71 using a solid line and mark the location of the three roots using circles on the plot
def p(x):
    return (816*x**3 - 3835*x**2 + 6000*x - 3125)

x = np.linspace(1.43, 1.71, 100)
plt.plot(x, 816*x**3 - 3835*x**2 + 6000*x - 3125)

a = 1.4705
b = 1.5625
c = 1.6666

plt.text(a,0.1,"a")
plt.text(b,0.1,"b")
plt.text(c,0.1,"c")

plt.scatter([a,b,c], [p(a), p(b), p(c)], s = 50, facecolors = 'none')
plt.scatter([a,b,c], [0,0,0], s = 50, c = 'red')

xaxis = plt.axhline(0)
pass

#Using the function scipy.optimize.fsolve with starting guesses  X0=1 ,  X0=1.6  and  X0=1.7  to compute the three roots.
def f(x):
    return (816*x**3 - 3835*x**2 + 6000*x - 3125)

x0 = opt.fsolve(f, (1, 1.6, 1.7))
print((x0))

#Using secant method for solving nonlinear equations with implementation to find the root by starting start with  a=1  and  b=2.
def secant(f, a, b, tol=0):
    '''
    Uses secant method to search for a root  of f(x) in the interval [a,b].
    Tol is the convergence threshold on x. If not set a default is provided.
    Returns the root and the number of iterations needed to find it.
    '''
    if tol <= 0:
        tol = np.finfo(float).eps

    fa = f(a)
    for k in range(100):
        fb = f(b)
        if abs(fb) == 0:
            x = b
            break
            
        x = b + ((fb) - (fa))/((b*(fb)) - (b*(fa)));

        if abs(x) < tol*abs(b):
            break
            
        a, fa = b, fb
        b = x
        
        print("root of given equation =", round(x, 9));
        
    else:
        print("cannot find root");

a = 1;
b = 2;
secant(f, a, b, tol=0);


