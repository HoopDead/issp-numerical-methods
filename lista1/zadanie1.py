import numpy as np
from matplotlib import pyplot as plt

range_of_plot = np.arange(0, 1.5, 0.0001)
zeroes = np.zeros(len(range_of_plot))
y = np.cos(range_of_plot) - 3*np.sin(np.tan(range_of_plot) - 1)
plt.title("F(x)")
plt.plot(range_of_plot, y)
plt.plot(range_of_plot, zeroes)
plt.show()


# If range is set for 1.5, the result should be 1
