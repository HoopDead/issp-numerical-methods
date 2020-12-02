from scipy import optimize
import numpy as np
import math as m

# x = 10
# y = 3

# 10 = v0 * cos(a) * t
# 3 = 2 + v0 * sin(a) * t - 4.095 * t^2

# v0 * cos(45) * t = 10
# v0 * sin(45) * t - t^2 * 4.095 = 1

# v0 * 0.70710678118 * t = 10
# v0 * 0.70710678118 * t - t^2 * 4.095 = 1

g = 9.81

def f(param_in):
    v0, angle = param_in
    t = 10 / (v0 * np.cos(angle))
    f_1 = v0 * np.sin(angle) * t - ((g * t**2)/2) - 1
    f_2 = v0 * (np.sin(angle) + np.cos(angle)) - (g*t)
    return [f_1, f_2]

if __name__ == "__main__":
    ans = list()
    for v0 in np.arange(0.1, 25, 0.1):
        for angle in np.arange(1, 90, 1):
            root = optimize.fsolve(f, [v0, angle])
            if [round(root[0], 3), round(root[1], 3)] not in ans:
                ans.append([round(root[0], 3), round(root[1], 3)])


print(f"Potrzebna predkosc to {ans[0][0]} m/s, potrzebny kat poczatkowy to {ans[0][1]} stopni")