# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:10:36 2017
Si hacemos una lista de todos los números naturales debajo de 10 que sean
múltiplos de 3 o 5 obtendríamos 3, 5, 6 y 9. La suma de los múltiplos es 23.
Encuentre la suma de todos los múltiplos de 3 y 5 debajo de 1000.

@author: ger
"""

nums = []

for i in range(1001):
    if i%3 == 0 or i%5 == 0:
        nums.append(i)

suma = sum(nums)
print('suma:', str(suma))