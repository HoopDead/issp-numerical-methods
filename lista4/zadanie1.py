from scipy import optimize

def f(x):
    return (2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1)


print(optimize.ridder(f,-10,-6))
print(optimize.ridder(f,-6,4))
print(optimize.ridder(f, 0, 0.12145))
print(optimize.ridder(f, 0.12146, 5))