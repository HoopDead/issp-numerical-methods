from scipy.optimize import newton
from numpy import random

f = lambda x, a: (x**5) + a
fder = lambda x, a: 5*x**4
a = [num for num in range(0, 5)]
x = random.randn(5)
print(newton(f, x,fprime=fder,args = (a,)))