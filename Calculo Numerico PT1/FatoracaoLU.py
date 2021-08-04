import numpy as np

matriz = np.array([[1.0, 1.0, 1.0, 1.0, -6.0],
                   [2.0, -1.0, -1.0, 2.0, 20.0],
                   [1.0, 3.0, -1.0, -1.0, -2.0],
                   [0.0, 1.0, 1.0, 1.0, 1.0]])

lu = np.array([[0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0]])
x = np.array([0.0, 0.0, 0.0, 0.0])
y = np.array([0.0, 0.0, 0.0, 0.0])
g = np.array([0.0, 0.0, 0.0, 0.0])
n = 4
i = 0
j = 0

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
        lu[l + 1][k] = cons
        d = 0
        while d < n:
            lu[d][d] = 1
            d = d + 1
        l = l + 1
    k = k + 1

i = 0
print("Matriz:")
while i < n:
    while j < (n + 1):
        print(matriz[i][j], end="   ")
        j = j + 1
    print("\n")
    i = i + 1
    j = 0
print("\n")

i = 0
print("LU:")
while i < n:
    while j < (n + 1):
        print(lu[i][j], end="   ")
        j = j + 1
    print("\n")
    i = i + 1
    j = 0
print("\n")

i = 0
while i < n:
    g[i] = matriz[i][n]
    i = i + 1

y[0] = g[0] / lu[0][0]
i = 0
while i < n:
    j = i
    while j < n:
        if i != j:
            g[i] = g[i] - (y[j] * lu[i][j])
        elif i == j:
            y[i] = g[i] / lu[i][j]
        j = j + 1
    i = i + 1

i = 1
while i <= n:
    print("Y", i, " = ", y[i - 1])
    i = i + 1

print("\n")
i = n - 1
while i >= 0:
    g[i] = y[i]
    i = i - 1

x[n - 1] = g[n - 1] / matriz[n - 1][n - 1]
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
    print("x"+ str(i), " = ", x[i - 1])
    i = i + 1
