# page 100
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spec

def Plot(x, y, label, figure, line, loc='true') :
    plt.figure(figure)
    plt.plot(x, y, line, label=label)
    plt.title('this function', fontsize='large', va='bottom', ha='right')
    plt.xlabel('x')
    plt.ylabel(figure)
    plt.legend(loc)
    plt.grid(True)


x = np.linspace(0., 20., 100)
y1 = spec.jn(0, x)
Plot(x, y1, '$J_0(x)$', 1,'-')

y2 = spec.jn(1, x)
Plot(x, y2, '$J_2(x)$', 1,'--')

y3 = spec.jn(2, x)
Plot(x, y3, '$J_3(x)$', 1,'-.')

y4 = spec.jn(3, x)
Plot(x, y4, '$T_4(x)$', 1,':')

zeros = spec.jn_zeros(0,6)
for xz in zeros :
    plt.scatter(xz, 0)

plt.show()

