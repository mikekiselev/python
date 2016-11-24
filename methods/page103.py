# page 103

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

def f(x) :
    f = x
    if x > 0.5 : f = 0
    return f

N = 32

y = np.zeros((N), 'float')
t = np.zeros((N), 'float')

for k in range(N):
    t[k] = np.float(k)/N
    y[k] = f(t[k])

x = fftpack.fft(y)
z = np.sqrt(x.real**2 + x.imag**2)

plt.figure(1)
plt.bar(range(N), z, align='center', width =0.5, color='g')
plt.xlabel('$k$')
plt.ylabel('$x_k$')
plt.figure(2)
y1 = fftpack.ifft(x)
plt.plot(t, y, ':', label='exact')
plt.plot(t, y1, '--', label='direct-invers')
plt.xlabel('$t$')
plt.legend(loc=1)
plt.show()
