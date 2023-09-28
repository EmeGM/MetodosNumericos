def regla_falsa(func, a, b, tol, max_iter):
    # Inicializar los valores de las variables
    iter_num = 0
    error = abs(b - a)
    fa = func(a)
    fb = func(b)
    c = a - (fa * (b - a)) / (fb - fa)
    fc = func(c)

    # Imprimir la cabecera de la tabla
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(
        "Iteración", "a", "b", "c", "f(a)", "f(c)", "Error"))

    # Realizar iteraciones hasta alcanzar la tolerancia o el máximo número de iteraciones
    while fc != 0 and error > tol and iter_num < max_iter:
        # Actualizar los valores de los puntos a, b y c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        # Calcular el nuevo valor de c y el error
        c = a - (fa * (b - a)) / (fb - fa)
        fc = func(c)
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

# Llamar a la función regula_falsi para encontrar la raíz
raiz = regla_falsa(f, 1, 2, 0.001, 10)

# Imprimir la raíz aproximada
print("\nLa raíz aproximada de la función es: {:.4f}".format(raiz))
