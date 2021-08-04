from __future__ import division
import numpy as np
from numpy import linalg


def fatoraLU(A, B):
    U = np.copy(A)
    n = np.shape(U)[0]
    L = np.eye(n)
    cont = 0
    for i in 100:
        for j in np.arange(n - 1):
            for i in np.arange(j + 1, n):
                L[i, j] = U[i, j] / U[j, j]
                for k in np.arange(j + 1, n):
                    U[i, k] = U[i, k] - L[i, j] * U[j, k]
                    U[i, j] = 0
                    print("Iteração L ", cont, ":\n", L)
                    print("Iteração U ", cont, ":\n", U)
                    cont = cont + 1
        return L, U


A = np.array([[1.0, 1.0, 1.0], [1.0, 2.0, 0], [2.0, 1.0, 1.0]])
B = np.array([[2.97619, -1.66666, 7.02380]])

print("LU resolvido:\n", fatoraLU(A, B))

# Não sei como retornar o valor dos dois parâmetros retornados pela funcao LU, então coloquei manualmente os
# valores que são desenvolvidos por essa função.
print("Sistema resolvido:\n", linalg.solve([[1., 0., 0.], [1., 1., 0.], [2., 0., 1.]],
                                           ([[1., 1., 1.], [0., 1., -1.], [0., -1., -1.]])))
