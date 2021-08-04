import numpy as np
import scipy as sci
from scipy import optimize


def g(x): return (x ** 4) + (x ** 3) + (9 * (x ** 2)) - (2 * x) - 1


xe = sci.optimize.fixed_point(g, 0.7)
x0 = 0.7
eps = np.fabs(x0 - xe)
print("x1 = %.5f, eps =~ %.5f" % (x0, eps))
for i in np.arrange(10):
    x = g(x0)
    eps = np.fabs(x - xe)
    print("%s =~ %.5f, eps =~ %.5f" % (('x' + str(i + 2)), x, eps))
    x0 = x

print(g(1))
