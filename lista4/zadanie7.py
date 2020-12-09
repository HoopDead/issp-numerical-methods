import numpy as np
import math as m

# Answers: -7, -2, 2i, -3i

complex_1 = complex(5, 1)
complex_2 = complex(8, -5)
complex_3 = complex(30, -14)

poly = [1, complex_1, -complex_2, complex_3, -84]

ans = np.roots(poly)

for num in ans:
    print(f"Rzecziwysta dla {num}: {round(num.real, 3)}")
    print(f"Imaginary dla {num}: {round(num.imag, 3)}")