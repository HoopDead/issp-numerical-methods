import numpy as np
from scipy.interpolate import CubicSpline
from scipy.misc import derivative

x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])

spl = CubicSpline(x, y)

print(f"Pochodna pierwszego rzędu w punkcie (x = 0) = {derivative(spl, 0, 1e-6, 1)}")
print(f"Pochodna drugiego rzędu w punkcie (x = 0) = {derivative(spl, 0, 1e-6, 2)}")