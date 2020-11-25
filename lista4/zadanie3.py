import numpy as np

u = 2510 # Predkosc spaln wzgledem rakiety (m/s)
M0 = 2.8 * 10**6 # Masa rakiety w momencie oderwania od ziemi (kg)
m = 13.3 * 10**3 # Szybkosc zuzycia paliwa (kg/s)
g = 9.81 # Przyspieszenie ziemskie (m/s^2)

def v(t):
    return u * np.log(M0/(M0 - (m*t))) - g*t 

t = np.linspace(0, 100, 2000) # Stworzenie dwóch tysięcy liczb w przedziale (0, 100)

for time in t:
    if v(time) >= 335:
         print(f"Czas potrzebny do osiagniecia predkosci 335 m/s {time} sekund") 
         break