import numpy as np


def func(x):
    return x * np.cos(pow(x, 2))


def d2x(x):
    return -4 * pow(x, 3) * np.cos(pow(x, 2)) - 6 * x * np.sin(pow(x, 2))


def erro(x, h):
    return (pow(h, 3) / 12) * abs(d2x(x))


def trapezio(a, b):
    valoranalitico = 0.42073549
    h = b - a
    fx1 = func(a)
    fx2 = func(b)
    valorobtido = (h / 2) * (fx1 + fx2)
    print("Valor obtido:", valorobtido)
    print("Valor analítico - Valor obtido:", valoranalitico - valorobtido)
    print("Valor obtido - Valor analítico:",  valorobtido - valoranalitico, "\n")

    errofx1 = abs(erro(fx1, h))
    errofx2 = abs(erro(fx2, h))

    if errofx1 > errofx2:
        print("O erro é:", errofx1)
        print("Valor analítico - erro:", valoranalitico - errofx1)
        print("erro - Valor analítico:", errofx1 - valoranalitico, "\n")
    else:
        print("O erro é:", errofx2)
        print("Valor analítico - erro:", valoranalitico - errofx2)
        print("erro - Valor analítico:", errofx2 - valoranalitico, "\n")


(trapezio(0, 1))
