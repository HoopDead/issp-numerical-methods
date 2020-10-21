import math

for i in range(2, 25, 2):
    x = 2**(-i)

    equation_1 = math.sqrt(x**4 + 4) - 2
    equation_2 = (x**4)/(math.sqrt(x**4 + 4) + 2)

    print(f"Wynik dla równania pierwszego (n = {i}): {equation_1}")
    print(f"Wynik dla równiania drugiego (n = {i}): {equation_2}")