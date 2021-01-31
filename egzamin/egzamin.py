from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.signal import argrelextrema
import numpy as np

def f(u, x):
    return (u[1], -11*u[1] -24*u[0])

y0 = [0, -7]
xs = np.linspace(0, 1, 200)
us = odeint(f, y0, xs)
ys = us[:, 0]
plt.plot(xs, ys, '-')

list_of_points = dict(zip(ys, xs))

for y, x in list_of_points.items():
    print(f"Punkt na osi y: {y}, punkt na osi x: {x}")

a = argrelextrema(ys, np.less)
plt.plot(xs[a[0]], ys[a[0]], 'r*')
plt.show()
