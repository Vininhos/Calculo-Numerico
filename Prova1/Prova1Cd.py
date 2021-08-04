def secante(x0, x1, erro):
    cont = 0
    saida = 0
    e = 10
    while saida < 100:
        if cont == 0:
            print("Iteracao", cont, ":", x0)
        cont = cont + 1
        saida = cont
        xn = ((x0 * f(x1)) - (x1 * f(x0))) / (f(x1) - f(x0))
        e = abs(xn - x1)
        x0 = x1
        x1 = xn
        if e < erro:
            saida = 1000
        print("Iteracao", cont, ":", "{:1.8s}".format(str(x0)))


def f(x): return (x ** 4) + (x ** 3) + (9 * (x ** 2)) - (2 * x) - 1


print(secante(0.4, 0.8, 0.00001))
