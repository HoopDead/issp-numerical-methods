from scipy import interpolate

# x = 1, 1.25, 1.75, 2, 2.25, 2.5, 2.75, 3
# y = -0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334

x = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
y = [-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334]

spline = interpolate.InterpolatedUnivariateSpline(x, y)
print(f"Miejsca zerowe dla zadanej funkcji to: {spline.roots()}")
spline_d = spline.derivative()