from scipy import optimize
import math as m
import numpy as np

def f(param_in):
    x, y = param_in
    f_1 = m.tan(x) - y - 1
    f_2 = m.cos(x) - 3 * m .sin(y)
    return [f_1, f_2]



ans = list()
if __name__ == "__main__":
    for x in np.arange(0, 1.5, 0.001):
        for y in np.arange(0, 1.5, 0.01):
            root = optimize.fsolve(f, [x, y])
            if [round(root[0], 3), round(root[1], 3)] not in ans and round(root[0], 3) >= 0 and round(root[0], 3) <= 1.5:
                ans.append([round(root[0], 3), round(root[1], 3)])

print(ans)
