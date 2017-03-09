# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:36:56 2017

Cada término en la serie de Fibonacci es generado a partir de la suma de los 
dos términos previos, empezando de 1 y 2, los diez primeros términos serán: 
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … Considerando los términos de la serie de 
Fibonacci que son impares, y por debajo de un millón encuentre la suma de 
dichos términos.



@author: ger
"""

fiboacci = [1,2]

while max(fiboacci) < 1000000:
    fiboacci.append(fiboacci[-1] + fiboacci[-2])

nums = []
for i in fiboacci:
    if i%2 == 0:
        nums.append(i)
        
print(nums)

print('suma:', str(sum(nums)))