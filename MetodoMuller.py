import math
from tabulate import tabulate

def muller(f, x0, x1, x2, tol, maxiter):
    """
    Encuentra una raíz de la función f(x) utilizando el método de Muller.

    Parámetros:
    f: función a encontrar la raíz
    x0, x1, x2: valores iniciales para la iteración
    tol: tolerancia para el criterio de parada
    maxiter: número máximo de iteraciones

    Retorna:
    (raiz, tabla) donde raiz es el valor de la raíz encontrado y tabla es una lista
    con la información de cada iteración (i, x0, x1, x2, x3, f(x3), error).
    """
    tabla = []
    x3 = 0
    error = tol + 1
    i = 0
    while error > tol and i < maxiter:
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a*h1 + d1
        c = f(x2)
        radicando = b**2 - 4*a*c
        if radicando < 0:
            # Manejar números complejos
            x3 = x2 - (2*c) / (b + complex(0, 1) * math.sqrt(-radicando) - b * a)
        else:
            x3 = x2 - (2*c) / (b + math.copysign(math.sqrt(radicando), b) - b * a)
        error = abs((x3 - x2) / x3)
        x0, x1, x2 = x1, x2, x3
        i += 1
        fila = [i, x0, x1, x2, x3, f(x3), error]
        tabla.append(fila)
        print(tabulate(tabla, headers=["i", "x0", "x1", "x2", "x3", "f(x3)", "error"]))
    return x3, tabla

# Ejemplo de uso
f = lambda x: x**3 - 3*x**2 + 5*x - 10
raiz, tabla = muller(f, 0, 2, 3, 0.0001, 10)
print("La raíz es:", raiz)
