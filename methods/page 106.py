# page 106

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

m = 25
h = 1. / (m+1)
h_2 = h**2
A = np.mat(np.zeros((m,m), 'float'))

for i in range (1, m):
    A[i-1,i] = -1./h_2
    A[i,i] = 2./ h_2
    A[i, i-1] =  A[i-1,i]

A[0,0] = 2./ h_2
A[m-1, m-1] =A[0,0]

plt.matshow(A)

print( 'det:',    linalg.det(A))
print ('norm-1:', linalg.norm(A,1))
print ('norm-2:', linalg.norm(A,2))
print ('norm-inf:', linalg.norm(A,np.inf))
print ('norm-inf:', linalg.norm(A,np.inf))

L = linalg.cholesky(A)
plt.matshow(L)
B = linalg.inv(A)
plt.matshow(B, cmap='gray')
b = np.mat(np.ones((m), 'float'))
y = B*b.T
plt.figure(4)
x = np.linspace(h, m*h, m)
plt.plot(x, y, '--', x, x*(1-x)/2, ':')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()