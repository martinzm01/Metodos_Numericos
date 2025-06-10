def regla_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par para aplicar Simpson")
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        factor = 4 if i % 2 != 0 else 2
        suma += factor * f(a + i * h)
    return (h / 3) * suma
