import numpy as np
from scipy.integrate import dblquad

def f(y, x):
    return np.sin(np.pi * x) * np.sin(np.pi * (y - x))

ans = dblquad(f, 0, 1, lambda x: 0, lambda x: x)

print(f"Wynik: {ans[0]}")