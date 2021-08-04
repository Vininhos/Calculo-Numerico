import math


def secante(x0, x1, erro):
    cont = 0
    saida = 0
    x0 = 0
    x1 = 0
    e = 10
    xn = 0
    while saida < 100:
        if cont == 0:
            print("Iteracao " + str(cont) + ": " + str(x0))
        cont = cont + 1
        saida = cont
        xn = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        e = abs(xn - x1)
        x0 = x1
        x1 = xn
        if e < erro:
            saida = 1000
        print("Iteracao " + str(cont) + ": " + str(x0))


def f(x): return math.pow(x, 4) - (4 * math.pow(x, 2) + 4)


print(secante(0.4, 0.8, 0.1))
