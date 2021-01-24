import numpy as np
from scipy.special import roots_legendre

def f(x):
    return (np.log(x) / (x**2 - 2*x + 2))

value_start = 1
value_stop = np.pi
weights_start = [2, 4]

for n in weights_start:
    sample_points, weights, sum_of_weights = roots_legendre(n, mu=True)
    result = 0
    print(sample_points, weights, sum_of_weights)

    for index, item in enumerate(sample_points):
        result += (value_stop - value_start)/2 * f((value_stop + value_start)/2 + (value_stop - value_start)/2 * sample_points[index])*weights[index]


    print(f"n = {result}")