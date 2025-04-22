import numpy as np
def jacobi(A, b, x0=None, tol=1e-5, max_iter=100):
    n = len(b)
    x = x0 or np.zeros(n)
    historial = []
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        historial.append(np.copy(x_new))
        if np.linalg.norm(x_new - x) < tol:
            return x_new, k+1, historial
        x = x_new
    return x, max_iter, historial
