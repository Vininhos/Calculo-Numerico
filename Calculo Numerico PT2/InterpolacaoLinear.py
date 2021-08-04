import numpy as np


def interpolacaolinear(linha1valor1, linha1valor2, linha2valor1, linha2valor2, linha3valor1, linha4valor2, linha5valor1,
                       linha5valor2):
    n = 5

    matriz = np.array([[linha1valor1, 1.0, linha1valor2],
                       [linha2valor1, 1.0, linha2valor2]])

    x = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    g = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    i = 0
    while i < n:
        j = 0
        while j < (n + 1):
            print(matriz[i][j], end="   ")
            j = j + 1
        print("\n")
        i = i + 1
    print("\n")

    k = 0
    while k < (n - 1):
        l = k
        while l < (n - 1):
            i = k
            while i < (n + 1):
                if i == (0 + k):
                    pivo = matriz[k][i]
                    elemento = matriz[l + 1][i]
                    cons = (elemento / pivo)
                    novo = -(cons * pivo)
                    matriz[l + 1][i] = elemento + novo
                else:
                    pivo = matriz[k][i]
                    elemento = matriz[l + 1][i]
                    novo = -(cons * pivo)
                    matriz[l + 1][i] = elemento + novo
                i = i + 1
            l = l + 1
        k = k + 1

    i = 0
    while i < n:
        j = 0
        while j < (n + 1):
            print(matriz[i][j], end="   ")
            j = j + 1
        print("\n")
        i = i + 1
    print("\n")

    x[n - 1] = matriz[n - 1][n] / matriz[n - 1][n - 1]

    i = (n - 1)
    while i >= 0:
        g[i] = matriz[i][n]
        i = i - 1

    i = (n - 2)
    while i >= 0:
        j = (n - 1)
        while j >= i:
            if i != j:
                g[i] = g[i] - (x[j] * matriz[i][j])
            elif i == j:
                x[i] = g[i] / matriz[i][j]
            j = j - 1
        i = i - 1

    print("P1(x) =", str(x[0]) + "x +", x[1], "\n")


interpolacaolinear(1.0, 2.0, -1.0, 4.0)
interpolacaolinear(7.0, 0.0, 1.0, 3.0)
