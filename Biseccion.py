def bisection_method(func, a, b, tol, max_iter):
    # Inicializar los valores de las variables
    iter_num = 0
    error = abs(b - a)
    c = (a + b) / 2
    fc = func(c)

    # Imprimir la cabecera de la tabla
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(
        "Iteración", "a", "b", "c", "f(a)", "f(c)", "Error"))

    # Realizar iteraciones hasta alcanzar la tolerancia o el máximo número de iteraciones
    while fc != 0 and error > tol and iter_num < max_iter:
        # Evaluar la función en los puntos a y c
        fa = func(a)
        fc = func(c)

        # Actualizar los valores de los puntos a o b
        if fa * fc < 0:
            b = c
        else:
            a = c

        # Calcular el nuevo valor de c y el error
        c = (a + b) / 2
        error = abs(b - a)

        # Incrementar el número de iteraciones
        iter_num += 1

        # Imprimir los resultados de la iteración actual
        print("{:<10}{:<10.4f}{:<10.4f}{:<10.4f}{:<10.4f}{:<10.4f}{:<10.4f}".format(
            iter_num, a, b, c, fa, fc, error))

    # Verificar si se alcanzó la tolerancia o el máximo número de iteraciones
    if fc == 0:
        print("\nSe encontró la raíz exacta en la iteración {}.".format(iter_num))
    elif error <= tol:
        print("\nSe alcanzó la tolerancia en la iteración {}.".format(iter_num))
    else:
        print("\nSe alcanzó el máximo número de iteraciones sin encontrar la raíz.")

    # Retornar el valor de la raíz aproximada
    return c
# Definir la función f(x) = x^3 - 4x^2 - 10
def f(x):
    return x**3 - 4*x**2 - 10

# Llamar a la función bisection_method para encontrar la raíz
raiz = bisection_method(f, 1, 2, 0.001, 10)

# Imprimir la raíz aproximada
print("\nLa raíz aproximada de la función es: {:.4f}".format(raiz))
