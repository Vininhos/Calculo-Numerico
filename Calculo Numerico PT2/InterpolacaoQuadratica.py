import numpy as np


def interpolacao(a1, y1, a2, y2, a3, y3):
    matriz = np.array([[pow(a1, 2), a1, 1, y1],
                       [pow(a2, 2), a2, 1, y2],
                       [pow(a3, 2), a3, 1, y3]])
    g = np.array([0.0, 0.0, 0.0])
    x = np.array([0.0, 0.0, 0.0])
    n = 3
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
    while k < n - 1:
        l = k
        while l < n - 1:
            i = k
            while i < n + 1:
                if i == 0 + k:
                    pivo = matriz[k][i]
                    elemento = matriz[l + 1][i]
                    cons = elemento / pivo
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

    print("Resposta final:")
    print("f(x)=", str(x[0]) + "x² +", str(x[1]) + "x +", x[2])

interpolacao(-0.42, 1.63, 0.35, 1.21, 0, -0.81)
