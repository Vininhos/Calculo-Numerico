import numpy as np


def func(x):
    return x * np.cos(pow(x, 2))


def d2x(x):
    return -4 * pow(x, 3) * np.cos(pow(x, 2)) - 6 * x * np.sin(pow(x, 2))


def erro(a, b, x, h):
    return ((b - a) / 180) * pow(h, 4) * abs(d2x(x))


def simpson(a, b, nIteracoes):
    valoranalitico = 0.42073549
    h = (b - a) / nIteracoes
    fx1 = func(a)
    fx2 = func(b)
    div = h
    soma = 0

    i = 0
    while i < nIteracoes - 1:
        mod = i % 2
        if mod == 0:
            soma = soma + (4 * func(a + div))
            div = div + h
        else:
            soma = soma + (2 * func(a + div))
            div = div + h
        i = i + 1

    valorobtido = (h / 3) * (fx1 + soma + fx2)
    print("A resposta é:", valorobtido)
    print("Valor analítico - Valor obtido:", valoranalitico - valorobtido)
    print("Valor obtido - Valor analítico:", valorobtido - valoranalitico, "\n")

    errofx1 = abs(erro(a, b, fx1, h))
    errofx2 = abs(erro(a, b, fx2, h))

    if errofx1 > errofx2:
        print("O erro é:", errofx1)
        print("Valor analítico - erro:", valoranalitico - errofx1)
        print("erro - Valor analítico:", errofx1 - valoranalitico, "\n")
    else:
        print("O erro é:", errofx2)
        print("Valor analítico - erro:", valoranalitico - errofx2)
        print("erro - Valor analítico:", errofx2 - valoranalitico, "\n")


i = 1
while i <= 6:
    print("Intervalo", str(i) + ":")
    simpson(0, 1, i)
    i = i + 1
