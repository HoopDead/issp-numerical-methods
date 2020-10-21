from scipy.linalg import hilbert, invhilbert, det

print(f"Hilbert 4x4: \n {hilbert(4)}") # Macierz hiblerta dla n = 4
print("===================")
print(f"Odwrotna macierz Hilberta 4x4: \n {invhilbert(4)}") # Macierz hiblerta dla n = 4

print(f"Hilbert 8x8 \n {hilbert(8)}") # Macierz hilberta dla n = 8
print("===================")
print(f"Odwrotna macierz Hilberta 8x8 \n {invhilbert(8)}") # Odwrotna macierz hilberta dla n = 8 

print("============")
for i in range(5, 21):
    print(f"Wyznacznik dla macierzy o wielkosc {i}x{i}: {det(hilbert(i))}")