import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828])


linear_function = np.polyfit(x, y, 1)
linear_polynominal = np.poly1d(linear_function)

cubic_function = np.polyfit(x, y, 2)
cubic_polynominal = np.poly1d(cubic_function)

x_axis = np.arange(start = 1, stop = 10, step = 0.1)

plt.plot(x_axis, linear_polynominal(x_axis))
plt.plot(x_axis, cubic_polynominal(x_axis))
plt.plot(x, y, '*')
plt.legend(["Funkcja liniowa", "Funkcja kwadratowa", "Punkty danych"])
plt.show()

# Dużo lepiej te dane wypadają dla funkcji kwadratowej - są lepiej dopasowane, co widać na wykresach.