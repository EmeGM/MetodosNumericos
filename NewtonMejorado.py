import math
import matplotlib.pyplot as plt

def newton_mejorado(f, df, x0, tol, max_iter):
    """
    Implementación del método de Newton mejorado para encontrar raíces de una función.
    
    :param f: La función de la cual se busca la raíz.
    :param df: La derivada de la función f.
    :param x0: El punto inicial para comenzar la iteración.
    :param tol: La tolerancia para el criterio de parada.
    :param max_iter: El número máximo de iteraciones permitidas.
    :return: La raíz encontrada y el número de iteraciones realizadas.
    """
    
    print("i\t|\tx\t\t|\tf(xi)\t\t|\tf'(xi)\t\t|\txr\t\t|\tTol")
    print("---------------------------------------------------------------------")
    
    iter_count = 0
    x = x0
    
    while True:
        iter_count += 1
        
        fx = f(x)
        dfx = df(x)
        
        # Calcula la nueva aproximación con la fórmula del método de Newton mejorado
        xr = x - fx/dfx + 0.5*math.pow(fx,2)/(dfx*math.pow(dfx,2)-math.pow(fx,2))
        
        # Calcula la tolerancia en esta iteración
        tol_i = abs(xr - x)
        
        # Imprime la información de la iteración actual
        print(f"{iter_count}\t|\t{x:.8f}\t|\t{fx:.8f}\t|\t{dfx:.8f}\t|\t{xr:.8f}\t|\t{tol_i:.8f}")
        
        # Verifica si se ha alcanzado la tolerancia o se ha excedido el número máximo de iteraciones
        if tol_i < tol or iter_count >= max_iter:
            break
        
        x = xr
    
    print("---------------------------------------------------------------------")
    
    # Graficar la función y la raíz encontrada
    x_vals = [i/10 for i in range(-50, 50)]
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals, y_vals)
    plt.axhline(y=0, color='black', linestyle='--')
    plt.axvline(x=xr, color='red', linestyle='--')
    plt.title('Función y raíz encontrada')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
    return xr, iter_count

# Definir la función y su derivada
def f(x):
    return x**3 - 5*x + 3

def df(x):
    return 3*x**2 - 5

# Establecer los parámetros iniciales
x0 = 1
tol = 1e-6
max_iter = 100

# Llamar al método de Newton mejorado
raiz, num_iter = newton_mejorado(f, df, x0, tol, max_iter)

# Imprimir la solución y el número de iteraciones realizadas
print(f"\nLa raíz es {raiz:.6f} después de {num_iter} iteraciones.")

