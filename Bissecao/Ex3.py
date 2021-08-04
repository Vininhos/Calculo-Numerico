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
        print("Iteracao " + str(cont) + ": " + str(xi))
        cont = cont + 1


def f(x): return (math.pow(x, 3)) - math.pow(7 * x, 2) + (14 * x) - 6


print("   a)")
print(bissecao(0, 1, 0.1))
print("   b)")
print(bissecao(1, 3.2, 0.1))
print("   c)")
print(bissecao(3.2, 4, 0.1))
