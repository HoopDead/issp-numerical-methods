import math

start = 1.0

for i in range(2, 30):
    next = math.e - (i + 1) * start
    print(f"Wartosc dla numeru {i} to {next}")
    start = next