import numpy as np
import matplotlib.pyplot as plt


def f(x): return np.tan(x) - (2 * x ^ 2)


plt.plot(0, f(2))
plt.grid()
plt.show()
