from numpy import linalg
from scipy.linalg import hilbert

matrix_5 = hilbert(5)
matrix_10 = hilbert(10)
matrix_20 = hilbert(20)

# Dla n = 5
print(f"Wskaźnik unormowania macierzy: {linalg.cond(matrix_5)}, norma: {linalg.norm(matrix_5)}")
print(f"Wskaźnik unormowania macierzy: {linalg.cond(matrix_10)}, norma: {linalg.norm(matrix_10)}")
print(f"Wskaźnik unormowania macierzy: {linalg.cond(matrix_20)}, norma: {linalg.norm(matrix_20)}")