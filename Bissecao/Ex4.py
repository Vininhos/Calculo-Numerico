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


# 4. a) -1,4150391 b) 1,4150391 c) 2,7314453 d) -0,7314453
def f(x): return math.pow(x, 4) - math.pow(2 * x, 3) - math.pow(4 * x, 2) + (4 * x) + 4


print("   a")
print(bissecao(-2, -1, math.pow(10, -3)))
print("   b")
print(bissecao(-0, -2, math.pow(10, -3)))
print("   c")
print(bissecao(2, 3, math.pow(10, -3)))
print("   d")
print(bissecao(-1, 0, math.pow(10, -3)))
