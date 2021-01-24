import numpy as np
from scipy.integrate import quad

angles = [np.pi / 12, np.pi / 6, np.pi / 4]

def f(t, t0):
    return (1 / np.sqrt(1 - np.sin(t0/2)**2 * np.sin(t)**2))

for x in angles:

    ans = quad(f, 0, np.pi/2, args=(x))
    print(f"{round(x * 180 / np.pi, 1)}, {ans[0]}, {(np.pi/2.0)-ans[0]}")
