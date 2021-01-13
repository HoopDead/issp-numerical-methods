import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150])
y = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])


# Metoda polyfit z modulu numpy korzysta z metody najmniejszych kwadatów

function = np.polyfit(x, y, 2)
polynominal = np.poly1d(function)

print(f"p (gestosc powietrza) na wysokosci 10.5km = {polynominal(10.5)}")

x_axis = np.arange(start = 0, stop = 10.5, step = 0.1)

plt.plot(x_axis, polynominal(x_axis))
plt.plot(x, y, '*')
plt.show()