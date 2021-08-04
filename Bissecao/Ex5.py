import math
import numpy as np


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
        print("Iteracao " + str(cont) + ": " + str(xi))
        cont = cont + 1


def f(x): return (x - 2) ** np.negative(x)


# def f(x): return (2 * x) * math.cos(2 * x) - ((x + 1) ** 2)  # 𝑝𝑎𝑟𝑎 − 3 ≤ 𝑥 ≤ −2 𝑒 − 1 ≤ 𝑥 ≤ 0


# def f(x): return (x * math.cos(x)) - math.pow(2 * x, 2) + (3 * x) - 1  # 𝑝𝑎𝑟𝑎 0,2 ≤ 𝑥 ≤ 0,3 𝑒 1,2 ≤ 𝑥 ≤ 1,3


print(bissecao(0, 1, math.pow(10, -5)))
