# page 101
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spec

def Plot(x, y, label, figure, line, axis = [-1,1, 1, 1], loc='true') :
    plt.figure(figure)
    plt.plot(x, y, line, label=label)
    plt.title('this function', fontsize='large', va='bottom', ha='right')
    plt.xlabel('x')
    plt.ylabel(figure)
    plt.legend(loc)
    plt.axis(axis)
    plt.grid(True)


x = np.arange(-5, 5, 0.01)
y = spec.gamma(x)

for i in x:
    if y[i] >1.e20: y[i] =1.e20
    if y[i] < -1.e20: y[i] = -1.e20


Plot(x, y, '$\\Gamma(x)$', 1,'-.', [-5., 5., -20., 20.])

plt.show()

