import numpy as np
from scipy.integrate import quadrature

def f(x):
    return (np.cos(x) - np.exp(x))/np.sin(x)

result = quadrature(f, -1, 1)

print(f"Wynik: {round(result[0], 10)}")