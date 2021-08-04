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


def f(x): return 3 * (x + 1) * (x - (1 / 2)) * (x - 1)


# a)
print("   a)")

print(bissecao(-2, 1.5, 0.4))

# b)
print("   b)")

print(bissecao(-1.25, 2.5, 0.4))
