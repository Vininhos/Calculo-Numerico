import numpy as np

matriz = np.array([[10.0, 2.0, 1.0, 7.0],
                   [1.0, 5.0, 1.0, -8.0],
                   [2.0, 3.0, 10.0, 6.0]])

e = 10
n = 3
x = np.array([0.7, -1.6, 0.6])
b = np.array([0.0, 0.0, 0.0])
g = np.array([0.0, 0.0, 0.0])
erro = 0.01
iterador = 0

i = 0
j = 0
print("Matriz:")
while i < n:
    while j < (n + 1):
        print(matriz[i][j], end="   ")
        j = j + 1
    print("\n")
    i = i + 1
    j = 0
print("\n")

print("Vetor de iteração:", iterador, "é:")

i = 0
while i < n:
    if i != (n - 1):
        print(x[i], ",", end="   ")
    else:
        print(x[i], end="\n")
    i = i + 1

i = 0
while i < n:
    b[i] = matriz[i][n]
    i = i + 1

saida = 0
aux = 0
eaux = 0
while saida < 15:
    i = 0
    while i < n:
        aux = b[i]
        j = 0
        while j < n:
            if i != j:
                aux = aux - (matriz[i][j] * x[j])
            j = j + 1
        g[i] = aux / matriz[i][i]
        i = i + 1

    i = 0
    while i < n:
        if i == 0:
            e = abs(g[i] - x[i])
        else:
            eaux = abs(g[i] - x[i])
        if eaux > e:
            e = eaux
            eaux = 0
        x[i] = g[i]
        i = i + 1

    iterador = iterador + 1
    saida = saida + 1
    eaux = 0

    i = 0
    if saida == 15:
        print("\nResultado final:")
    else:
        print("Vetor de iteração:", iterador, "é:")

    while i < n:
        if i != (n - 1):
            print("x" + str(i + 1), '{0:.6f}'.format(x[i]), ",", end="   ")
        else:
            print("x" + str(i + 1), '{0:.6f}'.format(x[i]), end="\n")
        i = i + 1

    # if e < erro:
    # saida = 1000
