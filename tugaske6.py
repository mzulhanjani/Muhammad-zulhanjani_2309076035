import numpy as np
A = np.array([[1, 1, 1],
              [1, 2, -1],
              [2, 1, 2]], dtype=float)
B = np.array([6, 2, 10], dtype=float)
n = len(B)
for i in range(n):
    A[i] = A[i] / A[i][i]  
    B[i] = B[i] / A[i][i]
    
    for j in range(i + 1, n):
        factor = A[j][i]
        A[j] = A[j] - factor * A[i]
        B[j] = B[j] - factor * B[i]
for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        factor = A[j][i]
        A[j] = A[j] - factor * A[i]
        B[j] = B[j] - factor * B[i]
print("Solusi: x1 =", B[0], "x2 =", B[1], "x3 =", B[2])
