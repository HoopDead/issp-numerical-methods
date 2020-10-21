import math

i_start = 1

for i in range(2, 21):
    i_next = math.e - (i + 1) * i_start
    print(f"Wartosc calki dla ( n = {i}): {i_next}")
    i_start = i_next 