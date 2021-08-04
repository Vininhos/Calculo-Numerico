import math


def bissecao(a, b, tol):
    saida = 0
    cont = 0
    while saida < 100:
        saida = cont
        xi = (a + b) / 2
        fa = f(a)
        fxi = f(xi)
        e = abs(xi - a)
        if fa * fxi >= 0:
            a = xi
        else:
            b = xi
        if e < tol:
            saida = 1000
        print("Iteracao", cont, ":", "{:1.8s}".format(str(xi)))
        cont = cont + 1


def f(x): return (-32.17 / (2 * (1.7 ** 2))) * (-math.e ** (-1.7 * x) - math.sin(1.7 * x))


print(bissecao(2, 3, 0.0001))
