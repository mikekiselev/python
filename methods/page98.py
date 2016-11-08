# page 98
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spec

def Plot(x, y, label, figure, line) :
    plt.figure(figure)
    plt.plot(x, y, line, label=label)
    plt.title('this function', fontsize='large', va='bottom', ha='right')
    plt.xlabel('x')
    plt.ylabel('$f(x)$')
    plt.legend(loc='lower left')
    plt.grid(True)


x = np.linspace(-1., 1., 100)
y1 = np.sin(2*np.pi*x)
y2 = x**2

Plot(x, y1, '$sin(2*pi*x)$', 1, 'r')
Plot(x, y2, '$x^2$', 2, 'd')

plt.show()

