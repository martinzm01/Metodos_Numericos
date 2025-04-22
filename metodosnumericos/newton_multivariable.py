from sympy import symbols, Matrix, lambdify
import numpy as np

def newton_multivariable(exprs_str, x0_vals, tol=1e-5, max_iter=100):
    """
    Resuelve un sistema no lineal con Newton-Raphson multivariable.
    - exprs_str: lista de strings con las ecuaciones (p.ej. ["x**2+y-1", "x-y**2+2"])
    - x0_vals: lista o tuple con el punto inicial (p.ej. [1.0, 1.0])
    - tol, max_iter: tolerancia e iteraciones máximas.

    Devuelve (solucion, iteraciones, historial), donde historial es
    una lista de tuplas (k, x_k, F(x_k), Δx_k, x_{k+1}).
    """
    # 1) Detectar y ordenar variables
    all_syms = set()
    for s in exprs_str:
        all_syms |= set(symbols(s))
    vars_list = sorted(all_syms, key=lambda v: v.name)
    X = Matrix(vars_list)

    # 2) Construir vector simbólico de funciones y su Jacobiano
    F_sym = Matrix([eval(s, {v.name:v for v in vars_list}) for s in exprs_str])
    J_sym = F_sym.jacobian(X)

    # 3) Lambdify para evaluación numérica
    F_num = lambdify([X], F_sym, modules="numpy")
    J_num = lambdify([X], J_sym, modules="numpy")

    # 4) Inicialización
    x = np.array(x0_vals, dtype=float)
    historial = []

    # 5) Iteraciones de Newton multivariable
    for k in range(1, max_iter+1):
        Fx = np.array(F_num(x), dtype=float).flatten()
        Jx = np.array(J_num(x), dtype=float)
        if np.linalg.cond(Jx) > 1e12:
            raise ZeroDivisionError("Jacobian casi singular en iteración %d" % k)

        dx = np.linalg.solve(Jx, -Fx)
        x_new = x + dx
        historial.append((k, x.copy(), Fx, dx, x_new.copy()))

        if np.linalg.norm(dx, ord=np.inf) < tol:
            return x_new, k, historial

        x = x_new

    # Si no convergió en max_iter
    return x, max_iter, historial
