import numpy as np
def gauss_seidel(A, b, x0=None, tol=1e-5, max_iter=100):
    n = len(b)
    x = x0 or np.zeros(n)
    historial = []
    for k in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        historial.append(np.copy(x_new))
        if np.linalg.norm(x_new - x) < tol:
            return x_new, k+1, historial
        x = x_new
    return x, max_iter, historial
