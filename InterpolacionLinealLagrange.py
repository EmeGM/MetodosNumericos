def lagrange_interpolation(x, y, x_interpolate):
    
    n = len(x)
    interpolated_value = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_interpolate - x[j]) / (x[i] - x[j])
        interpolated_value += term
        
    return interpolated_value

# Datos
x = [0, 1]
y = [-2, 1]
x_interpolate = 3

# Resultados
print("Polinomio de interpolación usando la fórmula de Lagrange:")
print(f"{'i':<5} {'L(x)':<10} {'Numerador':<20} {'Denominador':<20} {'f(x)':<10}")
for i in range(len(x)):
    numerador = ""
    denominador = ""
    for j in range(len(x)):
        if i != j:
            numerador += f"(x - {x[j]})"
            denominador += f"({x[i]} - {x[j]})"
    print(f"{i:<5} L{i}(x) = ", end="")
    print(f"{numerador:<20} / {denominador:<20} * {y[i]:<10}")
    
# Interpolación
interpolated_value = lagrange_interpolation(x, y, x_interpolate)
print(f"\nInterpolated value at x = {x_interpolate}: {interpolated_value}")
