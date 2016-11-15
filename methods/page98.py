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
y1 = spec.chebyt(1)(x)
Plot(x, y1, '$T_1(x)$', 1,'-')

y2 = spec.chebyt(2)(x)
Plot(x, y2, '$T_2(x)$', 1,'--')

y3 = spec.chebyt(3)(x)
Plot(x, y3, '$T_3(x)$', 1,'-.')

y4 = spec.chebyt(4)(x)
Plot(x, y4, '$T_4(x)$', 1,':')

plt.show()

