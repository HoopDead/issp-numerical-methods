import math

for i in range(2, 25, 2):
    x = 2**(-i)

    equation_1 = math.sqrt(x**2 + 1) - 1

    equation_2 = (x**2)/(math.sqrt(x**2 + 1)+1)  # <- Bardziej dokładnie obliczenie
    print(f"Dla równania pierwszego ( n = {i}): {equation_1}")
    print(f"Dla równania drugiego ( n = {i}): {equation_2}")