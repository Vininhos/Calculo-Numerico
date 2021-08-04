import numpy as np
from numpy import linalg


def gauss(A, b, x=None, n=15):
    # retorna os elementos de A zerados na diagonal
    cont = 0
    L = np.tril(A)
    U = A - L
    for i in range(n):
        # Produto escalar da matriz inversa de L e a escalar do Ux - b)
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print("\nIteração ", cont, ":\n", x)
        cont = cont + 1
    return x


A = np.array([[5.0, 1.0, 1.0], [3.0, 4.0, 1.0], [3.0, 3.0, 6.0]])
b = [5, 6, 0]
x = [0, 0, 0]

print("\nCalculo realizado também através do numpy.linalg para comparar.\n")
print("Sistema resolvido pelo numpy:\n", linalg.solve(A, b))

print("\nGauss:\n", gauss(A, b, x, 15))
