# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:21:03 2017

@author: ger
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

datos = np.loadtxt('tabla.dat')

x = datos[:,0]
y = datos[:,1]

plt.figure()
plt.plot(x,y,'o')
plt.show

coefs = np.polyfit(x,y,6)
p = np.poly1d(coefs)

x_new = np.linspace(4, 9.5, 100)
y_new = p(x_new)

plt.figure()
plt.plot(x,y,'o')
plt.plot(x_new,y_new)
plt.xlabel('X')
plt.ylabel('Y')
plt.show