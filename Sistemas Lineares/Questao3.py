import numpy as np
from numpy import diag, diagflat, dot, linalg


def jacobi(A, b, n=0, x=None):
    # Criação de um vetor diagonal dos elementos do Array A para fazer a subtração do Array.
    D = diag(A)
    R = A - diagflat(D)

    # Itera até N vezes para encontrar o valor Ax=b.
    for i in range(n):
        # "dot" realiza o produto escalar de dois arrays.
        x = (b - dot(R, x)) / D
        print("Iteração ", i, ":\n", x)
    return x


A = np.array([[10.0, 2.0, 1.0], [1.0, 5.0, 1.0], [2.0, 3.0, 10.0]])
b = np.array([1.0, 1.0, 1.0])
aproxInicial = np.array([0.7, -1.6, 0.6])

print("A: ", A)
print("b: ", b)

print("Resultado final Jacobi: ", jacobi(A, b, 25, aproxInicial))

print("Calculo realizado também através do numpy.linalg para comparar.")
print("Resultado final pelo numpy:\n", linalg.solve(A, b))
