def pontofixo(x0, erro):
    cont = 0
    saida = cont
    while saida < 100:
        if cont == 0:
            print("Iteracao: " + str(cont) + ": " + str(x0))
        cont = cont + 1
        saida = cont
        xn = f(x0)
        e = abs(xn - x0)
        x0 = xn
        if e < erro:
            saida = 1000
        print("Iteracao", cont, ":", xn)


def f(x): return (x ** 4) + (x ** 3) + (9 * (x ** 2)) - (2 * x) - 1


print(pontofixo(2, 0.00001))
