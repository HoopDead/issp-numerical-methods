from scipy import misc
import numpy as np

def f(x):
    return np.log(np.tanh(x / (x**2 + 1)))

print(f"Pochodna pierwszego rzedu = {misc.derivative(f, 0.2, 1e-6, 1)}")
print(f"Pochodna drugiego rzedu = {misc.derivative(f, 0.2, 1e-6, 2)}")
print(f"Pochodna trzeciego rzedu = {misc.derivative(f, 0.2, 1e-4, 3, order = 5)}")