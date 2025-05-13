
import math

def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b]")
    historial = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        historial.append((i + 1, a, b, c, fc))
        if abs(fc) < tol or abs(b - a) / 2 < tol:
            return c, i + 1, historial
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    # Si no se encontró dentro del límite de iteraciones, igual devolvemos la mejor aproximación
    c = (a + b) / 2
    return c, max_iter, historial

