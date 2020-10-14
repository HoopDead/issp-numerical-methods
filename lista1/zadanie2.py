import numpy as np
from matplotlib import pyplot as plt


a = 0.1 # Start condition  
b = 3.5*a*(1-a) # First item in list
ans = [a, b]


"""
Iterative method for getting next items of progression
"""
for i in range(1, 100):
    a = b
    b = 3.5*a*(1-a)
    ans.append(b)


x_for_plot = np.arange(0, len(ans))
plt.scatter(x_for_plot, ans)
plt.show()

print(ans)
print(x_for_plot)
