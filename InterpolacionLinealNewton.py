# Datos
x = [3, 4, 5, 6, 7]
y = [91, 135, 190, 260, 345]
t = 3.5

# Encontrar los puntos en los que se encuentra el tiempo t
i = 0
while t > x[i]:
    i += 1

# Imprimir tabla de valores
print("  i    xi   yi   yi+1   f(xi)   f(xi+1)   yi+1 - yi   t - xi   f(t)")
print("-"*65)
for j in range(len(x)-1):
    fx = (y[j+1] - y[j]) / (x[j+1] - x[j])
    if j == i-1:
        f_t = fx
    print(f"{j}    {x[j]}   {y[j]}   {y[j+1]}    {fx:.2f}     {fx:.2f}      {y[j+1]-y[j]:.2f}         {t-x[j]:.2f}   {'-' if j!=i-1 else '+'}")
    
# Interpolación lineal
y_t = ((t - x[i-1]) / (x[i] - x[i-1])) * (y[i] - y[i-1]) + y[i-1]

# Imprimir resultado
print("\nEl volumen de bacterias para el tiempo de 3.5 horas es:")
print(f"({t} - {x[i-1]}) * ({y[i]} - {y[i-1]}) + {y[i-1]}")
print(f"= ({t - x[i-1]:.2f}) * ({y[i] - y[i-1]:.2f}) + {y[i-1]:.2f}")
print(f"= {y_t:.2f}")

