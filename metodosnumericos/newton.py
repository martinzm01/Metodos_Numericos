def newton(f, df, x0, tol=1e-5, max_iter=100):
    historial = []
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivada nula: no se puede continuar")
        x_new = x - fx / dfx
        historial.append((i+1, x, fx, dfx, x_new))
        if abs(x_new - x) < tol:
            return x_new, i+1, historial
        x = x_new
    return x, max_iter, historial
