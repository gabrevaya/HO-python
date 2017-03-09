# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy

coefs = [1,1,-4,4]
p = np.poly1d(coefs)

xi = -10
xf = 10
dx = 0.1
num = (xf - xi)/dx

x = np.linspace(xi, xf, num)
y = p(x)

y_grad = np.gradient(y, dx, edge_order=2)

plt.figure()
plt.plot(x,y)
plt.plot(x,y_grad)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['Función','Derivada'])
plt.grid()
plt.show

np.savetxt('function.txt', y)