from scipy import optimize
import numpy as np

# x = 10
# y = 3

# 10 = v0 * cos(a) * t
# 3 = 2 + v0 * sin(a) * t - 4.095 * t^2

# v0 * cos(45) * t = 10
# v0 * sin(45) * t - t^2 * 4.095 = 1

# v0 * 0.70710678118 * t = 10
# v0 * 0.70710678118 * t - t^2 * 4.095 = 1

def f(param_in):
    v0, t = param_in
    f_1 = v0 * 0.70710678118 * t - 10
    f_2 = v0 *  0.70710678118 * t - t**2 * 4.095 - 1
    return [f_1, f_2]

if __name__ == "__main__":
    ans = list()
    for v0 in np.arange(0, 25, 0.1):
        for t in np.arange(0, 10, 0.1):
            root = optimize.fsolve(f, [v0, t])
            if [round(root[0], 3), round(root[1], 3)] not in ans and round(root[0], 3) >= 1:
                ans.append([round(root[0], 3), round(root[1], 3)])

print(f"Potrzebna predkosc to {ans[0][0]}")