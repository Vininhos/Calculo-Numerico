import numpy as np

cont = -1


def pivotamento():
    u = cont
    while u < n:
        if u != 0:
            if abs(matriz[u][cont]) > abs(matriz[cont][cont]):
                j = 0
                while j < (n + 1):
                    aux[j] = matriz[u - 1][j]
                    matriz[u - 1][j] = matriz[u][j]
                    matriz[u][j] = aux[j]
                    j = j + 1
        u = u + 1


matriz = np.array([[1.0, 1.0, 1.0, 2.0, 1.0, 6.0],
                   [1.0, 0.0, 0.0, 2.0, -1.0, 2.0],
                   [1.0, -1.0, 1.0, 2.0, -1.0, 0.0],
                   [0.0, 0.0, 1.0, 0.0, 7.0, 13.0],
                   [2.0, 0.0, 0.0, 0.0, -1.0, 4.0]])

aux = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
x = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
g = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

n = 5
i = 0
j = 0

print("Matriz atual:")
while i < n:
    while j < (n + 1):
        print(matriz[i][j], end="   ")
        j = j + 1
    print("\n")
    i = i + 1
    j = 0
print("\n")

k = 0

while k < (n - 1):
    cont = cont + 1
    pivotamento()
    l = k
    while l < (n - 1):
        i = k
        while i < (n + 1):
            if i == (0 + k):
                pivo = matriz[k][i]
                elemento = matriz[l + 1][i]
                cons = (elemento / pivo)
                novo = -(cons * pivo)
                matriz[l + 1][i] = (elemento + novo)
            else:
                pivo = matriz[k][i]
                elemento = matriz[l + 1][i]
                novo = -(cons * pivo)
                matriz[l + 1][i] = (elemento + novo)
            i = i + 1
        l = l + 1
    k = k + 1

print("Matriz pivoteada:")
i = 0
while i < n:
    while j < (n + 1):
        print(matriz[i][j], end="   ")
        j = j + 1
    print("\n")
    i = i + 1
    j = 0

x[n - 1] = matriz[n - 1][n] / matriz[n - 1][n - 1]

i = n - 1
while i >= 0:
    g[i] = matriz[i][n]
    i = i - 1

i = n - 2
while i >= 0:
    j = n - 1
    while j >= i:
        if i != j:
            g[i] = g[i] - (x[j] * matriz[i][j])
        elif i == j:
            x[i] = g[i] / matriz[i][j]
        j = j - 1
    i = i - 1

i = 1
while i <= n:
    print("x" + str(i), " = ", x[i - 1])
    i = i + 1
