import numpy as np
from scipy.interpolate import Akima1DInterpolator


x = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
y = [-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334]

spl = Akima1DInterpolator(x, y)

print(f"Miejsca zerrowe to: {spl.roots()}")
print(f"Wartosc pochodnej w x = 2.1 to {spl(2.1, 1)}")
