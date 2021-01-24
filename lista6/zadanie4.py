import numpy as np
from scipy.integrate import simps

def f(x):
    return np.cos(2 * np.cos(x)**(-1))

values = [3, 5, 7]

for i in values:
    x = np.linspace(-1, 1, i)
    y = list()
    for num in x:
        y.append(f(num))
    print(f"Wynik {simps(y, x)}")

# Według Wolframaalpha i wyników uzyskanych przez program można wnioskować, że im większy numer węzła, tym dokładniejszy wynik