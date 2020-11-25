from scipy import optimize
import numpy as np



"""
f(x)
Returns the equation from exercise
@params: x -> x[0] = x, x[1] = y
"""
def f(x):
    return [
        x[0] + np.exp(-x[0]) + x[1]**3,
        x[0]**2 + 2*x[0]*x[1] - x[1]**2 + np.tan(x[0])
    ]

if __name__ == "__main__":
    
    ans = list()

    # Searching numbers from given scope
    xy = [
        np.array([-1.270, -1.260]),
        np.array([-0.720, -0.700]),
        np.array([1.200, 1.210])
    ]

    for i in xy:
        x1 = optimize.root(f, i)
        x1 = optimize.root(f, i)
        if (x1.success):
            if(x1.x[0]**2 + x1.x[1]**2 <= 4): # Checking, if given number is in cricle radius (0,2)
                ans.append(x1.x)

    print(ans)
