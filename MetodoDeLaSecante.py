def secant_method(f, x0, x1, eps, max_iter):
    """
    Implementación del método de la secante para encontrar la raíz de la función f
    con una precisión de eps, utilizando x0 y x1 como valores iniciales.
    """
    fx0 = f(x0)
    fx1 = f(x1)
    iteraciones = [(0, x0, x1, fx0, fx1, x1, abs(x1-x0))]
    for i in range(1, max_iter+1):
        x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
        tolerancia = abs(x2 - x1)
        if tolerancia < eps:
            iteraciones.append((i, x1, x2, fx1, f(x2), x2, tolerancia))
            break
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = f(x1)
        iteraciones.append((i, x0, x1, fx0, fx1, x2, tolerancia))
    return x1, iteraciones

# Ejemplo de uso:
import math
import pandas as pd

# Definimos la función que queremos encontrar la raíz
def f(x):
    return math.cos(x) - x

# Llamamos a la función secant_method con los valores iniciales x0=0.5 y x1=1.0
# y una precisión de eps=1e-6 y un máximo de iteraciones de 10
raiz, iteraciones = secant_method(f, 0.5, 1.0, 1e-6, 10)

# Creamos una tabla con los valores de cada iteración
tabla = pd.DataFrame(iteraciones, columns=["i", "xi-1", "xi", "f(xi-1)", "f(xi)", "xi+1", "tolerancia"])

# Imprimimos la tabla y el resultado final
print(tabla)
print("La raíz de la función es:", raiz)
