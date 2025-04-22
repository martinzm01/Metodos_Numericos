def regula_falsi(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b]")
    historial = []
    for i in range(max_iter):
        fa, fb = f(a), f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        historial.append((i+1, a, b, c, fc))
        if abs(fc) < tol:
            return c, i+1, historial
        if fa * fc < 0:
            b = c
        else:
            a = c
    return c, max_iter, historial
