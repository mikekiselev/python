# page 73
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 1., 100)
y1 = np.sin(2*np.pi*x)
y2 = x**2
y3 = np.cos(4*np.pi*x)
plt.plot(x, y1, '-', label='$sin(2*np.pi*x)$')
plt.plot(x, y2, '--', label='$x^2$')
plt.title('this function', fontsize='large', va='bottom', ha='right')
plt.xlabel('x')
plt.ylabel('$f(x)$')
plt.legend(loc='lower left')
plt.grid(True)
plt.show()