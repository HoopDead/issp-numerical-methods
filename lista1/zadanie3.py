import numpy as np

A = np.matrix([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
B = np.matrix([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
w = np.matrix([[1], [-2], [3]])


print("A*B")
print(A*B)
print("A*w")
print(A*w)
print("B(Aw)")
print(B*(A*w))
print("det(A)")
print(np.linalg.det(A))
print("det(B)")
print("%.1f" % np.linalg.det(B))
print("inverse(A)")
print(np.linalg.inv(A))
print("inverse(B)")
print(np.linalg.inv(B))