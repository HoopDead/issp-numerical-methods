from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.signal import argrelextrema
import numpy as np

def f(u, x):
    return (u[1], -11*u[1] -24*u[0])

y0 = [0, -7]
ts = np.linspace(0, 1, 200)

index = 1

us = odeint(f, y0, ts)
ys = us[:, 0]
plt.plot(ts, ys, '-')

list_of_points = dict(zip(ys, ts))

for y, x in list_of_points.items():
    print(f"Numer punktu: {index}, punkt na osi y (wartość): {y}, punkt na osi x (argument): {x}")
    index += 1

extrema_index = argrelextrema(ys, np.less)[0]
plt.plot(ts[extrema_index], ys[extrema_index], 'r*')
print(f"Punkt, w jakim znajduje sie ekstremum, na osi y: {ys[extrema_index]}, na osi x: {ts[extrema_index]}")
plt.grid()
plt.title("Wykres funkcji y'' + 11y' + 24y = 0 ")
plt.xlabel("Argumenty t")
plt.ylabel("Wartości y")
plt.legend(["y'' + 11y' + 24y", "Ekstremum"])
plt.show()
