import matplotlib.pyplot as plt
import numpy as np


def f(x): return (x ** 4) + (x ** 3) + (9 * (x ** 2)) - (2 * x) - 1


xx = np.linspace(-2, 2)
plt.plot(f(xx))
plt.grid()
plt.show()
