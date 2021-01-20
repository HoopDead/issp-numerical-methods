import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

spl = CubicSpline(x, y)

print(f"Wartosc pochodnej w x = 0.2 to {spl(0.2, 1)}")