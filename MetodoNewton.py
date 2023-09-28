import numpy as np
import pandas as pd

def f(x):
    return x**3 + 4*x**5 - 12

def f_derivative(x):
    return 3*x**2 + 20*x**4

def newton_method(xi, tolerance, n):
    i = 1
    data = []
    while i <= n:
        fi = f(xi)
        f_di = f_derivative(xi)
        xi_1 = xi - fi/f_di
        error = abs(xi_1 - xi)
        row = [i, xi, fi, f_di, xi_1, error]
        data.append(row)
        if error < tolerance:
            table = pd.DataFrame(data, columns=["Iteración", "xi", "f(xi)", "f'(xi)", "xi+1", "Error"])
            print(table.to_string(index=False))
            print("\nLa raíz aproximada es {:.6f}".format(xi_1))
            return
        xi = xi_1
        i += 1
    table = pd.DataFrame(data, columns=["Iteración", "xi", "f(xi)", "f'(xi)", "xi+1", "Error"])
    print(table.to_string(index=False))
    print("\nEl método de Newton falló después de {} iteraciones.".format(n))

# Prueba del método con xi = 1, tolerancia de 0.0001 y 5 iteraciones
newton_method(1, 0.0001, 5)
