def secant(f, x0, x1, tol=1e-5, max_iter=100):
    historial = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            raise ZeroDivisionError("División por cero en el método de la secante")
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        historial.append((i+1, x0, x1, x2, f(x2)))
        if abs(x2 - x1) < tol:
            return x2, i+1, historial
        x0, x1 = x1, x2
    return x2, max_iter, historial
