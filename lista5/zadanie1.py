from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

# y = 1.225, 0.905, 0.652
# x = 0,     3,     6

x = [0, 3, 6]
y = [1.225, 0.905, 0.652]

f = interpolate.interp1d(x, y, kind = 'quadratic')


xnew = np.arange(0, 6, 0.01)
ynew = f(xnew)   # use interpolation function returned by `interp1d`

plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()