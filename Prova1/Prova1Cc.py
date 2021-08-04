def newton(x0, erro):
    cont = 0
    saida = 0
    e = 10
    while saida < 100:
        if cont == 0:
            print("Iteracao", cont, ":", x0)
        cont = cont + 1
        saida = cont
        xn = x0 - (f(x0) / derivada(x0))
        if cont != 1:
            e = abs(xn - x0)
        x0 = xn
        if e < erro:
            saida = 1000
        print("Iteracao", cont, ":", "{:1.8s}".format(str(x0)))


def f(x): return (x ** 4) + (x ** 3) + (9 * (x ** 2)) - (2 * x) - 1


def derivada(x): return (4 * (x ** 3)) + (3 * (x ** 2)) + (18 * x) - 2


print(newton(2, 0.00001))
