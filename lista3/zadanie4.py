import numpy as np
from scipy import linalg

# Zadanie 1

A = np.mat("[-1 1 -4; 2 2 0; 3 3 2]")
b = np.mat("[0; 1; 0.5]")

print(f"{linalg.solve(A, b)} \n")

# Zadanie 2

L = np.matrix([[1, 0, 0], [3/2, 1, 0], [1/2, 11/13, 1]])
U = np.matrix([[2, -3, -1], [0, 13/2, -7/2], [0, 0, 32/13]])
b = np.matrix([[1], [-1], [2]])

y = linalg.solve(L, b)
print(y)
x = linalg.solve(U, y)
print(x)

