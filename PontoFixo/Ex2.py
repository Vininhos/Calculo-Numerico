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
        print("Iteracao " + str(cont) + ": " + str(xn))


def f(x): return (x**3) + (5*x**2) - 12


print(pontofixo(1, 0.1))
