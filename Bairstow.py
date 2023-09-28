import numpy as np

def bairstow(a, r, s, tol=1e-5, maxiter=100):
    n = len(a) - 1
    b = np.zeros(n+1)
    c = np.zeros(n+1)
    r_ = np.zeros(maxiter+1)
    s_ = np.zeros(maxiter+1)
    r_[0], s_[0] = r, s
    
    for i in range(maxiter):
        b[-1], b[-2] = a[-1], a[-2] + r*b[-1]
        c[-1], c[-2] = b[-1], b[-2] + r*c[-1]
        for j in range(n-2, -1, -1):
            b[j] = a[j] + r*b[j+1] + s*b[j+2]
            c[j] = b[j] + r*c[j+1] + s*c[j+2]
        dr = (b[1]*c[2] - b[2]*c[1]) / (c[1]**2 - c[2]*c[0])
        ds = (b[2]*c[0] - b[1]*c[1]) / (c[1]**2 - c[2]*c[0])
        r += dr
        s += ds
        r_[i+1], s_[i+1] = r, s
        if abs(dr/r) < tol and abs(ds/s) < tol:
            break
        
    if i == maxiter-1:
        print('Atencion: Bairstow.')
    if len(r_) > 0 and len(s_) > 0:
        return r_[:i+1], s_[:i+1]
    
    else:
        
        return []

# Ejemplo de uso
f = [1, -3, -2, 16]
raices = bairstow(f, 1, 1)
print(raices)





