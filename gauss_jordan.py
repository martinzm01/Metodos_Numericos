import numpy as np
def gauss_jordan(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    M = np.hstack([A, b.reshape(-1,1)])
    for i in range(n):
        if M[i, i] == 0:
            raise ValueError("División por cero")
        M[i] = M[i] / M[i, i]
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j, i] * M[i]
    x = M[:, -1]
    return x
